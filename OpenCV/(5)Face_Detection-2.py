import cv2
import os
path=os.getcwd()
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam  = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    if(len(face)>0):
        for (x,y,w,h) in face:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        message = "person detected"
    else:
        message = "no person detected"
    cv2.putText(img, message, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key==ord("g"):
        break
print("image captured successfully")
cam.release()
cv2.destroyAllWindows()
