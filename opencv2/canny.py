'''
  Trackbars to find the proper thresholds.
'''

import cv2

def on_trackbar(thresh1):
	edge=cv2.Canny(gray,thresh1,thresh1*3)
	cv2.imshow('canny',edge)

if __name__=='__main__':
	try: fn=sys.argv[1]
	except: fn='data/lena.jpg'
	img=cv2.imread(fn)
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	cv2.namedWindow('canny')
	cv2.createTrackbar('thresh1','canny',1,100,on_trackbar)
	on_trackbar(0)
	cv2.waitKey(0)
	cv2.destroyAllWindows()