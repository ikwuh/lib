import sqlite3
import sqlite3, sys, os, PySide2

class UsersWithBooksDB(object):
    def __init__(self, cursor, connect):
        self.conn = connect
        self.c = cursor

    def initDB(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS userWithBooks (id integer primary key, user_id int, book_id int,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE)''')
        self.c.execute('''PRAGMA foreign_keys=ON''')
        self.conn.commit()

    def insertData(self, user_id, book_id):
        self.c.execute('''INSERT INTO userWithBooks(user_id, book_id) VALUES (?, ?)''',
                       (user_id, book_id))
        self.conn.commit()

    def getRecs(self):
        return self.c.execute('''SELECT userWithBooks.id, users.name, books.name FROM userWithBooks
          INNER JOIN users ON user_id = users.id
          INNER JOIN books ON book_id = books.id
          LIMIT 40''')

    def removeRec(self, id):
        self.c.execute(f'DELETE FROM userWithBooks WHERE id=%s' % id)


    def updateRec(self, user_id, book_id, id):
        self.c.execute('''UPDATE userWithBooks SET user_id=?, book_id=? WHERE ID=?''',
                          (user_id, book_id, str(id)))

    def searchRec(self, searchStr):
        searchStr = ('%' + searchStr + '%')
        return self.c.execute('''SELECT userWithBooks.id, users.name, books.name FROM userWithBooks
        INNER JOIN users ON user_id = users.id
        INNER JOIN books ON book_id = books.id
        WHERE users.name LIKE ? or books.name LIKE ?''',
                       (searchStr, searchStr))