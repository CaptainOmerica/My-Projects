#WarpingmyRX7

import cv2
import numpy as np

img = cv2.imread("Resources/RX7_WARPD.jpg")
print(img.shape)
width,height=1550,700
pts1=np.float32([[3,211],[745,100],[86,536],[794,422]])  #find these values using MSPAINT lmao; point order is left, right,left,right
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)  #Gets the two points
output=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image", img)
cv2.imshow("Warped!",output)
cv2.waitKey(0)