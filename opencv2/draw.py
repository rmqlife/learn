import cv2
import numpy as np
from common import Sketcher
if __name__=="__main__":
	import sys
	try: fn=sys.argv[1]
	except: fn="data/lena.jpg"
	img=cv2.imread(fn)
	img_mark=img.copy()
	mark=np.zeros(img.shape[:2],np.uint8)
	sketch=Sketcher('img',[img_mark,mark],lambda:((255,255,0),200)) # the color on the img_mark, the color on the mark
	cv2.waitKey()
	cv2.imwrite('img_mark.jpg',img_mark)
	cv2.imwrite('mark.jpg',mark)