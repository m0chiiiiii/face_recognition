# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileInfoWindowouwOBU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1600, 900)
        Form.setStyleSheet(u"*{\n"
"background-color: #dcdcdc;\n"
"font-family: Poppins;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QPushButton#backBtn{\n"
"background-color: #1b4440;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight: 700;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#backBtn:hover{\n"
"background-color: #5f6d67;\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 1561, 861))
        self.widget.setStyleSheet(u"background-color: #efefef;")
        self.fnameDisplayLabel = QLabel(self.widget)
        self.fnameDisplayLabel.setObjectName(u"fnameDisplayLabel")
        self.fnameDisplayLabel.setGeometry(QRect(450, 140, 191, 31))
        self.fnameDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.fnameDisplay = QLineEdit(self.widget)
        self.fnameDisplay.setObjectName(u"fnameDisplay")
        self.fnameDisplay.setGeometry(QRect(450, 170, 250, 40))
        self.fnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.fnameDisplay.setReadOnly(True)
        self.mnameDisplay = QLineEdit(self.widget)
        self.mnameDisplay.setObjectName(u"mnameDisplay")
        self.mnameDisplay.setGeometry(QRect(740, 170, 250, 40))
        self.mnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.mnameDisplay.setReadOnly(True)
        self.mnameDisplayLabel = QLabel(self.widget)
        self.mnameDisplayLabel.setObjectName(u"mnameDisplayLabel")
        self.mnameDisplayLabel.setGeometry(QRect(740, 140, 191, 31))
        self.mnameDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.lnameDisplayLabel = QLabel(self.widget)
        self.lnameDisplayLabel.setObjectName(u"lnameDisplayLabel")
        self.lnameDisplayLabel.setGeometry(QRect(1030, 140, 191, 31))
        self.lnameDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.lnameDisplay = QLineEdit(self.widget)
        self.lnameDisplay.setObjectName(u"lnameDisplay")
        self.lnameDisplay.setGeometry(QRect(1030, 170, 250, 40))
        self.lnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.lnameDisplay.setReadOnly(True)
        self.suffixDisplay = QLineEdit(self.widget)
        self.suffixDisplay.setObjectName(u"suffixDisplay")
        self.suffixDisplay.setGeometry(QRect(1320, 170, 81, 40))
        self.suffixDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.suffixDisplay.setReadOnly(True)
        self.suffixDisplayLabel = QLabel(self.widget)
        self.suffixDisplayLabel.setObjectName(u"suffixDisplayLabel")
        self.suffixDisplayLabel.setGeometry(QRect(1320, 140, 81, 31))
        self.suffixDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.sexDisplayLabel = QLabel(self.widget)
        self.sexDisplayLabel.setObjectName(u"sexDisplayLabel")
        self.sexDisplayLabel.setGeometry(QRect(1440, 140, 81, 31))
        self.sexDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.sexDisplay = QLineEdit(self.widget)
        self.sexDisplay.setObjectName(u"sexDisplay")
        self.sexDisplay.setGeometry(QRect(1440, 170, 81, 40))
        self.sexDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.sexDisplay.setReadOnly(True)
        self.dobDisplay = QLineEdit(self.widget)
        self.dobDisplay.setObjectName(u"dobDisplay")
        self.dobDisplay.setGeometry(QRect(450, 270, 150, 40))
        self.dobDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.dobDisplay.setReadOnly(True)
        self.dobDisplayLabel = QLabel(self.widget)
        self.dobDisplayLabel.setObjectName(u"dobDisplayLabel")
        self.dobDisplayLabel.setGeometry(QRect(450, 240, 151, 31))
        self.dobDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.ageDisplayLabel = QLabel(self.widget)
        self.ageDisplayLabel.setObjectName(u"ageDisplayLabel")
        self.ageDisplayLabel.setGeometry(QRect(620, 240, 81, 31))
        self.ageDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.ageDisplay = QLineEdit(self.widget)
        self.ageDisplay.setObjectName(u"ageDisplay")
        self.ageDisplay.setGeometry(QRect(620, 270, 81, 40))
        self.ageDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.ageDisplay.setReadOnly(True)
        self.birthplaceDisplayLabel = QLabel(self.widget)
        self.birthplaceDisplayLabel.setObjectName(u"birthplaceDisplayLabel")
        self.birthplaceDisplayLabel.setGeometry(QRect(730, 240, 91, 31))
        self.birthplaceDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.birthplaceDisplay = QLineEdit(self.widget)
        self.birthplaceDisplay.setObjectName(u"birthplaceDisplay")
        self.birthplaceDisplay.setGeometry(QRect(730, 270, 391, 40))
        self.birthplaceDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.birthplaceDisplay.setReadOnly(True)
        self.educattDisplayLabel = QLabel(self.widget)
        self.educattDisplayLabel.setObjectName(u"educattDisplayLabel")
        self.educattDisplayLabel.setGeometry(QRect(1140, 240, 171, 31))
        self.educattDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.birthplaceDisplay_2 = QLineEdit(self.widget)
        self.birthplaceDisplay_2.setObjectName(u"birthplaceDisplay_2")
        self.birthplaceDisplay_2.setGeometry(QRect(1140, 270, 191, 40))
        self.birthplaceDisplay_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.birthplaceDisplay_2.setReadOnly(True)
        self.mstatusDisplay = QLineEdit(self.widget)
        self.mstatusDisplay.setObjectName(u"mstatusDisplay")
        self.mstatusDisplay.setGeometry(QRect(1350, 270, 171, 40))
        self.mstatusDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.mstatusDisplay.setReadOnly(True)
        self.mstatusDisplayLabel = QLabel(self.widget)
        self.mstatusDisplayLabel.setObjectName(u"mstatusDisplayLabel")
        self.mstatusDisplayLabel.setGeometry(QRect(1350, 240, 171, 31))
        self.mstatusDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.nationalityDisplay = QLineEdit(self.widget)
        self.nationalityDisplay.setObjectName(u"nationalityDisplay")
        self.nationalityDisplay.setGeometry(QRect(450, 370, 250, 40))
        self.nationalityDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.nationalityDisplay.setReadOnly(True)
        self.citizenshipDisplayLabel = QLabel(self.widget)
        self.citizenshipDisplayLabel.setObjectName(u"citizenshipDisplayLabel")
        self.citizenshipDisplayLabel.setGeometry(QRect(740, 340, 171, 31))
        self.citizenshipDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.citizenshipDisplay = QLineEdit(self.widget)
        self.citizenshipDisplay.setObjectName(u"citizenshipDisplay")
        self.citizenshipDisplay.setGeometry(QRect(740, 370, 250, 40))
        self.citizenshipDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.citizenshipDisplay.setReadOnly(True)
        self.nationalityDisplayLabel = QLabel(self.widget)
        self.nationalityDisplayLabel.setObjectName(u"nationalityDisplayLabel")
        self.nationalityDisplayLabel.setGeometry(QRect(450, 340, 171, 31))
        self.nationalityDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.religionDisplay = QLineEdit(self.widget)
        self.religionDisplay.setObjectName(u"religionDisplay")
        self.religionDisplay.setGeometry(QRect(1030, 370, 250, 40))
        self.religionDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.religionDisplay.setReadOnly(True)
        self.religionDisplayLabel = QLabel(self.widget)
        self.religionDisplayLabel.setObjectName(u"religionDisplayLabel")
        self.religionDisplayLabel.setGeometry(QRect(1030, 340, 171, 31))
        self.religionDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.heightDisplayLabel = QLabel(self.widget)
        self.heightDisplayLabel.setObjectName(u"heightDisplayLabel")
        self.heightDisplayLabel.setGeometry(QRect(1320, 340, 101, 31))
        self.heightDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.heightDisplay = QLineEdit(self.widget)
        self.heightDisplay.setObjectName(u"heightDisplay")
        self.heightDisplay.setGeometry(QRect(1320, 370, 80, 40))
        self.heightDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.heightDisplay.setReadOnly(True)
        self.weightDisplayLabel = QLabel(self.widget)
        self.weightDisplayLabel.setObjectName(u"weightDisplayLabel")
        self.weightDisplayLabel.setGeometry(QRect(1440, 340, 81, 31))
        self.weightDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.weightDisplay = QLineEdit(self.widget)
        self.weightDisplay.setObjectName(u"weightDisplay")
        self.weightDisplay.setGeometry(QRect(1440, 370, 80, 40))
        self.weightDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.weightDisplay.setReadOnly(True)
        self.streetDisplayLabel = QLabel(self.widget)
        self.streetDisplayLabel.setObjectName(u"streetDisplayLabel")
        self.streetDisplayLabel.setGeometry(QRect(450, 430, 171, 31))
        self.streetDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.streetDisplay = QLineEdit(self.widget)
        self.streetDisplay.setObjectName(u"streetDisplay")
        self.streetDisplay.setGeometry(QRect(450, 460, 281, 40))
        self.streetDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.streetDisplay.setReadOnly(True)
        self.brgyDisplayLabel = QLabel(self.widget)
        self.brgyDisplayLabel.setObjectName(u"brgyDisplayLabel")
        self.brgyDisplayLabel.setGeometry(QRect(750, 430, 171, 31))
        self.brgyDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.brgyDisplay = QLineEdit(self.widget)
        self.brgyDisplay.setObjectName(u"brgyDisplay")
        self.brgyDisplay.setGeometry(QRect(750, 460, 215, 40))
        self.brgyDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.brgyDisplay.setReadOnly(True)
        self.cityDisplayLabel = QLabel(self.widget)
        self.cityDisplayLabel.setObjectName(u"cityDisplayLabel")
        self.cityDisplayLabel.setGeometry(QRect(980, 430, 171, 31))
        self.cityDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.cityDisplay = QLineEdit(self.widget)
        self.cityDisplay.setObjectName(u"cityDisplay")
        self.cityDisplay.setGeometry(QRect(980, 460, 215, 40))
        self.cityDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.cityDisplay.setReadOnly(True)
        self.provinceDisplayLabel = QLabel(self.widget)
        self.provinceDisplayLabel.setObjectName(u"provinceDisplayLabel")
        self.provinceDisplayLabel.setGeometry(QRect(1210, 430, 171, 31))
        self.provinceDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.provinceDisplay = QLineEdit(self.widget)
        self.provinceDisplay.setObjectName(u"provinceDisplay")
        self.provinceDisplay.setGeometry(QRect(1210, 460, 215, 40))
        self.provinceDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.provinceDisplay.setReadOnly(True)
        self.zipcodeDisplayLabel = QLabel(self.widget)
        self.zipcodeDisplayLabel.setObjectName(u"zipcodeDisplayLabel")
        self.zipcodeDisplayLabel.setGeometry(QRect(1440, 430, 81, 31))
        self.zipcodeDisplayLabel.setStyleSheet(u"font-size: 14px;")
        self.zipcodeDisplay = QLineEdit(self.widget)
        self.zipcodeDisplay.setObjectName(u"zipcodeDisplay")
        self.zipcodeDisplay.setGeometry(QRect(1440, 460, 81, 40))
        self.zipcodeDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.zipcodeDisplay.setReadOnly(True)
        self.momInfoLabel = QLabel(self.widget)
        self.momInfoLabel.setObjectName(u"momInfoLabel")
        self.momInfoLabel.setGeometry(QRect(30, 520, 171, 31))
        self.momInfoLabel.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 500")
        self.maFnameDisplay = QLineEdit(self.widget)
        self.maFnameDisplay.setObjectName(u"maFnameDisplay")
        self.maFnameDisplay.setGeometry(QRect(60, 580, 201, 40))
        self.maFnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maFnameDisplay.setReadOnly(True)
        self.maFnameLbl = QLabel(self.widget)
        self.maFnameLbl.setObjectName(u"maFnameLbl")
        self.maFnameLbl.setGeometry(QRect(60, 550, 171, 31))
        self.maFnameLbl.setStyleSheet(u"font-size: 14px;")
        self.maMnameDisplay = QLineEdit(self.widget)
        self.maMnameDisplay.setObjectName(u"maMnameDisplay")
        self.maMnameDisplay.setGeometry(QRect(310, 580, 201, 40))
        self.maMnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maMnameDisplay.setReadOnly(True)
        self.maMnameLbl = QLabel(self.widget)
        self.maMnameLbl.setObjectName(u"maMnameLbl")
        self.maMnameLbl.setGeometry(QRect(310, 550, 171, 31))
        self.maMnameLbl.setStyleSheet(u"font-size: 14px;")
        self.maLnameDisplay = QLineEdit(self.widget)
        self.maLnameDisplay.setObjectName(u"maLnameDisplay")
        self.maLnameDisplay.setGeometry(QRect(560, 580, 201, 40))
        self.maLnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maLnameDisplay.setReadOnly(True)
        self.maLnameLbl = QLabel(self.widget)
        self.maLnameLbl.setObjectName(u"maLnameLbl")
        self.maLnameLbl.setGeometry(QRect(560, 550, 171, 31))
        self.maLnameLbl.setStyleSheet(u"font-size: 14px;")
        self.maDobDisplay = QLineEdit(self.widget)
        self.maDobDisplay.setObjectName(u"maDobDisplay")
        self.maDobDisplay.setGeometry(QRect(810, 580, 141, 40))
        self.maDobDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maDobDisplay.setReadOnly(True)
        self.maDobLbl = QLabel(self.widget)
        self.maDobLbl.setObjectName(u"maDobLbl")
        self.maDobLbl.setGeometry(QRect(810, 550, 121, 31))
        self.maDobLbl.setStyleSheet(u"font-size: 14px;")
        self.maAgeDisplay = QLineEdit(self.widget)
        self.maAgeDisplay.setObjectName(u"maAgeDisplay")
        self.maAgeDisplay.setGeometry(QRect(1000, 580, 61, 40))
        self.maAgeDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maAgeDisplay.setReadOnly(True)
        self.maAgeLbl = QLabel(self.widget)
        self.maAgeLbl.setObjectName(u"maAgeLbl")
        self.maAgeLbl.setGeometry(QRect(1000, 550, 61, 31))
        self.maAgeLbl.setStyleSheet(u"font-size: 14px;")
        self.maOccDisplay = QLineEdit(self.widget)
        self.maOccDisplay.setObjectName(u"maOccDisplay")
        self.maOccDisplay.setGeometry(QRect(1110, 580, 191, 40))
        self.maOccDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maOccDisplay.setReadOnly(True)
        self.maOccLbl = QLabel(self.widget)
        self.maOccLbl.setObjectName(u"maOccLbl")
        self.maOccLbl.setGeometry(QRect(1110, 550, 111, 31))
        self.maOccLbl.setStyleSheet(u"font-size: 14px;")
        self.maPnumLbl = QLabel(self.widget)
        self.maPnumLbl.setObjectName(u"maPnumLbl")
        self.maPnumLbl.setGeometry(QRect(1350, 550, 111, 31))
        self.maPnumLbl.setStyleSheet(u"font-size: 14px;")
        self.maPnumDisplay = QLineEdit(self.widget)
        self.maPnumDisplay.setObjectName(u"maPnumDisplay")
        self.maPnumDisplay.setGeometry(QRect(1350, 580, 171, 40))
        self.maPnumDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.maPnumDisplay.setReadOnly(True)
        self.paLnameDisplay = QLineEdit(self.widget)
        self.paLnameDisplay.setObjectName(u"paLnameDisplay")
        self.paLnameDisplay.setGeometry(QRect(560, 720, 201, 40))
        self.paLnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paLnameDisplay.setReadOnly(True)
        self.paDobLbl = QLabel(self.widget)
        self.paDobLbl.setObjectName(u"paDobLbl")
        self.paDobLbl.setGeometry(QRect(810, 690, 121, 31))
        self.paDobLbl.setStyleSheet(u"font-size: 14px;")
        self.paFnameDisplay = QLineEdit(self.widget)
        self.paFnameDisplay.setObjectName(u"paFnameDisplay")
        self.paFnameDisplay.setGeometry(QRect(60, 720, 201, 40))
        self.paFnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paFnameDisplay.setReadOnly(True)
        self.paFnameLbl = QLabel(self.widget)
        self.paFnameLbl.setObjectName(u"paFnameLbl")
        self.paFnameLbl.setGeometry(QRect(60, 690, 171, 31))
        self.paFnameLbl.setStyleSheet(u"font-size: 14px;")
        self.paLnameLbl = QLabel(self.widget)
        self.paLnameLbl.setObjectName(u"paLnameLbl")
        self.paLnameLbl.setGeometry(QRect(560, 690, 171, 31))
        self.paLnameLbl.setStyleSheet(u"font-size: 14px;")
        self.paOccLbl = QLabel(self.widget)
        self.paOccLbl.setObjectName(u"paOccLbl")
        self.paOccLbl.setGeometry(QRect(1110, 690, 111, 31))
        self.paOccLbl.setStyleSheet(u"font-size: 14px;")
        self.momInfoLabel_13 = QLabel(self.widget)
        self.momInfoLabel_13.setObjectName(u"momInfoLabel_13")
        self.momInfoLabel_13.setGeometry(QRect(30, 660, 171, 31))
        self.momInfoLabel_13.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 500")
        self.paPnumLbl = QLabel(self.widget)
        self.paPnumLbl.setObjectName(u"paPnumLbl")
        self.paPnumLbl.setGeometry(QRect(1350, 690, 111, 31))
        self.paPnumLbl.setStyleSheet(u"font-size: 14px;")
        self.paPnumDisplay = QLineEdit(self.widget)
        self.paPnumDisplay.setObjectName(u"paPnumDisplay")
        self.paPnumDisplay.setGeometry(QRect(1350, 720, 171, 40))
        self.paPnumDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paPnumDisplay.setReadOnly(True)
        self.paMnameLbl = QLabel(self.widget)
        self.paMnameLbl.setObjectName(u"paMnameLbl")
        self.paMnameLbl.setGeometry(QRect(310, 690, 171, 31))
        self.paMnameLbl.setStyleSheet(u"font-size: 14px;")
        self.paAgeDisplay = QLineEdit(self.widget)
        self.paAgeDisplay.setObjectName(u"paAgeDisplay")
        self.paAgeDisplay.setGeometry(QRect(1000, 720, 61, 40))
        self.paAgeDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paAgeDisplay.setReadOnly(True)
        self.paDobDisplay = QLineEdit(self.widget)
        self.paDobDisplay.setObjectName(u"paDobDisplay")
        self.paDobDisplay.setGeometry(QRect(810, 720, 141, 40))
        self.paDobDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paDobDisplay.setReadOnly(True)
        self.paMnameDisplay = QLineEdit(self.widget)
        self.paMnameDisplay.setObjectName(u"paMnameDisplay")
        self.paMnameDisplay.setGeometry(QRect(310, 720, 201, 40))
        self.paMnameDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paMnameDisplay.setReadOnly(True)
        self.paAgeLbl = QLabel(self.widget)
        self.paAgeLbl.setObjectName(u"paAgeLbl")
        self.paAgeLbl.setGeometry(QRect(1000, 690, 61, 31))
        self.paAgeLbl.setStyleSheet(u"font-size: 14px;")
        self.paOccDisplay = QLineEdit(self.widget)
        self.paOccDisplay.setObjectName(u"paOccDisplay")
        self.paOccDisplay.setGeometry(QRect(1110, 720, 191, 40))
        self.paOccDisplay.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.paOccDisplay.setReadOnly(True)
        self.profileDisplay = QLabel(self.widget)
        self.profileDisplay.setObjectName(u"profileDisplay")
        self.profileDisplay.setGeometry(QRect(100, 180, 250, 250))
        self.profileDisplay.setStyleSheet(u"background-color: #dcdcdc;")
        self.profileDisplay.setAlignment(Qt.AlignCenter)
        self.profileInfo = QLabel(self.widget)
        self.profileInfo.setObjectName(u"profileInfo")
        self.profileInfo.setGeometry(QRect(460, 40, 641, 71))
        self.profileInfo.setStyleSheet(u"font-size: 50px;\n"
"font-weight: bold;")
        self.profileInfo.setAlignment(Qt.AlignCenter)
        self.backBtn = QPushButton(self.widget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 30, 71, 23))
        self.backBtn.setStyleSheet(u"border: none;\n"
"background-color: transparent;\n"
"font-weight: 400;\n"
"color: black;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Face Card Profile", None))
        self.fnameDisplayLabel.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.fnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"First name", None))
        self.mnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Middle name", None))
        self.mnameDisplayLabel.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.lnameDisplayLabel.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.lnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Last name", None))
        self.suffixDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Suffix", None))
        self.suffixDisplayLabel.setText(QCoreApplication.translate("Form", u"Suffix", None))
        self.sexDisplayLabel.setText(QCoreApplication.translate("Form", u"Sex", None))
        self.sexDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Sex", None))
        self.dobDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.dobDisplayLabel.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.ageDisplayLabel.setText(QCoreApplication.translate("Form", u"Age", None))
        self.ageDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Age", None))
        self.birthplaceDisplayLabel.setText(QCoreApplication.translate("Form", u"Birth Place", None))
        self.birthplaceDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Birth Place", None))
        self.educattDisplayLabel.setText(QCoreApplication.translate("Form", u"Educational Attainment", None))
        self.birthplaceDisplay_2.setPlaceholderText(QCoreApplication.translate("Form", u"Educational Attainment", None))
        self.mstatusDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Marital Status", None))
        self.mstatusDisplayLabel.setText(QCoreApplication.translate("Form", u"Marital Status", None))
        self.nationalityDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Nationality", None))
        self.citizenshipDisplayLabel.setText(QCoreApplication.translate("Form", u"Citizenship", None))
        self.citizenshipDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Citizenship", None))
        self.nationalityDisplayLabel.setText(QCoreApplication.translate("Form", u"Nationality", None))
        self.religionDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Religion", None))
        self.religionDisplayLabel.setText(QCoreApplication.translate("Form", u"Religion", None))
        self.heightDisplayLabel.setText(QCoreApplication.translate("Form", u"Height", None))
        self.heightDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Height", None))
        self.weightDisplayLabel.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.weightDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Weight", None))
        self.streetDisplayLabel.setText(QCoreApplication.translate("Form", u"Street", None))
        self.streetDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Street", None))
        self.brgyDisplayLabel.setText(QCoreApplication.translate("Form", u"Barangay", None))
        self.brgyDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Barangay", None))
        self.cityDisplayLabel.setText(QCoreApplication.translate("Form", u"City", None))
        self.cityDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"City", None))
        self.provinceDisplayLabel.setText(QCoreApplication.translate("Form", u"Province", None))
        self.provinceDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Province", None))
        self.zipcodeDisplayLabel.setText(QCoreApplication.translate("Form", u"Zip Code", None))
        self.zipcodeDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Zip Code", None))
        self.momInfoLabel.setText(QCoreApplication.translate("Form", u"Mother's Information", None))
        self.maFnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.maFnameLbl.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.maMnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.maMnameLbl.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.maLnameDisplay.setText("")
        self.maLnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.maLnameLbl.setText(QCoreApplication.translate("Form", u"LastName", None))
        self.maDobDisplay.setText("")
        self.maDobDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"DOB", None))
        self.maDobLbl.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.maAgeDisplay.setText("")
        self.maAgeDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Age", None))
        self.maAgeLbl.setText(QCoreApplication.translate("Form", u"Age", None))
        self.maOccDisplay.setText("")
        self.maOccDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Occupation", None))
        self.maOccLbl.setText(QCoreApplication.translate("Form", u"Occupation", None))
        self.maPnumLbl.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.maPnumDisplay.setText("")
        self.maPnumDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.paLnameDisplay.setText("")
        self.paLnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.paDobLbl.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.paFnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.paFnameLbl.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.paLnameLbl.setText(QCoreApplication.translate("Form", u"LastName", None))
        self.paOccLbl.setText(QCoreApplication.translate("Form", u"Occupation", None))
        self.momInfoLabel_13.setText(QCoreApplication.translate("Form", u"Father's Information", None))
        self.paPnumLbl.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.paPnumDisplay.setText("")
        self.paPnumDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.paMnameLbl.setText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.paAgeDisplay.setText("")
        self.paAgeDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Age", None))
        self.paDobDisplay.setText("")
        self.paDobDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"DOB", None))
        self.paMnameDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Middle Name", None))
        self.paAgeLbl.setText(QCoreApplication.translate("Form", u"Age", None))
        self.paOccDisplay.setText("")
        self.paOccDisplay.setPlaceholderText(QCoreApplication.translate("Form", u"Street", None))
        self.profileDisplay.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.profileInfo.setText(QCoreApplication.translate("Form", u"Personal Information", None))
        self.backBtn.setText(QCoreApplication.translate("Form", u"\u2190 Back", None))
    # retranslateUi


class profileWindow(QWidget):
    def __init__(self, user_id, db_cursor, main_window):
        super().__init__()

        self.main_window = main_window
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user_id = user_id
        self.db_cursor = db_cursor

        self.loadUserData()

        self.ui.backBtn.clicked.connect(self.backToMain)


    def backToMain(self):
        self.main_window.show()
        self.close()


    def loadUserData(self):
        cursor = self.db_cursor
        query = """SELECT U_FNAME, U_MNAME, U_LNAME, U_SUFFIX, U_SEX, U_DOB, U_AGE, U_BOP, U_EDUC_ATT, 
                          U_MARITAL_ST, U_RELIGION, U_CITIZENSHIP, U_NATIONALITY, U_WEIGHT, 
                          U_HEIGHT, U_STREET, U_BRGY, U_CITY, U_PROVINCE, U_ZIPCODE, 
                          U_MI_FNAME, U_MI_MNAME, U_MI_LNAME, U_MI_DOB, U_MI_AGE, U_MI_OCCUPATION, U_MI_PNUM, 
                          U_FI_FNAME, U_FI_MNAME, U_FI_LNAME, U_FI_DOB, U_FI_AGE, U_FI_OCCUPATION, U_FI_PNUM,
                          U_PHOTO_PATH
                   FROM USERS WHERE U_ID = %s"""
        cursor.execute(query, (self.user_id,))
        user_data = cursor.fetchone()

        if user_data:
            self.ui.fnameDisplay.setText(user_data[0]) 
            self.ui.mnameDisplay.setText(user_data[1])
            self.ui.lnameDisplay.setText(user_data[2])
            self.ui.suffixDisplay.setText(user_data[3])
            self.ui.sexDisplay.setText(user_data[4])
            self.ui.dobDisplay.setText(str(user_data[5]))  
            self.ui.ageDisplay.setText(str(user_data[6]))
            self.ui.birthplaceDisplay.setText(user_data[7])
            self.ui.birthplaceDisplay_2.setText(user_data[8])
            self.ui.mstatusDisplay.setText(user_data[9])
            self.ui.religionDisplay.setText(user_data[10])
            self.ui.nationalityDisplay.setText(user_data[11])
            self.ui.citizenshipDisplay.setText(user_data[12])
            self.ui.heightDisplay.setText(str(user_data[13]))  
            self.ui.weightDisplay.setText(str(user_data[14])) 
            self.ui.streetDisplay.setText(user_data[15])
            self.ui.brgyDisplay.setText(user_data[16])
            self.ui.cityDisplay.setText(user_data[17])
            self.ui.provinceDisplay.setText(user_data[18])
            self.ui.zipcodeDisplay.setText(user_data[19])

            self.ui.maFnameDisplay.setText(user_data[20])
            self.ui.maMnameDisplay.setText(user_data[21])
            self.ui.maLnameDisplay.setText(user_data[22])
            self.ui.maDobDisplay.setText(str(user_data[23])) 
            self.ui.maAgeDisplay.setText(str(user_data[24]))
            self.ui.maOccDisplay.setText(user_data[25])
            self.ui.maPnumDisplay.setText(str(user_data[26])) 

            self.ui.paFnameDisplay.setText(user_data[27])
            self.ui.paMnameDisplay.setText(user_data[28])
            self.ui.paLnameDisplay.setText(user_data[29])
            self.ui.paDobDisplay.setText(str(user_data[30]))  
            self.ui.paAgeDisplay.setText(str(user_data[31]))
            self.ui.paOccDisplay.setText(user_data[32])
            self.ui.paPnumDisplay.setText(str(user_data[33]))  

            if user_data[34]: 
                pixmap = QPixmap(user_data[34])
                self.ui.profileDisplay.setPixmap(pixmap.scaled(self.ui.profileDisplay.size(), Qt.KeepAspectRatio))
        else:
            print("No user found with the given ID")
