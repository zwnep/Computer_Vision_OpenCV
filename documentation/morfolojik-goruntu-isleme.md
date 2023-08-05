# Morfolojik Görüntü işleme

Morfoloji (İngilizce morphology) şekil bilimi olarak tanımlanmaktadır. Başlı başına bilim olan bu alanı tüm yöntemleri ile OpenCV Kütüphanesi içerisine taşımak elbette ki mantıklı bir seçim değildir bu yüzden ihtiyaç duyulabilecek bazı teknikler aktarılmıştır. Morfolojik görüntü işleme (morphology ) görüntü içindeki nesnelerin şekilleri (morfolojisi) ile ilgilenen bir dizi görüntü işleme tekniklerini tarif etmektedir.

![morfolojik görüntü işleme](https://miro.medium.com/v2/resize:fit:990/1*x5YxCmfTirD5ME6DBLAvUg.png)

Morfoloji’nin bir şekil bilimi olduğunu söylemiştik, çalışılan görüntü üzerindeki şekillerin yorumlanması, analiz edilmesi, istenilen bilginin çıkartılması, inceltme, görüntü sıkıştırma, köşe analizi, bozuk görüntü onarma (eksik veya fazla piksellerin çıkarılması, eklenmesi), dokuların tespiti gibi işlemlerde sıklıkla başvurulmaktadır.

Gri tonlu imgeler üzerinde de yapılabileceği gibi, genellikle ikili imgeler üzerinde yapılan işlemlerdir.


![morfolojik görüntü işleme](https://miro.medium.com/v2/resize:fit:726/1*k5k3172-W6S8lOs4aOwMjQ.png)

- Erosion (Aşındırma)
- Dilation (Yayma – Genişletme)
- Opening (Açınım)
- Closing (Kapanım)
- Morphological Gradient


**Erosion (Aşındırma)**

Bu operatör görüntü üzerinde bir aşındırma işlemi uygular. Parametrelere göre belirtilen alan içerisindeki pikseller aşındırılır ve gürültülü olarak adlandırılan bozuk olan görüntü, gürültüden arındırılarak temizlenir. Bütün bu olaylar matematiksel olarak tanımlanmıştır ve diziler üzerinde gerçekleştirilir. Aşağıdaki görseller yardımı ile nasıl çalıştığını somut olarak görelim. İlk görüntü dizisi aşındırma ile gürültüden arındırılmaktadır.

![morfolojik görüntü işleme](https://miro.medium.com/v2/resize:fit:960/1*o9KZrfuUwUkf79lPxLbKoA.png)

Erosion işlemi için kullanacağımız metot erode(), bu metot imgproc içerisinde yer almaktadır.  Erode metodunun üç adet overloadı bulunmaktadır. Kullandığımız parametre olarak giriş mat nesnesi, işlem sonucunu atamak için çıkış mat nesnesi ve yapılandırma için bir nesne almaktadır. Bu nesne yapısal element olarak adlandırılır (Structuring Element) ve yayma işleminin şeklini belirler. Yapısal elementin merkez noktası üzerine giriş görüntüsünün pikselleri bu noktaya oturtularak oluşturulur. 

*Python:*
```Python
import cv2
import numpy as np

frame = cv2.imread('resim.png',0)
#Numpy ile kernel matris tanımı
kernel = np.ones((5,5),np.uint8)
#Aşındırma işlemi
sonuc = cv2.erode(frame,kernel,iterations = 1)
cv2.imshow("Sonuc", sonuc)
cv2.waitKey(0)
```

![morfolojik görüntü işleme](https://4.bp.blogspot.com/-yG3ePxI1-JE/Vuc48S4lXGI/AAAAAAAAATk/4Wt3CmxdymkqdwqJJyjSFu4BIGlKAgJNg/s1600/A1ds%25C4%25B1z.png)



**Dilation (Yayma – Genişletme)**

Bu operatör giriş olarak verilen görüntü üzerinde parametreler ile verilen alan içerisindeki sınırları genişletmektedir, bu genişletme sayesinde piksel gurupları büyür ve pikseller arası boşluklar küçülür. 

Morfolojik operatörlerin iki girişi vardır:
1. Yayılacak imge,
2. Yayma işleminin şeklini belirleyen yapı elemanı (structure element).

- Z2 uzayında verilen A ve B kümeleri için yayma işlemi aşağıdaki gibi
tanımlanmaktadır:

![yayma operatörü](https://miro.medium.com/v2/resize:fit:680/1*nzC4JId4M_rVBj3s4zO_1g.png)

B': B'nin bire tümleyeni
A: işlenecekimge 
B: yapıelemanı


*Python:*
```Python
import cv2
import numpy as np

frame = cv2.imread('resim.png',0)
#Numpy ile kernel matris tanımı
kernel = np.ones((15,15),np.uint8)
#Aşındırma işlemi
sonuc = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("Sonuc", sonuc)
cv2.waitKey(0)
```

![dilation](https://miro.medium.com/v2/resize:fit:1166/1*jVooxf95UaF9TyQ0H3RkOA.png)


**Opening (Açınım)**

Erosion ve dilation operatörlerinin görüntü üzerine birlikte uygulanması ile gerçekleşir.  Öncelikli olarak erosion operatörü uygulanır ve ardından dilation operatörü uygulanır.

*Python:*

```Python
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernelMat)
```

![opening](https://images.slideplayer.biz.tr/33/10376906/slides/slide_45.jpg)


**Closing (Kapanım)**
Görüntüye dilation operatörü uygulanır ve ardından Erosion operatörü uygulanır.

*Python:*
```Python
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernelMatris)
```

![closing](https://slideplayer.biz.tr/slide/10376906/33/images/48/Kapanım+örnek.jpg)



![dilation](https://docplayer.biz.tr/docs-images/39/19573325/images/2-0.png)



**Gradyan**

Dilation ve Erosion operatörü arasındaki farktır. Nesnelerin ana hatlarını belirlemek için kullanılır. Sınır çizgilerini tam hatlarıyla belirlemek için yapısal element, görüntüye göre özelleştirilmelidir. 


*Python:*
```Python
morfolojik_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernelMatris)
```



## Thresholding (Eşikleme)

Giriş olarak verilen görüntüyü ikili görüntüye çevirmek için kullanılan bir yöntemdir. İkili görüntü (binary), görüntünün siyah ve beyaz olarak tanımlanmasıdır. Morfolojik operatörler gibi görüntü üzerindeki gürültüleri azaltmak veya nesne belirlemek gibi farklı amaçlar için kullanılır. Giriş olarak verilen görüntü üzerinde uygulanan thresholding tipine bağlı olarak, pikselleri verilen eşik değerine göre siyah ya da beyaz olarak günceller.

OpenCV içerisindeki sık kullanılan eşikleme tipleri:

 * THRESH_BINARY
 * THRESH_BINARY_INV
 * THRESH_TRUNC
 * THRESH_TOZERO
 * THRESH_TOZERO_INV


 Thresholding işlemi için threshold()metodunu kullanacağız. Bu metot beş adet parametre almaktadır. 
 Kaynak mat nesnesi yani giriş görüntüsü, hedef olarak ikinci bir mat nesnesi bu hedef nesne işlem sonucunu tutmak için, thresh olarak adlandırılan parametre eşik değeri, THRESH_BINARY ve THRESH_BINARY_INV gibi tipler için kullanılmak üzere maksimum değer ve yukarıda belirtilenler gibi threshold tipini parametre olarak almaktadır.


*Python:*
```Python
hedefMat = cv.threshold(kaynakMat,esikDegeri,maxDeger,cv.threshoidngTipi)
```


THRESH_BINARY:

Kaynak olarak alınan görüntü üzerindeki piksel, esikDegeri olarak verilen değerden büyükse maksDeger olarak verilen parametre değerine atanır.

 
THRESH_BINARY_INV:

Kaynak olarak alınan görüntü üzerindeki piksel, esikDegeri olarak verilen değerden küçükse maksDeger olarak verilen parametre değerine atanır. THRESH_BINARY_INV, THRESH_BINARY‘nin karşıtı olarak kullanılabilir.


THRESH_TRUNC:

Kaynak olarak alınan görüntü üzerindeki piksel,


THRESH_TOZERO:

Kaynak olarak alınan görüntü üzerindeki piksel,sınır olarak verilen değerden büyük olması durumunda piksel değeri korunacak, küçük olması durumunda ise piksel siyah olarak atanacaktır.

 
THRESH_TOZERO_INV:

Kaynak olarak alınan görüntü üzerindeki piksel,sınır olarak verilen değerden küçük olması durumunda piksel değeri korunacak, büyük olması durumunda ise piksel siyah olarak atanacaktır.



![thresholding](https://i0.wp.com/theailearner.com/wp-content/uploads/2019/07/thres_types.png?
resize=625%2C491&ssl=1)


![th](https://media5.datahacker.rs/2019/09/thresholding.jpg)

 