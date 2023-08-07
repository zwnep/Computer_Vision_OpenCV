import numpy as np
import cv2



resim=cv2.imread('kose_bulma.jpg')
griton=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
griton=np.float32(griton)

koseler=cv2.goodFeaturesToTrack(griton,300,0.01,10)
koseler=np.int0(koseler)

for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(resim,(x,y),3,255,-1)

cv2.imshow('koseler',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()