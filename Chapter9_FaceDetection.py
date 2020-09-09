import cv2



img=cv2.imread("Resources/MichaelScarn.JPG")
img=cv2.resize(img,(600,600))
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

facez = faces.detectMultiScale(imgGray, 1.3, 5)


for n,(x,y,w,h) in enumerate(facez):
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)



cv2.imshow("Result",img)
print("There are",n+1,"faces in this photo")
cv2.waitKey(0)