import cv2
import numpy as np

def nothing(x):
    pass

canvas = np.zeros((512,512,3),dtype=np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("R","Image",0,255,nothing)
cv2.createTrackbar("G","Image",0,255,nothing)
cv2.createTrackbar("B","Image",0,255,nothing)
cv2.createTrackbar("Switch","Image",0,1,nothing) #kontrol trackbar'ı


while True:
    cv2.imshow("Image",canvas)
    
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

    s = cv2.getTrackbarPos("Switch","Image")
    r = cv2.getTrackbarPos("R","Image")
    g = cv2.getTrackbarPos("G","Image")
    b = cv2.getTrackbarPos("B","Image")

    if s == 1:
        canvas[:] = [b,g,r]
    else:
        canvas[:] = [0,0,0]    



cv2.destroyAllWindows()










