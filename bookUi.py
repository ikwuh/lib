# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Book_Form(object):
    def setupUi(self, Book_Form):
        if not Book_Form.objectName():
            Book_Form.setObjectName(u"Book_Form")
        Book_Form.resize(261, 219)
        self.comboBox_2 = QComboBox(Book_Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 70, 221, 25))
        self.pushButton = QPushButton(Book_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 170, 91, 27))
        self.lineEdit = QLineEdit(Book_Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 221, 25))
        self.pushButton_2 = QPushButton(Book_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 170, 91, 27))
        self.comboBox = QComboBox(Book_Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 120, 221, 25))

        self.retranslateUi(Book_Form)

        QMetaObject.connectSlotsByName(Book_Form)
    # setupUi

    def retranslateUi(self, Book_Form):
        Book_Form.setWindowTitle(QCoreApplication.translate("Book_Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Book_Form", u"back", None))
        self.pushButton_2.setText(QCoreApplication.translate("Book_Form", u"add", None))
    # retranslateUi

