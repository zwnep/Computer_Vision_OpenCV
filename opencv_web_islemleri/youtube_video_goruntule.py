import pafy
import cv2

url='https://www.youtube.com/watch?v=R9Fu6Leb_aE'
vPaffy=pafy.new(url)
play=vPaffy.getbest(preftype="webm")

kamera=cv2.VideoCapture(play.url)
while True:
    _, video=kamera.read()
    griton=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)

    cv2.imshow('video',video)
    cv2.imshow('griton', griton)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()