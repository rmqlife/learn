#coding=utf-8
import urllib,urllib2
import os
import wget
import re

body=''' 
Buns ln My Oven

####FONT_SIZE=28    
####BOX=251,74,469,102    
the year!

http://www.bunsinrnyoven.com/2012/08/14/

enchilada-casserole/

####FONT_SIZE=27    
####BOX=40,159,593,252    
-> http://www.pinterest.com/

pin/123356477268926025/

'''

# body= body.replace(" ","")
body= body.replace("\n","")

print body
urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)

print urls