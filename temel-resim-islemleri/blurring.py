import cv2
import numpy as np

kamera= cv2.VideoCapture(0)

while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_mavi=np.array([100,60,60])
    ust_mavi=np.array([140,255,255])

    mask=cv2.inRange(hsv,dusuk_mavi,ust_mavi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(frame,-1,kernel)

    blur=cv2.GaussianBlur(son_resim,(15,15),0)
    median=cv2.medianBlur(son_resim,15)
    bileteral=cv2.bilateralFilter(son_resim,15,75,75)



    cv2.imshow('orjinal',frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('bileteral', smoothed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()