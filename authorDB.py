import sqlite3
class AuthorDB(object):
    def __init__(self, cursor, connect):
        self.conn = connect
        self.c = cursor

    def initDB(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS authors (id integer primary key, name text, date text )''')
        self.c.execute('''PRAGMA foreign_keys=ON''')
        self.conn.commit()

    def insertData(self, name, date):
        self.c.execute('''INSERT INTO authors(name, date) VALUES (?, ?)''',
                       (name, date))
        self.conn.commit()

    def getRecs(self):
        return self.c.execute('''SELECT * FROM authors LIMIT 40''')

    def removeRec(self, id):
        self.c.execute('DELETE FROM authors WHERE id=%s' % id)


    def updateRec(self, name, date, id):
        self.c.execute('''UPDATE authors SET name=?, date=? WHERE ID=?''',
                          (name, date,str(id)))

    def searchRec(self, searchStr):
        searchStr = ('%' + searchStr + '%')
        return self.c.execute('''SELECT * FROM authors WHERE name LIKE ? or date LIKE ?''',
                       (searchStr, searchStr ))