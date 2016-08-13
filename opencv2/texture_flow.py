#!/usr/bin/env python

'''
Texture flow direction estimation.

Sample shows how cv2.cornerEigenValsAndVecs function can be used
to estimate image texture flow direction.

Usage:
    texture_flow.py [<image>]
'''

import numpy as np
import cv2

if __name__ == '__main__':
    import sys
    try: fn = sys.argv[1]
    except: fn = 'data/starry_night.jpg'

    img = cv2.imread(fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]

    eigen = cv2.cornerEigenValsAndVecs(gray, 15, 3) # the block size==15, aperture size=3
    eigen = eigen.reshape(h, w, 3, 2)  # [[e1, e2], v1, v2]
	# eigenvalue1 eigenvalue2
	# eigenvector1
	# eigenvector2
    flow = eigen[:,:,2] #v2
	#flow = eigen[:,:,1] #the gradient directions

    vis = img.copy()
    vis[:] = (192 + np.uint32(vis)) / 2 # make the background lighter
	# make sure the 192+vis is not overflowed
    d = 15 # the length of the line segment 
    points =  np.dstack( np.mgrid[d/2:w:d, d/2:h:d] ).reshape(-1, 2)
	# reshape -1,2 to any*2
	# mgrid vector1 x vector2
	# dstack 
	# a:b:c for(x=a;x<b;x+=c)
    for x, y in points:
       vx, vy = np.int32(flow[y, x]*d)
       cv2.line(vis, (x-vx, y-vy), (x+vx, y+vy), (0, 0, 0), 1, cv2.CV_AA) # CV_AA, antialised, draw a line
    cv2.imshow('input', img)
    cv2.imshow('flow', vis)
    cv2.waitKey()
