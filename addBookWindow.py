
from PySide2.QtWidgets import *
from addBookUi import Ui_addBook_Form

class addBookWindow(QMainWindow, Ui_addBook_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
