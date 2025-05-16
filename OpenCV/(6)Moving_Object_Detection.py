import cv2
import time
import imutils
cam = cv2.VideoCapture(0)
time.sleep(3)
firstFrame = None
area = 500
while True:
    _,img = cam.read()
    text = "Normal"
    img = imutils.resize(img, width = 500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21,21), 0)
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    #cv2.imshow("camerafeed", imgDiff)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
   #cv2.imshow("camerafeed", threshImg)
    threshImg = cv2.dilate(threshImg, None, iterations=2)
   #cv2.imshow("camerafeed", threshImg)
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    count = 0
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0),  2) 
        text = "Moving Object detected"
        count = count+1
        text2 = f"No of Objects : {count}"
        print(text)
        print(text2)
    cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("camerafeed",img)
    key = cv2.waitKey(3)
    if key==ord("t"):
        break
cam.release()
cv2.destroyAllWindows()
                      
