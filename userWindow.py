
from PySide2.QtWidgets import *
from userUi import Ui_User_Form

class UserWindow(QMainWindow, Ui_User_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

