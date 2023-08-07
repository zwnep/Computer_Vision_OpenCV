import cv2
yuz_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
goz_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

kamera=cv2.VideoCapture(0)

while True:
    _,goruntu=kamera.read()
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_cascade.detectMultiScale(griton,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(255,0,0),2)
        roi_griton=griton[y:y+h,x:x+w]
        roi_renkli=goruntu[y:y+h,x:x+w]
        gozler=goz_cascade.detectMultiScale(roi_griton)
        for(ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(0,158,0),2)
    cv2.imshow('goruntu',goruntu)
    if cv2.waitKey(13) &0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()