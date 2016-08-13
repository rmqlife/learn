import os, base64
import sqlite3
filename='/Users/jzd/Documents/salty.db'
cx=sqlite3.connect(filename)
cu=cx.cursor()
cu.execute("select name from devimages")
print cu.fetchall()
k=[];
cu.execute("select image from devimages where name='img0'")
k=cu.fetchall()


leniystr=k[0][0];
imgData = base64.b64decode(leniystr)
leniyimg = open('imgout.jpg','wb')
leniyimg.write(imgData)
leniyimg.close()
