# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_User_Form(object):
    def setupUi(self, User_Form):
        if not User_Form.objectName():
            User_Form.setObjectName(u"User_Form")
        User_Form.resize(261, 219)
        self.lineEdit = QLineEdit(User_Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 221, 25))
        self.dateEdit = QDateEdit(User_Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 70, 221, 25))
        self.lineEdit_3 = QLineEdit(User_Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 120, 221, 25))
        rx = QRegExp("[0-9]{7,10}")  # +++
        val = QRegExpValidator(rx)  # +++
        self.lineEdit_3.setValidator(val)
        self.lineEdit_3.setValidator(val)
        self.pushButton = QPushButton(User_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 170, 91, 27))
        self.pushButton_2 = QPushButton(User_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 170, 91, 27))

        self.retranslateUi(User_Form)

        QMetaObject.connectSlotsByName(User_Form)
    # setupUi

    def retranslateUi(self, User_Form):
        User_Form.setWindowTitle(QCoreApplication.translate("User_Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("User_Form", u"back", None))
        self.pushButton_2.setText(QCoreApplication.translate("User_Form", u"add", None))
    # retranslateUi

