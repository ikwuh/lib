import sqlite3, os, sys, PySide2
from bookDB import BookDB
from authorDB import AuthorDB
from userDB import UserDB
from usersWithBooksDB import UsersWithBooksDB
from genreDB import GenreDB
from functools import partial
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from mainWindowUi import Ui_mainWindow
from bookWindow import BookWindow
from authorWindow import AuthorWindow
from userWindow import UserWindow
from addBookWindow import addBookWindow
from genreWindow import GenreWindow
class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.setupUi(self)

        self.source = "books"
        self.conn = sqlite3.connect('lib.db')
        self.c = self.conn.cursor()
        self.searchStr = None

        self.isSearched = False
        self.bookDB = BookDB(self.c, self.conn)
        self.authorDB = AuthorDB(self.c, self.conn)
        self.userDB = UserDB(self.c, self.conn)
        self.usersWithBooksDB = UsersWithBooksDB(self.c, self.conn)
        self.genreDB = GenreDB(self.c, self.conn)

        self.userDB.initDB()
        self.authorDB.initDB()
        self.genreDB.initDB()
        self.bookDB.initDB()
        self.usersWithBooksDB.initDB()




        self.statements = {"isBookSelected": False,
                           "isAuthorSelected": False,
                           "isUserSelected": False,
                           "isUserBooksSelected" : False,
                           "isGenreSelected" : False}

        self.bookForm = BookWindow()
        self.authorForm = AuthorWindow()
        self.userForm = UserWindow()
        self.addBookForm = addBookWindow()
        self.genreForm = GenreWindow()

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton.clicked.connect(partial(self.loadData, self.bookDB))
        self.pushButton_2.clicked.connect(partial(self.loadData, self.authorDB))
        self.pushButton_3.clicked.connect(partial(self.loadData, self.userDB))
        self.pushButton_7.clicked.connect(partial(self.loadData, self.usersWithBooksDB))
        self.pushButton_9.clicked.connect(partial(self.loadData, self.genreDB))
        self.pushButton_5.clicked.connect(self.removeRow)
        self.pushButton_4.clicked.connect(self.showWindow)
        self.pushButton_6.clicked.connect(self.showWindowEdit)
        self.pushButton_8.clicked.connect(self.searchRow)

        self.authors = {}
        self.users = {}
        self.books = {}
        self.genres = {}
        #self.userDB.c.execute('''DROP TABLE users''')
        #self.userDB.c.execute('''DROP TABLE authors''')
        #self.userDB.c.execute('''DROP TABLE books''')
        #self.userDB.c.execute('''DROP TABLE genres''')
        #self.userDB.c.execute('''DROP TABLE userWithBooks''')

        # retranslateUi



    def showWindow(self):
        self.bookForm = BookWindow()
        self.authorForm = AuthorWindow()
        self.userForm = UserWindow()
        self.addBookForm = addBookWindow()
        self.genreForm = GenreWindow()

        self.bookForm.pushButton_2.clicked.connect(self.addRow)
        self.authorForm.pushButton_2.clicked.connect(self.addRow)
        self.userForm.pushButton_2.clicked.connect(self.addRow)
        self.addBookForm.pushButton_2.clicked.connect(self.addRow)
        self.genreForm.pushButton_2.clicked.connect(self.addRow)
        if self.statements["isBookSelected"]:

            resAuthors = self.authorDB.getRecs()
            self.authors.clear()
            self.genres.clear()

            for row in resAuthors:
                self.authors[row[1]] = row[0]

            resGenres = self.genreDB.getRecs()

            print(resGenres)
            for row in resGenres:
                print(row)
                self.genres[row[1]] = row[0]

            self.bookForm.comboBox_2.addItems(self.genres)

            self.bookForm.comboBox.addItems(self.authors)
            self.bookForm.show()
        if self.statements["isUserBooksSelected"]:
            resUsers = self.userDB.getRecs()
            self.users.clear()
            self.books.clear()
            for row in resUsers:
                self.users[row[1]] = row[0]

            resBooks = self.bookDB.getRecs()
            for row in resBooks:
                self.books[row[1]] = row[0]
                print(row)

            self.addBookForm.comboBox.addItems(self.users)
            self.addBookForm.comboBox_2.addItems(self.books)
            self.addBookForm.show()

        elif self.statements["isAuthorSelected"]:
            self.authorForm.show()
        elif self.statements["isGenreSelected"]:
            self.genreForm.show()
        elif self.statements["isUserSelected"]:
            self.userForm.show()

    def showWindowEdit(self):
        row = self.tableWidget.currentRow()
        if self.statements["isBookSelected"]:
            name = self.tableWidget.item(row, 1).text()
            genre = self.tableWidget.item(row, 2).text()

            resAuthors = self.authorDB.getRecs()
            self.authors.clear()

            for row in resAuthors:
                self.authors[row[1]] = row[0]

            resGenres = self.genreDB.getRecs()
            self.genres.clear()

            for row in resGenres:
                self.genres[row[1]] = row[0]

            self.bookForm = BookWindow()
            self.bookForm.lineEdit.setText(name)
            self.bookForm.comboBox.addItems(self.authors)
            self.bookForm.comboBox_2.addItems(self.genres)

            self.bookForm.pushButton_2.clicked.connect(self.updateRow)
            self.bookForm.show()

        elif self.statements["isUserBooksSelected"]:
            user = self.tableWidget.item(row, 1).text()
            genre = self.tableWidget.item(row, 2).text()
            resUser = self.userDB.getRecs()
            self.users.clear()
            self.books.clear()
            for row in resUser:
                self.users[row[1]] = row[0]

            resBook = self.bookDB.getRecs()
            for row in resBook:
                self.books[row[1]] = row[0]

            self.addBookForm = addBookWindow()
            self.addBookForm.comboBox.addItems(self.users)
            self.addBookForm.comboBox_2.addItems(self.books)
            self.addBookForm.pushButton_2.clicked.connect(self.updateRow)
            self.addBookForm.show()

        elif self.statements["isAuthorSelected"]:
            name = self.tableWidget.item(row, 1).text()
            date = self.tableWidget.item(row, 2).text()
            self.authorForm = AuthorWindow()
            self.authorForm.pushButton_2.clicked.connect(self.updateRow)
            self.authorForm.lineEdit.setText(name)
            self.authorForm.dateEdit.setDate(QDate.fromString(date, "yyyy-MM-dd"))
            self.authorForm.show()

        elif self.statements["isGenreSelected"]:
            name = self.tableWidget.item(row, 1).text()
            self.genreForm = GenreWindow()
            self.genreForm.pushButton_2.clicked.connect(self.updateRow)
            self.genreForm.lineEdit.setText(name)
            self.genreForm.show()

        elif self.statements["isUserSelected"]:
            name = self.tableWidget.item(row, 1).text()
            date = self.tableWidget.item(row, 2).text()
            phone = self.tableWidget.item(row, 3).text()
            self.userForm = UserWindow()
            self.userForm.lineEdit.setText(name)
            self.userForm.dateEdit.setDate(QDate.fromString(date, "yyyy-MM-dd"))
            self.userForm.lineEdit_3.setText(phone)
            self.userForm.pushButton_2.clicked.connect(self.updateRow)
            self.userForm.show()

    def updateRow(self):
        row = self.tableWidget.currentRow()
        index = self.tableWidget.model().index(row, 0).data()
        if self.statements["isBookSelected"]:
            name = self.bookForm.lineEdit.text()
            genre = self.genres[self.bookForm.comboBox_2.currentText()]
            author = self.authors[self.bookForm.comboBox.currentText()]
            print("isBookSelected")
            if name != '' and genre != '':
                print("update", author)
                #genre = self.lineEdit.setText(self.tableWidget.item(row, 2).text())
                #author = self.lineEdit.setText(self.tableWidget.item(row, 3).text())
                self.bookDB.updateRec(name,genre, author, index)
                self.bookForm.lineEdit.setText("")
                self.bookForm.lineEdit_3.setText("")
                self.loadData(self.bookDB)
            self.bookForm.close()

        if self.statements["isUserBooksSelected"]:
            user = self.users[self.addBookForm.comboBox.currentText()]
            book = self.books[self.addBookForm.comboBox_2.currentText()]

            print("isBookSelected")
            if user != '' and book != '':
                #genre = self.lineEdit.setText(self.tableWidget.item(row, 2).text())
                #author = self.lineEdit.setText(self.tableWidget.item(row, 3).text())
                self.usersWithBooksDB.updateRec(user,book, index)
                self.loadData(self.usersWithBooksDB)
            self.addBookForm.close()

        elif self.statements["isAuthorSelected"]:
            name = self.authorForm.lineEdit.text()
            date = self.authorForm.dateEdit.date().toPython()
            print("isBookSelected")
            if name != '' and date != '':
                print("added")
                self.authorDB.updateRec(name, date, index)
                self.authorForm.lineEdit.setText("")
                self.loadData(self.authorDB)
            self.authorForm.close()

        elif self.statements["isGenreSelected"]:
            name = self.genreForm.lineEdit.text()
            print("isBookSelected")
            if name != '':
                print("added")
                self.genreDB.updateRec(name, index)
                self.genreForm.lineEdit.setText("")
                self.loadData(self.genreDB)
            self.genreForm.close()

        elif self.statements["isUserSelected"]:
            name = self.userForm.lineEdit.text()
            date = self.userForm.dateEdit.date().toPython()
            phone = self.userForm.lineEdit_3.text()
            print("isBookSelected")
            if name != '' and date != '' and phone != '':
                print("added")
                self.userDB.updateRec(name, date, phone, index)
                self.userForm.lineEdit.setText("")
                self.userForm.lineEdit_3.setText("")
                self.loadData(self.userDB)
            self.userForm.close()

    def addRow(self):
        if self.statements["isBookSelected"]:
            name = self.bookForm.lineEdit.text()
            genre = self.genres[self.bookForm.comboBox_2.currentText()]
            author = self.authors[self.bookForm.comboBox.currentText()]
            print("isBookSelected")
            if name != '' and genre != '':
                print("added")
                self.bookDB.insertData(name,genre, author)
                self.bookForm.lineEdit.setText("")
                self.bookForm.close()
                self.loadData(self.bookDB)

        elif self.statements["isAuthorSelected"]:
            name = self.authorForm.lineEdit.text()
            date = self.authorForm.dateEdit.date().toPython()
            print("isBookSelected")
            if name != '' and date != '':
                print("added")
                self.authorDB.insertData(name, date)
                self.authorForm.lineEdit.setText("")
                self.loadData(self.authorDB)
            self.authorForm.close()

        elif self.statements["isGenreSelected"]:
            name = self.genreForm.lineEdit.text()
            print("isBookSelected")
            if name != '':
                print("added")
                self.genreDB.insertData(name)
                self.genreForm.lineEdit.setText("")
                self.loadData(self.genreDB)
            self.genreForm.close()

        elif self.statements["isUserSelected"]:
            name = self.userForm.lineEdit.text()
            date = self.userForm.dateEdit.date().toPython()
            phone = self.userForm.lineEdit_3.text()
            print("isBookSelected")
            if name != '' and date != '' and phone != '':
                print("added")
                self.userDB.insertData(name, date, phone)
                self.userForm.lineEdit.setText("")
                self.userForm.lineEdit_3.setText("")
                self.loadData(self.userDB)
            self.userForm.close()

        elif self.statements["isUserBooksSelected"]:
            user = self.users[self.addBookForm.comboBox.currentText()]
            book = self.books[self.addBookForm.comboBox_2.currentText()]
            print("isUserBooksSelected")
            if user != '' and book != '':
                self.usersWithBooksDB.insertData(user, book)
                self.loadData(self.usersWithBooksDB)
            self.addBookForm.close()



    def removeRow(self):
        row = self.tableWidget.currentRow()
        index = self.tableWidget.model().index(row, 0)

        print(row)
        if row > -1:

            if self.statements["isBookSelected"]:
                self.bookDB.removeRec(index.data())
            elif self.statements["isAuthorSelected"]:
                self.authorDB.removeRec(index.data())
            elif self.statements["isGenreSelected"]:
                self.genreDB.removeRec(index.data())
            elif self.statements["isUserSelected"]:
                self.userDB.removeRec(index.data())
            elif self.statements["isUserBooksSelected"]:
                self.usersWithBooksDB.removeRec(index.data())

            self.tableWidget.removeRow(row)
            self.tableWidget.selectionModel().clearCurrentIndex()

    def searchRow(self):
        self.isSearched = True
        self.searchStr = self.lineEdit.text()
        print(self.searchStr)
        if self.searchStr != '':
            if self.statements["isBookSelected"]:
                self.loadData(self.bookDB)
            elif self.statements["isAuthorSelected"]:
                self.loadData(self.authorDB)
            elif self.statements["isGenreSelected"]:
                self.loadData(self.genreDB)
            elif self.statements["isUserSelected"]:
                self.loadData(self.userDB)
            elif self.statements["isUserBooksSelected"]:
                self.loadData(self.usersWithBooksDB)

        self.isSearched = False

    def loadData(self, source):
        self.tableWidget.clear()
        source.initDB()
        results = source.getRecs()
        if self.isSearched:
            results = source.searchRec(self.searchStr)
        tablerow = 0
        self.tableWidget.setRowCount(50)
        for state in self.statements.keys():
            self.statements[state] = False
        if type(source) is BookDB:
            cols = 4
            self.statements["isBookSelected"] = True
            self.tableWidget.setColumnCount(cols)
            self.tableWidget.geometry().width()
            for i in range(cols):
                self.tableWidget.setColumnWidth(i, (
                        self.tableWidget.geometry().width() - (self.pushButton.geometry().width()-50))/ cols)
            self.tableWidget.setHorizontalHeaderLabels(["id","name","genre", "author"])
            for row in results:
                print(row)
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
                tablerow += 1
        elif type(source) is AuthorDB:
            cols = 3
            self.statements["isAuthorSelected"] = True
            self.tableWidget.setColumnCount(cols)
            self.tableWidget.geometry().width()
            for i in range(cols):
                self.tableWidget.setColumnWidth(i, (
                            self.tableWidget.geometry().width() - (self.pushButton.geometry().width() - 50)) / cols)
            for row in results:
                print(row)
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                tablerow += 1

        elif type(source) is GenreDB:
            cols = 2
            self.statements["isGenreSelected"] = True
            self.tableWidget.setColumnCount(cols)
            self.tableWidget.geometry().width()
            for i in range(cols):
                self.tableWidget.setColumnWidth(i, (
                            self.tableWidget.geometry().width() - (self.pushButton.geometry().width() - 50)) / cols)
            for row in results:
                print(row)
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                tablerow += 1

        elif type(source) is UserDB:
            cols = 4
            self.statements["isUserSelected"] = True
            self.tableWidget.setColumnCount(cols)
            self.tableWidget.geometry().width()
            for i in range(cols):
                self.tableWidget.setColumnWidth(i, (
                            self.tableWidget.geometry().width() - (self.pushButton.geometry().width() - 50)) / cols)
            self.tableWidget.setHorizontalHeaderLabels(["id", "name", "reg_date", "phone"])

            for row in results:
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
                tablerow += 1
        elif type(source) is UsersWithBooksDB:
            cols = 3
            self.statements["isUserBooksSelected"] = True
            self.tableWidget.setColumnCount(cols)
            self.tableWidget.geometry().width()
            for i in range(cols):
                self.tableWidget.setColumnWidth(i, (
                            self.tableWidget.geometry().width() - (self.pushButton.geometry().width() - 50)) / cols)
            self.tableWidget.setHorizontalHeaderLabels(["id", "user_name", "book_name"])
            for row in results:
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
                tablerow += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())