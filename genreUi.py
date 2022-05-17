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


class Ui_Genre_Form(object):
    def setupUi(self, Genre_Form):
        if not Genre_Form.objectName():
            Genre_Form.setObjectName(u"Author_Form")
        Genre_Form.resize(261, 162)
        self.pushButton = QPushButton(Genre_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 120, 91, 27))
        self.pushButton_2 = QPushButton(Genre_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 120, 91, 27))
        self.lineEdit = QLineEdit(Genre_Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 221, 25))
        self.retranslateUi(Genre_Form)

        QMetaObject.connectSlotsByName(Genre_Form)
    # setupUi

    def retranslateUi(self, Genre_Form):
        Genre_Form.setWindowTitle(QCoreApplication.translate("Genre_Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Genre_Form", u"back", None))
        self.pushButton_2.setText(QCoreApplication.translate("Genre_Form", u"add", None))
    # retranslateUi

