# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowgePxyn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1600, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setStyleSheet(u"*{\n"
"	background-color: #efefef;\n"
"	font-family: Poppins;\n"
"}\n"
"")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginframe = QFrame(self.centralwidget)
        self.loginframe.setObjectName(u"loginframe")
        self.loginframe.setGeometry(QRect(530, 70, 551, 731))
        self.loginframe.setStyleSheet(u"*{\n"
"background-color: white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton#scanFaceBtn{\n"
"background-color: #292929;\n"
"color: white;\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#scanFaceBtn:hover, #registerBtn:hover{\n"
"background-color: #000000;\n"
"}\n"
"\n"
"QPushButton#registerBtn{\n"
"background-color: #525252;\n"
"color: white;\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"}")
        self.loginframe.setFrameShape(QFrame.StyledPanel)
        self.loginframe.setFrameShadow(QFrame.Raised)
        self.scanFaceBtn = QPushButton(self.loginframe)
        self.scanFaceBtn.setObjectName(u"scanFaceBtn")
        self.scanFaceBtn.setGeometry(QRect(80, 390, 391, 101))
        self.scanFaceBtn.setStyleSheet(u"")
        self.registerBtn = QPushButton(self.loginframe)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setGeometry(QRect(80, 580, 391, 91))
        self.registerBtn.setStyleSheet(u"")
        self.label_2 = QLabel(self.loginframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 540, 391, 31))
        self.label_2.setStyleSheet(u"font-size: 16px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.loginframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 451, 271))
        self.label.setPixmap(QPixmap(u":/icons/fc-logo.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Face Card", None))
        self.scanFaceBtn.setText(QCoreApplication.translate("mainWindow", u"Scan Face", None))
        self.registerBtn.setText(QCoreApplication.translate("mainWindow", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Haven't registered yet?", None))
        self.label.setText("")
    # retranslateUi

