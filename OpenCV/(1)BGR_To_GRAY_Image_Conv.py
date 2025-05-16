#show image
import cv2
img = cv2.imread("aditrisharmanew.jpg")
print(img.size)
print(img.shape)
print(img.dtype)
cv2.imshow("MYPHOTO",img)
cv2.imwrite("Aditriphoto.jpg",img)
cv2.waitKey(0)    #infinite display time
cv2.destroyAllWindows()


#grayImage
'''import cv2
img = cv2.imread("aditrisharmanew.jpg")
i = cv2.resize(img, (300,300))
grayImage = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)    #convert color
cv2.resize(grayImage,(30,30))
cv2.imwrite("GrayImage.jpg",grayImage)
cv2.imshow("GRAYIMAGE",grayImage)
cv2.imshow("IMAGE",i)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
