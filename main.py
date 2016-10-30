import cv2
import os
import numpy as np

picsDirectory = '/Users/max/Desktop/comma-ai-challenge/projective_challenge/pics/'

def processImage(file):
	fPath = picsDirectory + file
	print(fPath)
	img = cv2.imread(fPath)
	
#	fimg = cv2.GaussianBlur(img,(5,5),10)

	fimg = img
	
	gray = cv2.cvtColor(fimg,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,2,3,0.04)
	dst = cv2.dilate(dst,None)
	ret, dst = cv2.threshold(dst,.0001 * dst.max(), 255, 0)
	dst = np.uint8(dst)

	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

	res = np.hstack((centroids,corners))
	res = np.int0(res)
	img[res[:,1],res[:,0]]=[0,0,255]
	img[res[:,3],res[:,2]] = [0,255,0]

	cv2.imwrite('/tmp/'+file,img)

def tryHomography():
	im1 = cv2.imread('/Users/max/Desktop/comma-ai-challenge/projective_challenge/pics/0_0.jpg')
	im2 = cv2.imread('/Users/max/Desktop/comma-ai-challenge/projective_challenge/pics/0_1.jpg')

	img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

	surf = cv2.SURF(400)


if __name__ == '__main__':
#	for filename in os.listdir(picsDirectory):
#		if filename.endswith((".png", ".jpg")):
#			processImage(filename)
	tryHomography()
