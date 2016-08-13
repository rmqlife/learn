import sqlite3
import os
import os.path


filename='/Users/jzd/Desktop/pics/Dev/saltyfish.db'
tsvname='/Users/jzd/Desktop/pics/Dev/TrainClickLog.tsv'
os.remove(filename)
cx=sqlite3.connect(filename)
cu=cx.cursor()
cu.execute("create table dict (name varchar(50) UNIQUE, count integer)")


count=0;
s=[]
tsvData=open(tsvname,'r')
for line in tsvData:
        s=line.split('\t')
        #break
        k=[]
        k=[s[1],int(s[2])]
        #print k
        if k[1]>100:
                k[0]=k[0].decode('utf8')
                cu.execute("insert or replace into dict values (?,?)", k)
                count=count+1
                if count%1000==0:
                        cx.commit()
                        print k[0]
                        print count
cx.commit()



#cu.execute("update catalog set name='Boy' where id = 0")

