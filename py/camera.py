# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanFaceDopGII.ui'
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
        Form.resize(700, 550)
        font = QFont()
        font.setFamily(u"Poppins")
        font.setStyleStrategy(QFont.PreferDefault)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #d3f4ec;\n"
"font-family: Poppins;\n"
"font-size: 14px;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 681, 531))
        self.widget.setStyleSheet(u"background-color: white;")
        self.cameraFeed = QLabel(self.widget)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setGeometry(QRect(20, 50, 641, 471))
        self.cameraFeed.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.cameraFeed.setAlignment(Qt.AlignCenter)
        self.backBtn = QPushButton(self.widget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(260, 10, 71, 31))
        self.backBtn.setStyleSheet(u"background-color: #0c2729;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight: 500;\n"
"font-size: 12px;")
        self.captureBtn = QPushButton(self.widget)
        self.captureBtn.setObjectName(u"captureBtn")
        self.captureBtn.setGeometry(QRect(350, 10, 71, 31))
        self.captureBtn.setStyleSheet(u"background-color: #0c2729;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight: 500;\n"
"font-size: 12px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cameraFeed.setText(QCoreApplication.translate("Form", u"Camera", None))
        self.backBtn.setText(QCoreApplication.translate("Form", u"Back", None))
        self.captureBtn.setText(QCoreApplication.translate("Form", u"Capture", None))
    # retranslateUi

