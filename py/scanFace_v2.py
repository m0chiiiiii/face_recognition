# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanFaceauHGRZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
from dotenv import load_dotenv
from profileInfoWindow import profileWindow
from registerWindow import registerWindow

import cv2
import cv2.data
import numpy as np
import torch
import psycopg2
import os
import resource

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1600, 900)
        font = QFont()
        font.setFamily(u"Poppins")
        font.setStyleStrategy(QFont.PreferDefault)
        Form.setFont(font)
        Form.setStyleSheet(u"*{\n"
"background-color: #efefef;\n"
"font-family: Poppins;\n"
"font-size: 14px;\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(330, 80, 991, 751))
        self.widget.setStyleSheet(u"*{\n"
"background-color: white;\n"
"}\n"
"\n"
"QPushButton#scanBtn{\n"
"background-color: #292929;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton#scanBtn:hover{\n"
"background-color: gray;\n"
"}")
        self.cameraFeed = QLabel(self.widget)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setGeometry(QRect(170, 110, 660, 530))
        self.cameraFeed.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.cameraFeed.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 60, 261, 31))
        self.label.setStyleSheet(u"font-size: 30px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.scanBtn = QPushButton(self.widget)
        self.scanBtn.setObjectName(u"scanBtn")
        self.scanBtn.setGeometry(QRect(420, 670, 161, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Face Card | Scan Face", None))
        self.cameraFeed.setText(QCoreApplication.translate("Form", u"Camera", None))
        self.label.setText(QCoreApplication.translate("Form", u"Scan Face", None))
        self.scanBtn.setText(QCoreApplication.translate("Form", u"Scan Face", None))
    # retranslateUi


class scanFace(QWidget):
    def __init__(self, main_window):
        super().__init__()
        load_dotenv()
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_pass = os.getenv("DB_PASS")

        self.main_window = main_window
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #initialize setup
        self.setupCam()

        #initialization of MTCNN and InceptionResnetV1
        self.mtcnn = MTCNN(keep_all=True)
        self.model = InceptionResnetV1(pretrained='vggface2').eval()

        self.db_embeddings = []
        self.db_labels = []

        self.ui.scanBtn.clicked.connect(self.startScan)

        self.profileWindow = None
        self.frame_counter = 0
    
        self.isScanning = False
        self.isCamOn = False

        self.connect_to_db()
        self.loadDatabaseEmbeddings()

    # db function
    def connect_to_db(self):
        """Connect to the PostgreSQL database"""
        try:
            self.db_connection = psycopg2.connect(
                host = self.db_host,
                port = self.db_port,
                dbname = self.db_name,
                user = self.db_user,
                password = self.db_pass
        )

            self.db_cursor = self.db_connection.cursor()
            print(f'Database connection established successfully.')

        except Exception as e:
            print(f'Error connecting to the database: {e}')
            self.db_connection = None
    

    def loadDatabaseEmbeddings(self):
        try:
            cursor = self.db_cursor
            cursor.execute("SELECT U_FACE_EMBEDDINGS, U_ID FROM USERS")
            rows = cursor.fetchall()

            for row in rows:
                embedding_data = row[0]
                user_id = row[1]

                if isinstance(embedding_data, (bytes, bytearray)):
                    embedding = np.frombuffer(embedding_data, dtype=np.float32)
                elif isinstance(embedding_data, list):
                    embedding = np.array(embedding_data, dtype=np.float32)
                else:
                    print(f"Unexpected embedding format for user {user_id}: {type(embedding_data)}")
                    continue

                embedding = torch.tensor(embedding)
                embedding = embedding / embedding.norm(p=2)

                self.db_embeddings.append(embedding)
                self.db_labels.append(user_id)

            print(f"Loaded {len(self.db_embeddings)} embeddings from database")
        
        except Exception as e:
            print(f"Error loading embeddings: {e}")

    def closeCam(self):
        if self.isCamOn:
            self.timer.stop()
            self.cam.release()
            self.ui.regCameraFeed.clear()
            self.ui.regToggleCamBtn.setText("Off")
            self.isCamOn = False

    # initialize camera
    def setupCam(self):
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self .cam.isOpened():
            print('Error: Could not open camera.')
            return

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateCam)
        self.timer.start(50)

    # camera and face recognition
    def updateCam(self):
        ret, frame = self.cam.read()
        if ret:
            frame = cv2.flip(frame, 1)

            if self.isScanning:
                if self.frame_counter % 5 == 0:
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_image = Image.fromarray(rgb_frame)

                    try:
                        faces = self.mtcnn(pil_image)
                    except ValueError:
                        faces = None

                    if faces is not None:
                        match_found = False
                        for face in faces:
                            embedding = self.model(face.unsqueeze(0))
                            embedding = embedding / embedding.norm(p=2)

                            if self.db_embeddings:
                                distances = [torch.dist(embedding, db_emb).item() for db_emb in self.db_embeddings]
                                min_distance = min(distances)

                                if min_distance < 0.6:
                                    index = distances.index(min_distance)
                                    label = self.db_labels[index]
                                    self.displayProfileInfo(label)
                                    match_found = True
                                    self.showMatchMessage()
                                    break
                
                        if not match_found:
                            self.showNoMatchMessage()
            
                self.frame_counter += 1

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            ht, wd, channel = rgb_frame.shape
            bytes_per_lines = 3 * wd
            q_image = QImage(rgb_frame.data, wd, ht, bytes_per_lines, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.ui.cameraFeed.setPixmap(pixmap.scaled(self.ui.cameraFeed.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)) 


    def showNoMatchMessage(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("No user matched. Please register.")
        msg_box.setWindowTitle("User Not Found")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.buttonClicked.connect(self.openRegisterWindow)
        msg_box.exec_()
        self.stopScan()
        self.closeCam()

    def showMatchMessage(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("User Matched.")
        msg_box.setWindowTitle("User Found")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
        self.stopScan()
        self.closeCam()


    def openRegisterWindow(self):
        self.registerWindow = registerWindow(self.main_window)
        self.registerWindow.show()
        self.close()


    def displayProfileInfo(self, label):
        print(f"User matched: {label}")
        self.stopScan()

        self.timer.stop()
        self.cam.release()  

        if self.profileWindow is None:
            self.profileWindow = profileWindow(label, self.db_cursor, self.main_window)
        self.profileWindow.show()
        self.close()


    def startScan(self):
        print(f"Scanning...")
        self.isScanning = True
        self.ui.scanBtn.setEnabled(False)
        self.ui.scanBtn.setText("Scanning...")
        self.timer.start(50)


    def stopScan(self):
        self.isScanning = False
        self.ui.scanBtn.setEnabled(True)
        self.ui.scanBtn.setText("Scan Face")