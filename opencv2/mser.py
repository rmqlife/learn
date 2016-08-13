'''
maximal stable extremal regions, MSER detector
'''
import cv2
import video # a file library of video reading for python
def find(img):
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	mser=cv2.MSER()	
	regions=mser.detect(gray,None)
	return regions

def draw(vis,regions):
	# get convex hulls from these points, reshape is to separate these points by different region
	hulls=[cv2.convexHull(p.reshape(-1,1,2)) for p in regions]
	cv2.polylines(vis,hulls,1,(0,255,0))
	
def cam():
	cam=video.create_capture(0)
	while True:
		ret,img= cam.read()
		regions=find(img)
		vis=img.copy()
		draw(vis,regions)
		cv2.imshow('vis',vis)
		if 0xFF & cv2.waitKey(5)==27:
			break
	cv2.destroyAllWindows()

if __name__=='__main__':
	cam()
