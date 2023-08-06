import cv2

kamera = cv2.VideoCapture(0)

#kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
#kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#video boyutalandırma için bir yöntem

while True:
    ret,goruntu = kamera.read()
    ret = kamera.set(3,640) #ret'den aldığımız 3. bilgi width özelliğidir.
    ret = kamera.set(4,480) #ret'den aldığımız 4. bilgi height özelliğidir.

    gray = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    cv2.imshow("goruntu",goruntu)
    cv2.imshow("goruntu-gri",gray)

    if cv2.waitKey(25) & 0xFF == orf("q"):
        break


kamera.release()
cv2.destroyAllWindows()
