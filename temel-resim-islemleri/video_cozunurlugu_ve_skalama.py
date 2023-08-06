import cv2

kamera= cv2.VideoCapture(0)

def cozun_1080p():
    kamera.set(3,1920)
    kamera.set(4,1080)

def cozun_720p():
    kamera.set(3,1280)
    kamera.set(4,720)

def cozun_480p():
    kamera.set(3,640)
    kamera.set(4,480)

def coz_belirle(width, height):
    kamera.set(3, width)
    kamera.set(4, height)

cozun_1080p()


#tekrardan ölçeklendirmek için
def scalalama(frame, percent=75):
    width=int(frame.shape[1]*percent/100)
    height = int(frame.shape[0] * percent / 100)
    boyut=(width,height)

    return cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)


while True:
    ret, frame= kamera.read()
    frame150=scalalama(frame,155)
    cv2.imshow('goruntu1',frame)
    cv2.imshow('goruntu2', frame150)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
 