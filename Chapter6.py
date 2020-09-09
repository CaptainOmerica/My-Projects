# Horziontally Stacking Images together!
import cv2
import numpy as np

img=cv2.imread('Resources/Lenna.png')

print(img.shape)

imgHor=np.hstack((img,img,img))  #horizontal stack
lenaonlena=np.vstack((img,img))  #vertical stack

cv2.imshow("Threesome",imgHor)
cv2.imshow("Babe on Babe",lenaonlena)
cv2.waitKey(0)