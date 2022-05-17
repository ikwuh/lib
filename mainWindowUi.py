# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(640, 414)
        self.tableWidget = QTableWidget(mainWindow)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(120, 20, 521, 301))
        self.pushButton = QPushButton(mainWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 101, 23))
        self.pushButton_2 = QPushButton(mainWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 60, 101, 23))
        self.pushButton_3 = QPushButton(mainWindow)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 100, 101, 23))
        self.pushButton_4 = QPushButton(mainWindow)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(450, 340, 75, 23))
        self.pushButton_5 = QPushButton(mainWindow)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(560, 340, 75, 23))
        self.pushButton_6 = QPushButton(mainWindow)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 340, 75, 23))
        self.pushButton_7 = QPushButton(mainWindow)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 140, 101, 23))
        self.pushButton_9 = QPushButton(mainWindow)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 180, 101, 23))

        self.lineEdit = QLineEdit(mainWindow)
        self.lineEdit.setObjectName(u"pushButton")
        self.lineEdit.setGeometry(QRect(10, 240, 101, 23))
        self.pushButton_8 = QPushButton(mainWindow)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 270, 101, 23))
        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"books", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"authors", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"users", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"add", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainWindow", u"delete", None))
        self.pushButton_6.setText(QCoreApplication.translate("mainWindow", u"edit", None))
        self.pushButton_7.setText(QCoreApplication.translate("mainWindow", u"users/books", None))

        self.pushButton_8.setText(QCoreApplication.translate("mainWindow", u"search", None))

        self.pushButton_9.setText(QCoreApplication.translate("mainWindow", u"genres", None))
    # retranslateUi

