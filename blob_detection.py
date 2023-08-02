#BLOB Analizi:
#BLOB (Binary Large Object) ikili büyük nesne anlamına gelir ve bir ikili görüntüde bağlı piksellerin bir grubunu ifade etmektedir.
#Büyük terimi belirli boyuttaki nesne olarak adlandırılır. 
#Dolayısıyla büyük boyutun dışında kalan küçük nesneler gürültü olarak değerlendirilir. 
#Görüntü işlemede nesne tespit etme konusunda özellikle yaygın kullanılır. 
#Bir görüntüde odaklandığımız nesneleri genellikle önce ikilik görüntüye çevirip BLOB haline getiririz.


#BLOB analizinin amacı: Bilgisayar görmesi, insan bilgisayar etkileşimi veya örüntü tanıma için nesnelerin etiketlenmesini 
#ya da başka bir ifade ile ikili görüntüdeki büyük nesneleri diğerlerinden (gürültüden) ayırıp etiketleyip öznitelik verileri üretmektir.

import cv2
import numpy as np;
 
im = cv2.imread("blob_image.jpeg", cv2.IMREAD_GRAYSCALE)
 
detector = cv2.SimpleBlobDetector()
 
keypoints = detector.detect(im)
 
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
