import cv2

video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    success,frame = video.read()
    hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width,_ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixelCenter = hsvFrame[cy,cx]

    hueValue = pixelCenter[0]

    color = "Belirli degil"
    if hueValue < 5:
        color = "KIRMIZI"
    elif hueValue < 22:
        color = "TURUNCU"    
    elif hueValue < 33:
        color = "SARI"
    elif hueValue < 78:
        color = "YESİL"
    elif hueValue < 131:
        color = "MAVİ"
    elif hueValue < 170:
        color = "MOR"
    else: 
        color = "KIRMIZI"                    


    print(pixelCenter)
    cv2.putText(frame,color,(10,50),0,1,(255,0,0),2)
    cv2.circle(frame,(cx,cy),5,(255,0,0),3)

    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()


