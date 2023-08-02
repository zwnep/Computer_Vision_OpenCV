import cv2
import numpy as np


#OpenCV'de özellik algılama, bir görüntüdeki önemli noktaları tanımlama işlemidir. 
#Bu noktalar, nesneleri veya kalıpları tanımlamak, görüntüleri eşleştirmek veya görüntüleri birleştirmek için kullanılabilir.

#OpenCV'de özellik algılama için çok çeşitli yöntemler vardır. 
#En yaygın yöntemlerden bazıları şunlardır:
#Harris köşe algılayıcı
#Shi-Tomasi köşe algılayıcı
#SIFT (ölçeklere duyarlı özellik dönüşümü)
#SURF (hızlandırılmış sağlam özellikler)

#Bu yöntemler, görüntüdeki önemli noktaları tanımlamak için farklı teknikler kullanır. 
#Harris köşe algılayıcı, bir görüntüdeki köşeleri tanımlamak için bir matematiksel yaklaşım kullanır. 
#Shi-Tomasi köşe algılayıcı, Harris köşe algılayıcıdan daha sağlamdır ve gürültüye karşı daha duyarlıdır. 
#SIFT ve SURF, görüntüdeki önemli noktaları tanımlamak için daha karmaşık teknikler kullanır ve ölçek, dönüş ve aydınlatma değişikliklerine karşı daha duyarlıdır.

#OpenCV'de özellik algılamanın mantığı, görüntüdeki önemli noktaları tanımlamak ve bunları bir veri kümesi oluşturmak için kullanmaktır. 
#Bu veri kümesi daha sonra nesneleri veya kalıpları tanımlamak, görüntüleri eşleştirmek veya görüntüleri birleştirmek için kullanılabilir.

#Örneğin, bir görüntüdeki insan yüzlerini tanımak istiyorsanız, OpenCV'yi kullanarak yüzlerin özelliklerini tanımlayabilirsiniz.
#Bu özellikler daha sonra bir veri kümesi oluşturmak için kullanılabilir. 
#Bu veri kümesi daha sonra bir yüz tanıma algoritması eğitmek için kullanılabilir. 
#Yüz tanıma algoritması, bir görüntüdeki bir kişinin yüzünün özelliklerini tanımlayarak kişinin kim olduğunu belirleyebilir.




#HARRIS CORNER DETECTION
#Harris Köşe Bulma Algoritması'nın temel mantığı, bir pikselin etrafındaki bölgeyi küçük bir pencere ile karşılaştırarak ve 
#bu pencereyi farklı yönlerde kaydırarak kenar ve köşe bölgelerini tespit etmektir. 

#cv2.cornerHarris(src,dest,blockSize,ksize,k)
#src -> input image
#dest -> Harris detector response
#blockSize -> neighborhood size 
#ksize -> 
#k -> free parameter 

image = cv2.imread("chessboard.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#cv2.imshow("gray",gray)

corner = cv2.cornerHarris(gray,7,5,0.1)

corner = cv2.dilate(corner,None)

cv2.imshow("corner",corner)

image[corner>0.01*corner.max()] = [0,0,255]

cv2.imshow("image corner",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Şimdi algoritmanın çalışma mantığına göz atalım:
# 1)Görüntüyü gri tonlamalı hale getir: Algoritma, kenar ve köşe tespiti için tek bir renk kanalı olan gri tonlamalı görüntüleri kullanır. 
# Renk bilgisinin çıkarılması, işlemleri basitleştirir.

# 2)Gradient Hesaplama: Algoritma, görüntüdeki yoğunluk değişikliklerini tespit etmek için Sobel operatörü veya benzeri bir yöntemle görüntü gradyanını hesaplar.
# Gradient, piksel değerlerindeki yoğunluk değişikliklerinin yön ve büyüklüğünü ifade eder.

# 3)Otomatik korelasyon matrisinin hesaplanması: Algoritma, her piksel için belirli bir pencere boyutunda otomatik korelasyon matrisini hesaplar.
# Bu matris, piksel etrafındaki yoğunluk değişikliklerinin korelasyonunu ifade eder.

# 4)Harris köşe tepki fonksiyonu hesaplama: Algoritma, her piksel için Harris köşe tepki fonksiyonunu hesaplar.
# Bu tepki fonksiyonu, pikselin bir köşe olasılığını ölçer ve kenarların tepki değerini azaltır. Harris köşe tepki fonksiyonu, özdeğerler aracılığıyla hesaplanır.

# 5)Köşe noktalarının tespiti: Algoritma, belirli bir eşik değeri kullanarak tepki fonksiyonu değerlerine dayanarak köşe noktalarını tespit eder. 
# Tepki fonksiyonu değeri, eşik değerinden büyükse ve lokal maksimum bir değerse, o nokta bir köşe olarak kabul edilir.


# Sonuç olarak, Harris Köşe Bulma Algoritması, görüntüdeki kenar ve köşe noktalarını tespit etmek için otomatik korelasyon matrisini ve tepki fonksiyonunu kullanır.
# Bu yöntem, özellik eşleştirme, nesne tanıma, hareket analizi ve stereo görüş gibi birçok görüntü işleme ve bilgisayar görüşü uygulamasında kullanılmaktadır.




