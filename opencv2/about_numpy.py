'''
Learn the use of numpy, which is the basic structure of openCV with python.
'''
import numpy as np
import cv2
debug_fag=True
if __name__ == '__main__':
	# get input
	import sys
	try: fn = sys.argv[1]
	except: fn = 'python2/data/starry_night.jpg'
	img=cv2.imread(fn)
	# main process
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rows,cols=gray.shape[:2]
	print "size=",gray.shape
	print "rows=",gray.shape[0]
	print "cols=",gray.shape[1]
	
	center=(gray.shape[0]/2,gray.shape[1]/2)
	print "center=",center
	window_size=100
	# a horizonal stripe in the middle
	rect=img[center[0]-window_size/2:center[0]+window_size/2]
	# a window in the middle
	rect=img[center[0]-window_size/2:center[0]+window_size/2\
	,center[1]-window_size/2:center[1]+window_size/2]
	# a single channel of the BGR image, and copy it
	rect=img[:,:,0].copy()
	# copy a image
	# create mat
	a=np.eye(3)
	a=np.ones([3,4])
	a=np.zeros([3,4])
	a=np.arange(1:12:1).reshape(-1,4)
	
	# show for debug
	if debug_fag:
		cv2.imshow('rect',rect)
		cv2.waitKey()
