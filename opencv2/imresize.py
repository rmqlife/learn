'''
a tool to resize picture based on OpenCV and python
source filename, destine filename, height, width
'''

import cv2

def resize(img,h,w):
	h0,w0=img.shape[:2]
	h1,w1=(h,w)
	if h<=0 and w<=0:
		print 'haha'
		h1,w1=(h0,w0)
	elif h<=0:
		h1=h0*w/w0
		w1=w
	elif w<=0:
		h1=h
		w1=w0*h/h0
	return cv2.resize(img,(w1,h1))

def run(srcfn,dstfn,h,w):
	src=cv2.imread(srcfn)
	dst=resize(src,h,w)
	cv2.imwrite(dstfn,dst)
	
if __name__=="__main__":
	import sys
	run(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))

