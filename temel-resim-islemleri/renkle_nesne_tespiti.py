import cv2
import numpy as np


image = cv2.imread("color-blue.jpg")

blue_lower = np.array([150,50,50])
blue_upper = np.array([255,255,255])

blueImage = cv2.inRange(image,blue_lower,blue_upper)

cv2.imshow("original",image)
cv2.imshow("Just Blue",blueImage)


#bgr->hsv
img_HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("rgb to hsv",img_HSV)

hsv_lower = np.array([84,98,0])
hsv_upper = np.array([179,255,255])

hsvImage = cv2.inRange(img_HSV,hsv_lower,hsv_upper)

cv2.imshow("hsv ımage",hsvImage)


#Kameradan görüntü alma
#HSV renk uzayının kullanılmasının sebebi aynı rengin farklı tonlarını belirlemek daha kolaydır.

video = cv2.VideoCapture(1) 

while True:
    success,frame = video.read()
    frame = cv2.flip(frame,1)
    hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerGreen = np.array([36, 25, 25])
    upperGreen = np.array([70, 255,255])

    greenMask = cv2.inRange(hsvFrame,lowerGreen,upperGreen) #fonksiyonun amacı girilen değerler arasındaki renkleri tespit etme
    green = cv2.bitwise_and(frame,frame,mask=greenMask) #fonskiyonun amacı frame ile frame'i karşılaştırıp yeşil olan yerleri döndürüyor.


    lowerBlue = np.array([100,150,0])
    upperBlue = np.array([140,255,255])

    blueMask = cv2.inRange(hsvFrame,lowerBlue,upperBlue)
    blue = cv2.bitwise_and(frame,frame,mask=blueMask)

    
    #cv2.imshow("Webcam",frame)
    #cv2.imshow("Green Mask",greenMask)
    cv2.imshow("Just Green",green)

    cv2.imshow("Just Blue",blue)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()

