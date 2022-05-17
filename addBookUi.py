# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addBook.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_addBook_Form(object):
    def setupUi(self, addBook_Form):
        if not addBook_Form.objectName():
            addBook_Form.setObjectName(u"addBook_Form")
        addBook_Form.resize(261, 162)
        self.pushButton = QPushButton(addBook_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 120, 91, 27))
        self.pushButton_2 = QPushButton(addBook_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 120, 91, 27))
        self.comboBox = QComboBox(addBook_Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 221, 25))
        self.comboBox_2 = QComboBox(addBook_Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 70, 221, 25))

        self.retranslateUi(addBook_Form)

        QMetaObject.connectSlotsByName(addBook_Form)
    # setupUi

    def retranslateUi(self, addBook_Form):
        addBook_Form.setWindowTitle(QCoreApplication.translate("addBook_Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("addBook_Form", u"back", None))
        self.pushButton_2.setText(QCoreApplication.translate("addBook_Form", u"add", None))
    # retranslateUi

