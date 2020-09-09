import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #^image, extreme external contours retrieved only, request for ALL the contours (no compressed info)
    for cnt in contours:
        area=cv2.contourArea(cnt) #gives you the areas of the contour
        print(area)
        cv2.drawContours(imgContour,cnt,-1,(0,255,0),3)


path='Resources/shapes.png'
img=cv2.imread(path)
imgContour=img.copy()

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
blur=cv2.GaussianBlur(gray,(7,7),1) #blurring it a lil

imgCanny=cv2.Canny(blur,50,50)

h_stack=np.hstack((gray,blur))

cv2.imshow("Original", h_stack)
cv2.imshow("uncanny!", imgCanny)
cv2.imshow("contour", imgContour)

blankimage=np.zeros_like(img)

getContours(imgCanny)




cv2.waitKey(0)