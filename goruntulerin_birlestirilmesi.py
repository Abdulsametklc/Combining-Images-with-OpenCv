import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("Lenna_(test_image)")
cv2.imshow("Orijinal",img)

#yatay 
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

#dikey
ver = np.vstack((img,img))
cv2.imshow("Dikey", ver)