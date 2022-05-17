# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'author.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Author_Form(object):
    def setupUi(self, Author_Form):
        if not Author_Form.objectName():
            Author_Form.setObjectName(u"Author_Form")
        Author_Form.resize(261, 162)
        self.pushButton = QPushButton(Author_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 120, 91, 27))
        self.pushButton_2 = QPushButton(Author_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 120, 91, 27))
        self.lineEdit = QLineEdit(Author_Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 221, 25))
        self.dateEdit = QDateEdit(Author_Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 70, 221, 25))
        self.retranslateUi(Author_Form)

        QMetaObject.connectSlotsByName(Author_Form)
    # setupUi

    def retranslateUi(self, Author_Form):
        Author_Form.setWindowTitle(QCoreApplication.translate("Author_Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Author_Form", u"back", None))
        self.pushButton_2.setText(QCoreApplication.translate("Author_Form", u"add", None))
    # retranslateUi

