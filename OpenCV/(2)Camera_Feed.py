import cv2
import time
cam = cv2.VideoCapture(0)    #0 takes your laptops inbuilt camera
                                                         #1 takes other camers device connected  with usb
time.sleep(1)        #after 1 second it will off and display the captured image
_,img = cam.read()
cv2.imwrite("imagefromcamera.jpg",img)
cam.release()
