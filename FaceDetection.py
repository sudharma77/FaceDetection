import cv2


path = "Face/Face.xml"
faceCascade = cv2.CascadeClassifier("Face/Face.xml")
img = cv2.imread("image/dp1.jpg")
imgGray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
imgGray.save("geeks.jpg")
faces = faceCascade.detectMultiScale(imgGray ,1.1 ,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img ,(x,y),(x+w ,y+h),(0,225,0),2)

cv2.imshow("Image" ,img)
cv2.waitKey(0)