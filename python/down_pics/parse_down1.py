import urllib,urllib2
import os

def down_page(link,target_dir):
    f= urllib.urlopen(link);
    myfile=f.read()
    import re
    targetcount=0
    urls=re.findall('''src="(http[^ ]+?jpg)"''',myfile)
    for i in urls:
        targetname=os.path.basename(i)
        if (len(targetname)>40 and len(targetname)<50):
            print targetname
            targetcount=targetcount+1
            os.system("wget"+" "+i)
            os.system("mv"+" "+targetname+" "+target_dir+str(targetcount)+".jpg")
    f.close()

def main():
    for page_num in range(40,52):
        link="http://tieba.baidu.com/p/2123788751?pn=%d" % (page_num)
        if not os.path.exists(str(page_num)):
            os.mkdir(str(page_num))
            down_page(link,str(page_num)+"/")

if __name__=="__main__":
    main()
