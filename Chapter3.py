#RESIZING N CROPPING
#in Open CV, the positive y axis is downwards (southwards)

import cv2
import numpy as np

img=cv2.imread("Resources/lambo.png")
print(img.shape)  #(Height,Width,Color Channels (BGR))

imgResize=cv2.resize(img,(300,200)) #here width comes first and then height
print(imgResize.shape)

imgCropped = img[0:200,200:500]  #Height Cropped 0 to 200, Width Cropped: 200 to 500

cv2.imshow("Image",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)

