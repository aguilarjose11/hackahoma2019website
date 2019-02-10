import sqlite3 as sql
from os import path
ROOT = path.dirname(path.realpath(__file__))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def authenticate(user, psw):
        con = sql.connect(path.join(ROOT, 'database.db'))
        cur = con.cursor()
        result = cur.execute('select * from keychain where username=? and password=?;', (user, psw)).fetchall()
        con.close()
        if result:
            return True
            #loged in!
        else:
            return False

def databasesize():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    total = cur.execute('select max(ID) from posts ').fetchall()
    return total
