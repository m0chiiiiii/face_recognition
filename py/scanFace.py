# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanFacelxXeCf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import cv2.data
import numpy as np
import resource

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 550)
        font = QFont()
        font.setFamily(u"Poppins")
        font.setStyleStrategy(QFont.PreferDefault)
        Form.setFont(font)
        Form.setStyleSheet(u"*{\n"
"background-color: #d3f4ec;\n"
"font-family: Poppins;\n"
"font-size: 14px;\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 680, 530))
        self.widget.setStyleSheet(u"*{\n"
"background-color: white;\n"
"}\n"
"\n"
"QPushButton#captureBtn{\n"
"background-color: #0c2729;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight: 600;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QPushButton#captureBtn:hover{\n"
"background-color: #5f6d67;\n"
"}")
        self.cameraFeed = QLabel(self.widget)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setGeometry(QRect(20, 20, 641, 461))
        self.cameraFeed.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.cameraFeed.setAlignment(Qt.AlignCenter)
        self.captureBtn = QPushButton(self.widget)
        self.captureBtn.setObjectName(u"captureBtn")
        self.captureBtn.setGeometry(QRect(230, 490, 221, 31))
        self.captureBtn.setStyleSheet(u"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

        self.captureBtn.clicked.connect(self.captureFace)

        #initialize setup
        self.setupCamera()

        #pre-trained classifier for face recognition
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cameraFeed.setText(QCoreApplication.translate("Form", u"Camera", None))
        self.captureBtn.setText(QCoreApplication.translate("Form", u"S C A N", None))
    # retranslateUi


    def setupCamera(self):
        #initialize opencv camera
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            print('Error: Could not open camera.')
            return
        
        #start of camera feed
        self.timer =QTimer()
        self.timer.timeout.connect(self.updateCam)
        self.timer.start(20)

    def updateCam(self):
        ret, frame = self.cam.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #detect face
            face = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            #rectangle to follow the users face
            for(w, x, y, z) in face:
                cv2.rectangle(frame, (w, x), (w + y, x + z), (255, 0, 0), 2)

            #frame convertion to rgb
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


            #frame to QImage
            ht, wd, channel = rgb_frame.shape
            bytes_per_line = 3 * wd
            q_image = QImage(rgb_frame.data, wd, ht, bytes_per_line, QImage.Format_RGB888)

            #QImage to QPixmap
            pixmap = QPixmap.fromImage(q_image)
            self.cameraFeed.setPixmap(pixmap.scaled(self.cameraFeed.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def captureFace(self):
        ret, frame = self.cam.read()
        if ret:
            #detect face
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(face) > 0:
                timestamp = QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
                img_filename = f"captured_face_{timestamp}.jpg"
                cv2.imwrite(img_filename, frame)
                print(f"Image saved as {img_filename}")
            else:
                print("No face detected.")


    def closeEvent(self, event):
        self.cam.release()
        event.accept()