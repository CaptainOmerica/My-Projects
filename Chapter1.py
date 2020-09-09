import cv2
import numpy as np

print("Package Imported")

img=cv2.imread("Resources/Lenna.png")
kernel=np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Converts to Gray
imgBlur= cv2.GaussianBlur(imgGray,(5,5),0) #ksize defines how much blur; has to be an odd number
imgCanny= cv2.Canny(img,150,200) #Canny Edge Detection, Thresholds changeable
imgDilation=cv2.dilate(imgCanny,kernel, iterations=1)  #Thickens Canny Edges
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Gray Image lmao", imgGray)
cv2.imshow("Blur Image lmao", imgBlur)
cv2.imshow("Canny Image lmao", imgCanny)
cv2.imshow("Dilation Image lmao", imgDilation)
cv2.imshow("Erosion Image lmao", imgEroded)


cv2.waitKey(0)