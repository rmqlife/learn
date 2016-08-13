import urllib,urllib2
import os
import wget


link="http://www.cvpapers.com/cvpr2014.html"
f= urllib.urlopen(link);
myfile=f.read()
f.close()
# print myfile

import re
# '''<dt>(.+?)\(<a href="(http[^ ]+?)">PDF</a>\)'''
# urls=re.findall('''<a href="(http[^ ]+?)">PDF</a>''',myfile)
urls=re.findall('''<dt>(.+?)\(<a href="(http[^ ]+?)">PDF</a>\)''',myfile)

# urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', myfile)
# print urls


from subprocess import call
for name,i in urls:
    # name = os.path.basename(i)
    name = name+'.pdf'
    print name
    print i
    if os.path.exists(name):
    	continue
    try:
    	filename=wget.download(i)
    	os.rename(filename, name);
    except:
    	pass
	# call(["wget",'http://www.cvpapers.com/cvpr2014.html']);