
from PySide2.QtWidgets import *
from bookUi import Ui_Book_Form

class BookWindow(QMainWindow, Ui_Book_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
