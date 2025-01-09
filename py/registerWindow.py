# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerWindowGWIBvW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from dotenv import load_dotenv
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image

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
        Form.setStyleSheet(u"*{\n"
"	background-color: #efefef;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"\n"
"QPushButton#regConfirmBtn{\n"
"	background-color: #525252;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	font-weight: 650;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton#regConfirmBtn:hover{\n"
"	background-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.registrationLabel = QLabel(Form)
        self.registrationLabel.setObjectName(u"registrationLabel")
        self.registrationLabel.setGeometry(QRect(620, 20, 321, 71))
        self.registrationLabel.setStyleSheet(u"font-size: 40px;\n"
"font-weight: bold;\n"
"color: black;")
        self.registrationLabel.setAlignment(Qt.AlignCenter)
        self.regConfirmBtn = QPushButton(Form)
        self.regConfirmBtn.setObjectName(u"regConfirmBtn")
        self.regConfirmBtn.setGeometry(QRect(630, 830, 311, 45))
        self.regConfirmBtn.setStyleSheet(u"")
        self.paOccupationField = QLineEdit(Form)
        self.paOccupationField.setObjectName(u"paOccupationField")
        self.paOccupationField.setGeometry(QRect(1120, 760, 231, 45))
        self.paOccupationField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paMnameField = QLineEdit(Form)
        self.paMnameField.setObjectName(u"paMnameField")
        self.paMnameField.setGeometry(QRect(320, 760, 260, 45))
        self.paMnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paLnameField = QLineEdit(Form)
        self.paLnameField.setObjectName(u"paLnameField")
        self.paLnameField.setGeometry(QRect(600, 760, 271, 45))
        self.paLnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paLnameLabel = QLabel(Form)
        self.paLnameLabel.setObjectName(u"paLnameLabel")
        self.paLnameLabel.setGeometry(QRect(600, 730, 131, 31))
        self.paLnameLabel.setStyleSheet(u"font-size: 16px;")
        self.paPhonenumField = QLineEdit(Form)
        self.paPhonenumField.setObjectName(u"paPhonenumField")
        self.paPhonenumField.setGeometry(QRect(1370, 760, 191, 45))
        self.paPhonenumField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paAgeField = QLineEdit(Form)
        self.paAgeField.setObjectName(u"paAgeField")
        self.paAgeField.setGeometry(QRect(1030, 760, 71, 45))
        self.paAgeField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paDobField = QDateEdit(Form)
        self.paDobField.setObjectName(u"paDobField")
        self.paDobField.setGeometry(QRect(890, 760, 121, 45))
        self.paDobField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.paDobField.setCalendarPopup(True)
        self.paAgeLabel = QLabel(Form)
        self.paAgeLabel.setObjectName(u"paAgeLabel")
        self.paAgeLabel.setGeometry(QRect(1030, 730, 81, 31))
        self.paAgeLabel.setStyleSheet(u"font-size: 16px;")
        self.paDobLabel = QLabel(Form)
        self.paDobLabel.setObjectName(u"paDobLabel")
        self.paDobLabel.setGeometry(QRect(890, 730, 111, 31))
        self.paDobLabel.setStyleSheet(u"font-size: 16px;")
        self.paMnameLabel = QLabel(Form)
        self.paMnameLabel.setObjectName(u"paMnameLabel")
        self.paMnameLabel.setGeometry(QRect(320, 730, 131, 31))
        self.paMnameLabel.setStyleSheet(u"font-size: 16px;")
        self.paFnameLabel = QLabel(Form)
        self.paFnameLabel.setObjectName(u"paFnameLabel")
        self.paFnameLabel.setGeometry(QRect(40, 730, 131, 31))
        self.paFnameLabel.setStyleSheet(u"font-size: 16px;")
        self.paFnameField = QLineEdit(Form)
        self.paFnameField.setObjectName(u"paFnameField")
        self.paFnameField.setGeometry(QRect(40, 760, 260, 45))
        self.paFnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.paOccupationLabel = QLabel(Form)
        self.paOccupationLabel.setObjectName(u"paOccupationLabel")
        self.paOccupationLabel.setGeometry(QRect(1120, 730, 121, 31))
        self.paOccupationLabel.setStyleSheet(u"font-size: 16px;")
        self.momPhonenumLabel_2 = QLabel(Form)
        self.momPhonenumLabel_2.setObjectName(u"momPhonenumLabel_2")
        self.momPhonenumLabel_2.setGeometry(QRect(1370, 730, 121, 31))
        self.momPhonenumLabel_2.setStyleSheet(u"font-size: 16px;")
        self.momInfoLabel_2 = QLabel(Form)
        self.momInfoLabel_2.setObjectName(u"momInfoLabel_2")
        self.momInfoLabel_2.setGeometry(QRect(30, 700, 231, 31))
        self.momInfoLabel_2.setStyleSheet(u"font-size: 18px;\n"
"font-weight: 600;")
        self.momFnameField = QLineEdit(Form)
        self.momFnameField.setObjectName(u"momFnameField")
        self.momFnameField.setGeometry(QRect(40, 640, 260, 45))
        self.momFnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momInfoLabel = QLabel(Form)
        self.momInfoLabel.setObjectName(u"momInfoLabel")
        self.momInfoLabel.setGeometry(QRect(30, 580, 231, 31))
        self.momInfoLabel.setStyleSheet(u"font-size: 18px;\n"
"font-weight: 600;")
        self.momFnameLabel = QLabel(Form)
        self.momFnameLabel.setObjectName(u"momFnameLabel")
        self.momFnameLabel.setGeometry(QRect(40, 610, 131, 31))
        self.momFnameLabel.setStyleSheet(u"font-size: 16px;")
        self.momMnameField = QLineEdit(Form)
        self.momMnameField.setObjectName(u"momMnameField")
        self.momMnameField.setGeometry(QRect(320, 640, 260, 45))
        self.momMnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momMnameLabel = QLabel(Form)
        self.momMnameLabel.setObjectName(u"momMnameLabel")
        self.momMnameLabel.setGeometry(QRect(320, 610, 131, 31))
        self.momMnameLabel.setStyleSheet(u"font-size: 16px;")
        self.momLnameField = QLineEdit(Form)
        self.momLnameField.setObjectName(u"momLnameField")
        self.momLnameField.setGeometry(QRect(600, 640, 271, 45))
        self.momLnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momLnameLabel = QLabel(Form)
        self.momLnameLabel.setObjectName(u"momLnameLabel")
        self.momLnameLabel.setGeometry(QRect(600, 610, 131, 31))
        self.momLnameLabel.setStyleSheet(u"font-size: 16px;")
        self.momDobField = QDateEdit(Form)
        self.momDobField.setObjectName(u"momDobField")
        self.momDobField.setGeometry(QRect(890, 640, 121, 45))
        self.momDobField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.momDobField.setCalendarPopup(True)
        self.momDobLabel = QLabel(Form)
        self.momDobLabel.setObjectName(u"momDobLabel")
        self.momDobLabel.setGeometry(QRect(890, 610, 111, 31))
        self.momDobLabel.setStyleSheet(u"font-size: 16px;")
        self.momAgeField = QLineEdit(Form)
        self.momAgeField.setObjectName(u"momAgeField")
        self.momAgeField.setGeometry(QRect(1030, 640, 71, 45))
        self.momAgeField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momAgeLabel = QLabel(Form)
        self.momAgeLabel.setObjectName(u"momAgeLabel")
        self.momAgeLabel.setGeometry(QRect(1030, 610, 81, 31))
        self.momAgeLabel.setStyleSheet(u"font-size: 16px;")
        self.momOccupationField = QLineEdit(Form)
        self.momOccupationField.setObjectName(u"momOccupationField")
        self.momOccupationField.setGeometry(QRect(1120, 640, 231, 45))
        self.momOccupationField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momOccupationLabel = QLabel(Form)
        self.momOccupationLabel.setObjectName(u"momOccupationLabel")
        self.momOccupationLabel.setGeometry(QRect(1120, 610, 121, 31))
        self.momOccupationLabel.setStyleSheet(u"font-size: 16px;")
        self.momPhonenumField = QLineEdit(Form)
        self.momPhonenumField.setObjectName(u"momPhonenumField")
        self.momPhonenumField.setGeometry(QRect(1370, 640, 191, 45))
        self.momPhonenumField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.momPhonenumLabel = QLabel(Form)
        self.momPhonenumLabel.setObjectName(u"momPhonenumLabel")
        self.momPhonenumLabel.setGeometry(QRect(1370, 610, 121, 31))
        self.momPhonenumLabel.setStyleSheet(u"font-size: 16px;")
        self.suffixLabel = QLabel(Form)
        self.suffixLabel.setObjectName(u"suffixLabel")
        self.suffixLabel.setGeometry(QRect(1460, 110, 71, 31))
        self.suffixLabel.setStyleSheet(u"font-size: 16px;")
        self.lnameLabel = QLabel(Form)
        self.lnameLabel.setObjectName(u"lnameLabel")
        self.lnameLabel.setGeometry(QRect(1170, 110, 131, 31))
        self.lnameLabel.setStyleSheet(u"font-size: 16px;")
        self.fnameField = QLineEdit(Form)
        self.fnameField.setObjectName(u"fnameField")
        self.fnameField.setGeometry(QRect(610, 140, 260, 45))
        self.fnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.mnameLabel = QLabel(Form)
        self.mnameLabel.setObjectName(u"mnameLabel")
        self.mnameLabel.setGeometry(QRect(890, 110, 131, 31))
        self.mnameLabel.setStyleSheet(u"font-size: 16px;")
        self.suffixField = QLineEdit(Form)
        self.suffixField.setObjectName(u"suffixField")
        self.suffixField.setGeometry(QRect(1460, 140, 101, 45))
        self.suffixField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.fnameLabel = QLabel(Form)
        self.fnameLabel.setObjectName(u"fnameLabel")
        self.fnameLabel.setGeometry(QRect(610, 110, 131, 31))
        self.fnameLabel.setStyleSheet(u"font-size: 16px;")
        self.mnameField = QLineEdit(Form)
        self.mnameField.setObjectName(u"mnameField")
        self.mnameField.setGeometry(QRect(890, 140, 260, 45))
        self.mnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.lnameField = QLineEdit(Form)
        self.lnameField.setObjectName(u"lnameField")
        self.lnameField.setGeometry(QRect(1170, 140, 271, 45))
        self.lnameField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.sexField = QLineEdit(Form)
        self.sexField.setObjectName(u"sexField")
        self.sexField.setGeometry(QRect(730, 230, 61, 45))
        self.sexField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.sexLabel = QLabel(Form)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setGeometry(QRect(730, 200, 61, 31))
        self.sexLabel.setStyleSheet(u"font-size: 16px;")
        self.dobField = QDateEdit(Form)
        self.dobField.setObjectName(u"dobField")
        self.dobField.setGeometry(QRect(610, 230, 101, 45))
        self.dobField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.dobField.setCalendarPopup(True)
        self.dobLabel = QLabel(Form)
        self.dobLabel.setObjectName(u"dobLabel")
        self.dobLabel.setGeometry(QRect(610, 200, 111, 31))
        self.dobLabel.setStyleSheet(u"font-size: 16px;")
        self.ageField = QLineEdit(Form)
        self.ageField.setObjectName(u"ageField")
        self.ageField.setGeometry(QRect(810, 230, 81, 45))
        self.ageField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.ageLabel = QLabel(Form)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setGeometry(QRect(810, 200, 81, 31))
        self.ageLabel.setStyleSheet(u"font-size: 16px;")
        self.birthplaceField = QLineEdit(Form)
        self.birthplaceField.setObjectName(u"birthplaceField")
        self.birthplaceField.setGeometry(QRect(910, 230, 361, 45))
        self.birthplaceField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.birthplaceLabel = QLabel(Form)
        self.birthplaceLabel.setObjectName(u"birthplaceLabel")
        self.birthplaceLabel.setGeometry(QRect(910, 200, 131, 31))
        self.birthplaceLabel.setStyleSheet(u"font-size: 16px;")
        self.educattField = QComboBox(Form)
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.addItem("")
        self.educattField.setObjectName(u"educattField")
        self.educattField.setGeometry(QRect(1290, 230, 271, 45))
        self.educattField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px")
        self.educattLabel = QLabel(Form)
        self.educattLabel.setObjectName(u"educattLabel")
        self.educattLabel.setGeometry(QRect(1290, 200, 201, 31))
        self.educattLabel.setStyleSheet(u"font-size: 16px;")
        self.mstatusLabel = QLabel(Form)
        self.mstatusLabel.setObjectName(u"mstatusLabel")
        self.mstatusLabel.setGeometry(QRect(610, 290, 121, 31))
        self.mstatusLabel.setStyleSheet(u"font-size: 16px;")
        self.nationalityField = QLineEdit(Form)
        self.nationalityField.setObjectName(u"nationalityField")
        self.nationalityField.setGeometry(QRect(1340, 320, 221, 45))
        self.nationalityField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.nationalityLabel = QLabel(Form)
        self.nationalityLabel.setObjectName(u"nationalityLabel")
        self.nationalityLabel.setGeometry(QRect(1340, 290, 121, 31))
        self.nationalityLabel.setStyleSheet(u"font-size: 16px;")
        self.brgyField = QLineEdit(Form)
        self.brgyField.setObjectName(u"brgyField")
        self.brgyField.setGeometry(QRect(830, 410, 260, 45))
        self.brgyField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.brgyLabel = QLabel(Form)
        self.brgyLabel.setObjectName(u"brgyLabel")
        self.brgyLabel.setGeometry(QRect(830, 380, 91, 31))
        self.brgyLabel.setStyleSheet(u"font-size: 16px;")
        self.religionField = QLineEdit(Form)
        self.religionField.setObjectName(u"religionField")
        self.religionField.setGeometry(QRect(830, 320, 231, 45))
        self.religionField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.religionLabel = QLabel(Form)
        self.religionLabel.setObjectName(u"religionLabel")
        self.religionLabel.setGeometry(QRect(830, 290, 121, 31))
        self.religionLabel.setStyleSheet(u"font-size: 16px;")
        self.citizenshipLabel = QLabel(Form)
        self.citizenshipLabel.setObjectName(u"citizenshipLabel")
        self.citizenshipLabel.setGeometry(QRect(1080, 290, 121, 31))
        self.citizenshipLabel.setStyleSheet(u"font-size: 16px;")
        self.citizenshipField = QLineEdit(Form)
        self.citizenshipField.setObjectName(u"citizenshipField")
        self.citizenshipField.setGeometry(QRect(1080, 320, 241, 45))
        self.citizenshipField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.heightField = QLineEdit(Form)
        self.heightField.setObjectName(u"heightField")
        self.heightField.setGeometry(QRect(720, 410, 90, 45))
        self.heightField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.heightLabel = QLabel(Form)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setGeometry(QRect(720, 380, 91, 31))
        self.heightLabel.setStyleSheet(u"font-size: 16px;")
        self.weightField = QLineEdit(Form)
        self.weightField.setObjectName(u"weightField")
        self.weightField.setGeometry(QRect(610, 410, 90, 45))
        self.weightField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.weightLabel = QLabel(Form)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setGeometry(QRect(610, 380, 91, 31))
        self.weightLabel.setStyleSheet(u"font-size: 16px;")
        self.streetField = QLineEdit(Form)
        self.streetField.setObjectName(u"streetField")
        self.streetField.setGeometry(QRect(1110, 410, 451, 45))
        self.streetField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.streetLabel = QLabel(Form)
        self.streetLabel.setObjectName(u"streetLabel")
        self.streetLabel.setGeometry(QRect(1110, 380, 91, 31))
        self.streetLabel.setStyleSheet(u"font-size: 16px;")
        self.cityLabel_2 = QLabel(Form)
        self.cityLabel_2.setObjectName(u"cityLabel_2")
        self.cityLabel_2.setGeometry(QRect(870, 470, 91, 31))
        self.cityLabel_2.setStyleSheet(u"font-size: 16px;")
        self.cityField = QLineEdit(Form)
        self.cityField.setObjectName(u"cityField")
        self.cityField.setGeometry(QRect(610, 500, 241, 45))
        self.cityField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.cityLabel = QLabel(Form)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setGeometry(QRect(610, 470, 91, 31))
        self.cityLabel.setStyleSheet(u"font-size: 16px;")
        self.provinceField = QLineEdit(Form)
        self.provinceField.setObjectName(u"provinceField")
        self.provinceField.setGeometry(QRect(870, 500, 221, 45))
        self.provinceField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.zipcodeField = QLineEdit(Form)
        self.zipcodeField.setObjectName(u"zipcodeField")
        self.zipcodeField.setGeometry(QRect(1100, 500, 91, 45))
        self.zipcodeField.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;")
        self.cityLabel_3 = QLabel(Form)
        self.cityLabel_3.setObjectName(u"cityLabel_3")
        self.cityLabel_3.setGeometry(QRect(1100, 470, 81, 31))
        self.cityLabel_3.setStyleSheet(u"font-size: 16px;")
        self.mstatusCBox = QComboBox(Form)
        self.mstatusCBox.addItem("")
        self.mstatusCBox.addItem("")
        self.mstatusCBox.addItem("")
        self.mstatusCBox.addItem("")
        self.mstatusCBox.addItem("")
        self.mstatusCBox.setObjectName(u"mstatusCBox")
        self.mstatusCBox.setGeometry(QRect(610, 320, 201, 45))
        self.mstatusCBox.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px")
        self.regCameraFeed = QLabel(Form)
        self.regCameraFeed.setObjectName(u"regCameraFeed")
        self.regCameraFeed.setGeometry(QRect(20, 120, 561, 421))
        self.regCameraFeed.setStyleSheet(u"*{\n"
"color: white;\n"
"background-color: black;\n"
"}\n"
"")
        self.regCameraFeed.setAlignment(Qt.AlignCenter)
        self.regCaptureBtn = QPushButton(Form)
        self.regCaptureBtn.setObjectName(u"regCaptureBtn")
        self.regCaptureBtn.setGeometry(QRect(260, 500, 81, 31))
        self.regCaptureBtn.setStyleSheet(u"QPushButton#regCaptureBtn{\n"
"background-color: #525252;\n"
"color: white;\n"
"border-radius: 15px;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"}")
        self.regCaptureBtn.setAutoExclusive(False)
        self.camInstruction = QLabel(Form)
        self.camInstruction.setObjectName(u"camInstruction")
        self.camInstruction.setGeometry(QRect(20, 120, 561, 41))
        self.camInstruction.setStyleSheet(u"font-size: 13px;\n"
"color: white;\n"
"background-color: black;")
        self.camInstruction.setAlignment(Qt.AlignCenter)
        self.regToggleCamBtn = QPushButton(Form)
        self.regToggleCamBtn.setObjectName(u"regToggleCamBtn")
        self.regToggleCamBtn.setGeometry(QRect(90, 90, 61, 21))
        self.regToggleCamBtn.setStyleSheet(u"QPushButton#regToggleCamBtn{\n"
"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"}")
        self.regToggleCamBtn.setAutoExclusive(False)
        self.camInstruction_2 = QLabel(Form)
        self.camInstruction_2.setObjectName(u"camInstruction_2")
        self.camInstruction_2.setGeometry(QRect(20, 90, 71, 21))
        self.camInstruction_2.setStyleSheet(u"font-size: 14px;\n"
"color: black;")
        self.camInstruction_2.setAlignment(Qt.AlignCenter)
        self.backBtn = QPushButton(Form)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(14, 20, 71, 23))
        self.backBtn.setStyleSheet(u"border: none;\n"
"background-color: transparent;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Face Card | Register", None))
        Form.setWindowFilePath(QCoreApplication.translate("Form", u"++++*", None))
        self.registrationLabel.setText(QCoreApplication.translate("Form", u"Registration", None))
        self.regConfirmBtn.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.paOccupationField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter occupation", None))
        self.paMnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter middle name", None))
        self.paLnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter last name", None))
        self.paLnameLabel.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.paPhonenumField.setText("")
        self.paPhonenumField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter phone number", None))
        self.paAgeField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter age", None))
        self.paAgeLabel.setText(QCoreApplication.translate("Form", u"Age", None))
        self.paDobLabel.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.paMnameLabel.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.paFnameLabel.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.paFnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter first name", None))
        self.paOccupationLabel.setText(QCoreApplication.translate("Form", u"Occupation", None))
        self.momPhonenumLabel_2.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.momInfoLabel_2.setText(QCoreApplication.translate("Form", u"Father's Information", None))
        self.momFnameField.setText("")
        self.momFnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter first name", None))
        self.momInfoLabel.setText(QCoreApplication.translate("Form", u"Mother's Information", None))
        self.momFnameLabel.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.momMnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter middle name", None))
        self.momMnameLabel.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.momLnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter last name", None))
        self.momLnameLabel.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.momDobLabel.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.momAgeField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter age", None))
        self.momAgeLabel.setText(QCoreApplication.translate("Form", u"Age", None))
        self.momOccupationField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter occupation", None))
        self.momOccupationLabel.setText(QCoreApplication.translate("Form", u"Occupation", None))
        self.momPhonenumField.setText("")
        self.momPhonenumField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter phone number", None))
        self.momPhonenumLabel.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.suffixLabel.setText(QCoreApplication.translate("Form", u"Suffix", None))
        self.lnameLabel.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.fnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter first name", None))
        self.mnameLabel.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.suffixField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter suffix", None))
        self.fnameLabel.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.mnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter middle name", None))
        self.lnameField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter last name", None))
        self.sexField.setPlaceholderText(QCoreApplication.translate("Form", u"F or M", None))
        self.sexLabel.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.dobLabel.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.ageField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter age", None))
        self.ageLabel.setText(QCoreApplication.translate("Form", u"Age", None))
        self.birthplaceField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter birth place", None))
        self.birthplaceLabel.setText(QCoreApplication.translate("Form", u"Birth Place", None))
        self.educattField.setItemText(0, QCoreApplication.translate("Form", u"Early Childhood Graduate", None))
        self.educattField.setItemText(1, QCoreApplication.translate("Form", u"Some Elementary", None))
        self.educattField.setItemText(2, QCoreApplication.translate("Form", u"Elementary Graduate", None))
        self.educattField.setItemText(3, QCoreApplication.translate("Form", u"Some High School", None))
        self.educattField.setItemText(4, QCoreApplication.translate("Form", u"High School Graduate", None))
        self.educattField.setItemText(5, QCoreApplication.translate("Form", u"Some College", None))
        self.educattField.setItemText(6, QCoreApplication.translate("Form", u"Associate's Degree", None))
        self.educattField.setItemText(7, QCoreApplication.translate("Form", u"Bachelor's Degree", None))
        self.educattField.setItemText(8, QCoreApplication.translate("Form", u"Master's Degree", None))
        self.educattField.setItemText(9, QCoreApplication.translate("Form", u"Doctorate Degree", None))
        self.educattField.setItemText(10, QCoreApplication.translate("Form", u"Other", None))

        self.educattLabel.setText(QCoreApplication.translate("Form", u"Educational Attainment", None))
        self.mstatusLabel.setText(QCoreApplication.translate("Form", u"Marital Status", None))
        self.nationalityField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter nationality", None))
        self.nationalityLabel.setText(QCoreApplication.translate("Form", u"Nationality", None))
        self.brgyField.setText("")
        self.brgyField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter barangay name", None))
        self.brgyLabel.setText(QCoreApplication.translate("Form", u"Barangay", None))
        self.religionField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter religion", None))
        self.religionLabel.setText(QCoreApplication.translate("Form", u"Religion", None))
        self.citizenshipLabel.setText(QCoreApplication.translate("Form", u"Citizenship", None))
        self.citizenshipField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter citizenship", None))
        self.heightField.setPlaceholderText(QCoreApplication.translate("Form", u"ht. in cm.", None))
        self.heightLabel.setText(QCoreApplication.translate("Form", u"Height", None))
        self.weightField.setPlaceholderText(QCoreApplication.translate("Form", u"wt. in kl.", None))
        self.weightLabel.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.streetField.setText("")
        self.streetField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter street name", None))
        self.streetLabel.setText(QCoreApplication.translate("Form", u"Street", None))
        self.cityLabel_2.setText(QCoreApplication.translate("Form", u"Province", None))
        self.cityField.setText("")
        self.cityField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter city name", None))
        self.cityLabel.setText(QCoreApplication.translate("Form", u"City", None))
        self.provinceField.setText("")
        self.provinceField.setPlaceholderText(QCoreApplication.translate("Form", u"Enter province name", None))
        self.zipcodeField.setText("")
        self.zipcodeField.setPlaceholderText(QCoreApplication.translate("Form", u"Zip code", None))
        self.cityLabel_3.setText(QCoreApplication.translate("Form", u"Zip Code", None))
        self.mstatusCBox.setItemText(0, QCoreApplication.translate("Form", u"Single", None))
        self.mstatusCBox.setItemText(1, QCoreApplication.translate("Form", u"Maried", None))
        self.mstatusCBox.setItemText(2, QCoreApplication.translate("Form", u"Divorced", None))
        self.mstatusCBox.setItemText(3, QCoreApplication.translate("Form", u"WIdowed", None))
        self.mstatusCBox.setItemText(4, QCoreApplication.translate("Form", u"Separated", None))

        self.regCameraFeed.setText(QCoreApplication.translate("Form", u"Camera", None))
        self.regCaptureBtn.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.camInstruction.setText(QCoreApplication.translate("Form", u"Find better lighting to detect face", None))
        self.regToggleCamBtn.setText(QCoreApplication.translate("Form", u"Off", None))
        self.camInstruction_2.setText(QCoreApplication.translate("Form", u"Camera:", None))
        self.backBtn.setText(QCoreApplication.translate("Form", u"\u2190 Back", None))
    # retranslateUi



class registerWindow(QWidget):
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

        self.mtcnn = MTCNN(keep_all=True)
        self.embedder = InceptionResnetV1(pretrained='vggface2').eval()
        self.is_camera_on = False
        self.db_connection = None
        self.db_cursor = None

        self.connect_to_db()
        
        # to capture face in camera
        self.ui.regCaptureBtn.clicked.connect(self.capturePhoto)
        # for cam toggle on and off
        self.ui.regToggleCamBtn.clicked.connect(self.toggleCam)
        # for insertion of users
        self.ui.regConfirmBtn.clicked.connect(self.insertUser)
        # back button 
        self.ui.backBtn.clicked.connect(self.backToMain)


    def backToMain(self):
        self.main_window.show()
        self.close()


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


    def generateFaceEmbedding(self, img_path):
        try:
                img = Image.open(img_path)
                face = self.mtcnn(img)
                if face is None:
                        QMessageBox.warning(self, "Face Embedding Failed", "No face detected in the image.")
                        return None
                
                # Convert face to float and move to CPU if it's on GPU
                face = face.float().to('cpu')
                
                # Ensure face tensor has the correct shape
                if face.dim() == 3:
                        face = face.unsqueeze(0)
                
                with torch.no_grad():
                        embedding = self.embedder(face)
                
                return embedding.numpy().flatten()
        
        except Exception as e:
                error_msg = f"Error generating face embedding: {str(e)}"
                print(error_msg)  # For console debugging
                print.error(error_msg, exc_info=True)  # Log the full stack trace
                QMessageBox.critical(self, "Face Embedding Failed", error_msg)
                return None
        

    def insertUser(self):
        if not hasattr(self, 'photo_path') or not self.photo_path:
            print(f"No photo captured. Failed to confirm registration.")
            QMessageBox.warning(self, "Registration Failed", "No face has been captured. Please capture before confirming.")
            return
        
        required_fields = [self.ui.fnameField.text(), self.ui.lnameField.text(), self.ui.dobField.date(), self.ui.sexField.text(), self.ui.ageField.text(),
                           self.ui.birthplaceField.text(), self.ui.educattField.currentText(), self.ui.mstatusCBox.currentText(), self.ui.religionField.text(),
                           self.ui.citizenshipField.text(), self.ui.nationalityField.text(), self.ui.weightField.text(), self.ui.heightField.text(), self.ui.streetField.text(),
                           self.ui.brgyField.text(), self.ui.cityField.text(), self.ui.provinceField.text(), self.ui.zipcodeField.text()]
        
        if not all(required_fields):
            QMessageBox.warning(self, "Registration Failed", "Please input required fields.")
            return


        u_fname = self.ui.fnameField.text()
        u_mname = self.ui.mnameField.text()
        u_lname = self.ui.lnameField.text()
        u_suffix = self.ui.suffixField.text()
        u_dob = self.ui.dobField.date().toString("yyyy-MM-dd")
        u_sex = self.ui.sexField.text()
        u_age = self.ui.ageField.text()
        u_bop = self.ui.birthplaceField.text()
        u_educ_att = self.ui.educattField.currentText()
        u_marital_st = self.ui.mstatusCBox.currentText()
        u_religion = self.ui.religionField.text()
        u_citizenship = self.ui.citizenshipField.text()
        u_nationality = self.ui.nationalityField.text()
        u_weight = self.ui.weightField.text()
        u_height = self.ui.heightField.text()
        u_street = self.ui.streetField.text()
        u_brgy = self.ui.brgyField.text()
        u_city = self.ui.cityField.text()
        u_province = self.ui.provinceField.text()
        u_zipcode = self.ui.zipcodeField.text()

        # Collect mother info
        mom_fname = self.ui.momFnameField.text()
        mom_mname = self.ui.momMnameField.text()
        mom_lname = self.ui.momLnameField.text()
        mom_dob = self.ui.momDobField.date().toString("yyyy-MM-dd")
        mom_age = self.ui.momAgeField.text()
        mom_occupation = self.ui.momOccupationField.text()
        mom_phone = self.ui.momPhonenumField.text()

        # Collect father info
        pa_fname = self.ui.paFnameField.text()
        pa_mname = self.ui.paMnameField.text()
        pa_lname = self.ui.paLnameField.text()
        pa_dob = self.ui.paDobField.date().toString("yyyy-MM-dd")
        pa_age = self.ui.paAgeField.text()
        pa_occupation = self.ui.paOccupationField.text()
        pa_phone = self.ui.paPhonenumField.text()


        try:
            
            face_embeddings = None  # Initialize face_embeddings
            face_embeddings = self.generateFaceEmbedding(self.photo_path)
        
            if face_embeddings is None:
              QMessageBox.warning(self, "Registration Failed", "Failed to generate face embeddings.")
              return
        
            face_embeddings_array = np.array(face_embeddings, dtype=np.float64)
            face_embeddings_list = face_embeddings_array.tolist()
            
        #     if isinstance(face_embeddings_list, list):
        #         face_embeddings_bytes = np.array(face_embeddings_list, dtype=np.float32).tobytes()
        #     else:
        #         raise ValueError("face_embeddings_list must be a list of floats.")

            #data insertion
            cursor = self.db_cursor
            cursor.execute("""
                INSERT INTO USERS (U_FNAME, U_MNAME, U_LNAME, U_SUFFIX, U_DOB, U_SEX, U_AGE, U_BOP, U_EDUC_ATT, 
                                U_MARITAL_ST, U_RELIGION, U_CITIZENSHIP, U_NATIONALITY, U_WEIGHT, U_HEIGHT, 
                                U_STREET, U_BRGY, U_CITY, U_PROVINCE, U_ZIPCODE, U_MI_FNAME, U_MI_MNAME, U_MI_LNAME,
                                U_MI_DOB, U_MI_AGE, U_MI_OCCUPATION, U_MI_PNUM, U_FI_FNAME, U_FI_MNAME, U_FI_LNAME,
                                U_FI_DOB, U_FI_AGE, U_FI_OCCUPATION, U_FI_PNUM,  U_FACE_EMBEDDINGS, U_PHOTO_PATH)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (u_fname, u_mname, u_lname, u_suffix, u_dob, u_sex, u_age, u_bop, u_educ_att, u_marital_st, 
                u_religion, u_citizenship, u_nationality, u_weight, u_height, u_street, u_brgy, u_city, 
                u_province, u_zipcode, mom_fname, mom_mname, mom_lname, mom_dob, mom_age, mom_occupation,
                mom_phone, pa_fname, pa_mname, pa_lname, pa_dob, pa_age, pa_occupation, pa_phone, face_embeddings_list,
                self.photo_path))

            self.db_connection.commit() 

            cursor.execute("SELECT lastval()")
            user_id = cursor.fetchone()[0]
            
            QMessageBox(self, "Face Card", "Added Successfully")
            print(f"Inserted Successfully")

            self.main_window.show()
            self.close()


        except Exception as e:
            print(f"Error during registration: {e}")
        #     if self.db_cursor:
        #         self.db_cursor.close()
        #     if self.db_connection:
        #         self.db_connection.close()



    def setupCamera(self):
        #initialize opencv camera
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cam.isOpened():
            print('Error: Could not open camera')
            return
        
        #start of camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateCam)
        self.timer.start(20)

        self.is_camera_on = True


    def closeCam(self):
        if self.is_camera_on:
            self.timer.stop()
            self.cam.release()
            self.ui.regCameraFeed.clear()
            self.ui.regToggleCamBtn.setText("Off")
            self.is_camera_on = False


    def toggleCam(self):
        if self.is_camera_on:
            self.closeCam()
            self.ui.regToggleCamBtn.setText("Off")
        else:
            self.setupCamera()
            self.ui.regToggleCamBtn.setText("On")


    def updateCam(self):
        ret, frame = self.cam.read()
        if ret:
            frame = cv2.flip(frame, 1)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb_frame)
            
            boxes, _ = self.mtcnn.detect(pil_img)

            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            ht, wd, channel = rgb_frame.shape
            bytes_per_line = 3 * wd
            q_img = QImage(rgb_frame.data, wd, ht, bytes_per_line, QImage.Format_RGB888)

            #QImage to QPixmap
            pixmap = QPixmap.fromImage(q_img)
            self.ui.regCameraFeed.setPixmap(pixmap.scaled(self.ui.regCameraFeed.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def captureFace(self):
        ret, frame = self.cam.read()
        if ret:
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb_frame)

            boxes, _ = self.mtcnn.detect(pil_img)

            if boxes is not None and len(boxes) > 0:
                x1, y1, x2, y2 = map(int, boxes[0])  
                face = frame[y1:y2, x1:x2]  

                timestamp = QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
                img_filename = f"usersFace/captured_face_{timestamp}.jpg"
                cv2.imwrite(img_filename, face)
                print(f"Image saved as {img_filename}")

                # self.closeCam()
                return img_filename
            else:
                print("No face detected.")
                return None
        else:
             print("Failed to capture frame.")
             return None
        

    def capturePhoto(self):
        self.photo_path = self.captureFace()
        if self.photo_path:
            self.ui.camInstruction.setText("C A P T U R E D")
            print(f"Photo captured successfully!")
            self.closeCam()
        else:
            print(f"Photo captured failed!")


    def closeEvent(self, event):
        try:
            if hasattr(self, 'cam') and self.cam.isOpened():
                self.cam.release()
            if hasattr(self, 'db_connection') and self.db_connection:
                self.db_connection.close()
                # Any other cleanup needed
        except Exception as e:
            print.error(f"Error during cleanup: {str(e)}", exc_info=True)
        finally:
            event.accept()

    