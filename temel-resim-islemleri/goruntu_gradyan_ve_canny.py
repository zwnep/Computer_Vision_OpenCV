import cv2
import numpy as np

kamera= cv2.VideoCapture(0)

while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_mavi=np.array([100,60,60])
    ust_mavi=np.array([140,255,255])

    kenarlar=cv2.Canny(frame,100,150)

    mask=cv2.inRange(hsv,dusuk_mavi,ust_mavi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)


    cv2.imshow('orjinal',frame)
    cv2.imshow('kenarlar', kenarlar)



    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()