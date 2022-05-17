import sqlite3
class UserDB(object):
    def __init__(self, cursor, connect):
        self.conn = connect
        self.c = cursor

    def initDB(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS users (id integer primary key, name text, date text, phone text)''')
        self.c.execute('''PRAGMA foreign_keys=ON''')
        self.conn.commit()

    def insertData(self, name, address, phone):
        self.c.execute('''INSERT INTO users(name, date, phone) VALUES (?, ?, ?)''',
                       (name, address, phone))
        self.conn.commit()

    def getRecs(self):
        return self.c.execute('''SELECT * FROM users LIMIT 40''')

    def removeRec(self, id):
        self.c.execute('DELETE FROM users WHERE id=%s' % id)

    def updateRec(self, name, address, phone, id):
        self.c.execute('''UPDATE users SET name=?, date=?, phone=? WHERE ID=?''',
                          (name, address, phone, str(id)))

    def searchRec(self, searchStr):
        searchStr = ('%' + searchStr + '%')
        return self.c.execute('''SELECT * FROM users
         WHERE name LIKE ? or date LIKE ? or phone LIKE ?''',
                       (searchStr, searchStr,searchStr))