import sqlite3
import sqlite3, sys, os, PySide2



class BookDB(object):
    def __init__(self, cursor, connect):
        self.conn = connect
        self.c = cursor

    def initDB(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS books (id integer primary key, name text, genre int, author int,
             FOREIGN KEY (genre) REFERENCES genres(id) ON DELETE CASCADE,
             FOREIGN KEY (author) REFERENCES authors(id) ON DELETE CASCADE )''')
        self.c.execute('''PRAGMA foreign_keys=ON''')
        self.conn.commit()

    def insertData(self, name, genre, author):
        self.c.execute('''INSERT INTO books(name, genre, author) VALUES (?, ?, ?)''',
                       (name, genre, author))
        self.conn.commit()

    def getRecs(self):
        print()
        return self.c.execute('''SELECT books.id, books.name, genres.name, authors.name 
         FROM books
        INNER JOIN authors ON books.author = authors.id
         INNER JOIN genres ON books.genre = genres.id
         LIMIT 40''')

    def removeRec(self, id):
        self.c.execute(f'DELETE FROM books WHERE id=%s' % id)


    def updateRec(self, name, genre, author, id):
        self.c.execute('''UPDATE books SET name=?, genre=?, author=? WHERE ID=?''',
                          (name, genre, author, str(id)))

    def searchRec(self, searchStr):
        searchStr = ('%' + searchStr + '%')
        return self.c.execute('''SELECT books.id, books.name, genres.name, authors.name 
         FROM books INNER JOIN authors ON books.author = authors.id
        INNER JOIN genres ON books.genre = genres.id
         WHERE books.name LIKE ? or books.genre LIKE ? or authors.name LIKE ?''',
                       (searchStr, searchStr,searchStr))