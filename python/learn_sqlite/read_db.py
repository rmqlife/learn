import os, base64
import sqlite3
def getImage(tag):
        filename='newfish.db'
        cx=sqlite3.connect(filename)
        cu=cx.cursor()
        k=[];
        cu.execute("select * from tags where name like'%%s%'"%tag)
        k=cu.fetchone()
        print k

a=raw_input("search:")
getImage(a)
