import cv2
import numpy as np 

img = np.zeros((512,512,3),np.uint8) #float tipinde matris oluşturumasın diye uint8 yazdım.

print(img)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(100,200),(450,140),(0,250,250)) #(yüklenecek resim,başlangıç noktası,bitiş noktası,rengi)
cv2.circle(img,(150,400),75,(255,255,56),3)

cv2.putText(img,"görüntü işleme",(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,4,(150,150,150),2)

cv2.imshow("deneme resmi",img)

cv2.waitKey(0)