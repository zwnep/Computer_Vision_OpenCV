import cv2
import numpy as np

image = cv2.imread("sekiller.png")

font = cv2.FONT_HERSHEY_COMPLEX
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
a,thresh = cv2.threshold(gray,200,300,cv2.THRESH_BINARY)
kontur,b = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in kontur:
    e = 0.01*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,e,True)
    cv2.drawContours(image,[approx],0,5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    print(approx)
    print(len(approx))

    if len(approx) == 3:
        cv2.putText(image,"ucgen",(x,y),font,1,1,(0))
    if len(approx) == 4:
        cv2.putText(image,"dortgen",(x,y),font,1,1,(0))  
    else:
        cv2.putText(image,"daire",(x,y),font,1,1,(0))      


cv2.imshow("şekiller",image)

cv2.waitKey(0)
cv2.destroyAllWindows()