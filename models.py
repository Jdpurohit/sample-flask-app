import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_method(name, content):

    con = sql.connect(path.join(ROOT, 'sampledatabase.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_method():
    con = sql.connect(path.join(ROOT, 'sampledatabase.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts