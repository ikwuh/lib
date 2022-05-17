
from PySide2.QtWidgets import *
from genreUi import Ui_Genre_Form


class GenreWindow(QMainWindow, Ui_Genre_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
