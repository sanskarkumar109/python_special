import cv2
import numpy as np

img=cv2.imread(r'C:\Users\ASUS\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2022-05-04 at 5.54.38 PM.jpeg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

color=cv2.bilateralFilter(img,9,250,250)
unique=cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Iamge",img)
cv2.imshow("edges",edges)
cv2.imshow("unique",unique)

cv2.waitKey(0)
cv2.destroyAllWindows()
