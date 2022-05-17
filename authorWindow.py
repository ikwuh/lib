
from PySide2.QtWidgets import *
from authorUi import Ui_Author_Form

class AuthorWindow(QMainWindow, Ui_Author_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
