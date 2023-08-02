import cv2
import numpy as np

img1 = cv2.imread("mars.jpeg",0)
img2 = cv2.imread("agac.jpeg")

print(img1.shape)
print(img2.shape)

#resimlerin kendilerine eşit olması için resize'ladık.
img1 = cv2.resize(img1,(0,0),None,0.5,0.5)
img2 = cv2.resize(img2,(0,0),None,0.5,0.5)

img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR) # bir kanaldan 3 kanala dönüştürmek için,
#eğer resimlerden biri tek kanallı yani gri olsaydı.


yatay = np.hstack((img1,img2)) #yatay birleştirme
dikey = np.vstack((img1,img2)) #dikey birleştirme

cv2.imshow("Dikey", dikey)
cv2.imshow("Yatay", yatay)

cv2.waitKey(0)
cv2.destroyAllWindows()