import sqlite3
class GenreDB(object):
    def __init__(self, cursor, connect):
        self.conn = connect
        self.c = cursor

    def initDB(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS genres (id integer primary key, name text)''')
        self.c.execute('''PRAGMA foreign_keys=ON''')
        self.conn.commit()

    def insertData(self, name):
        self.c.execute('''INSERT INTO genres(name) VALUES (?)''',
                       (name, ))
        self.conn.commit()

    def getRecs(self):
        return self.c.execute('''SELECT * FROM genres LIMIT 40''')

    def removeRec(self, id):
        self.c.execute('DELETE FROM genres WHERE id=%s' % id)


    def updateRec(self, name, id):
        self.c.execute('''UPDATE genres SET name=? WHERE ID=?''',
                          (name, str(id)))

    def searchRec(self, searchStr):
        searchStr = ('%' + searchStr + '%')
        return self.c.execute('''SELECT * FROM genres WHERE name LIKE ?''',
                       (searchStr,))