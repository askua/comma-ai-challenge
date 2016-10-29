import cv2


img = cv2.imread('projective_challenge/pics/0_0.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img, None)
print("# kps: {}, descriptors: {}".format(len(kp), des.shape))
