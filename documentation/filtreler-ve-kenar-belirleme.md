# Filtreleme ve Kenar Belirleme Algoritmaları

**Filtreleme:**

Filtre konusuna geçmeden önce öncelikli olarak gürültü kavramına bakmakta fayda var. Gürültü; hareket veya atmosferik kararsızlık nedeniyle meydana gelen bulanıklaşma veya resmi çekerken yanlış ışık etkisinden dolayı focus bulanıklaşması, kusursuz olmayan lenslerden kaynaklanan geometrik bozulma ve elektronik kaynaklardan gelen hatalar olarak verilebilir.

Filtreler genellikle ön işlem veya gürültü temizleme için kullanılırlar. Temel olarak görüntüyü bir fx fonksiyonuna sokararak filtre sabitini kullanır bu sayede görüntü üzerinde yer alan piksel değerlerinde bazı değişiklikler meydana gelir, sonuç olarak görüntü değişime uğrar. 

Instagram, mobil fotoğraf düzenleme uygulamaları veya profesyonel görüntü düzenleme programlarında filtrelere rastlamışsınızdır. Bundan önceki ilk iki konuda ele alınan örneklere dikkat ederseniz çıktı olarak oluşturulan görsellerde bazı piksellerin kaydığını, silik çıktığını veya tam olarak temizlenemediğini görürsünüz. Farklı görseller ile bu örnekleri yaptıysanız benzer sonuçlarla karşılaşmışsınızdır. Bunun nedeni kaynak olarak alınan görüntünün gürültülü olması veya ışık dengesinin bozuk olması gibi birçok durumdur. 
Bu sorunları aşmak için kaynak görüntüye öncelikle bir filtre uygulanır ve görüntünün
işleme için en verimli hale getirilmesi sağlanır ve bu durum ön işleme olarak adlandırılır.


![filters](https://www.researchgate.net/publication/37394153/figure/fig3/
AS:669375770140693@1536603028535/Performance-of-Median-filter-in-the-presence-of-AWGN-a-Original-Test-Image-Lena-face.png)

**Blur**

Blur filtresi görüntüyü bulanıklaştırmak için kullanılır. Uygulamak için ise blur() metodu kullanılır. Bu metot parametre olarak kaynak görüntü mat nesnesi tipinde, mat tipinde bir sonuç ve Size tipinde uygulanacak olan bulanıklık değerini almaktadır.(çekirdek boyutu olarak da adlandırılır).

*Python:*
```Python
hedefGoruntu = cv2.blur(kaynakGoruntu,(50,50))
```


**GaussianBlur**

GaussianBlur filtresi görüntü üzerinde düzleştirme işlemi uygular. Uygulamak için GaussianBlur() metodu kullanılır. Bu metot parametre olarak kaynak görüntü mat nesnesi tipinde, mat tipinde bir sonuç ve Size tipinde uygulanacak olan bulanıklık değerini (çekirdek boyutu olarak da adlandırılır) ve SigmaX olarak adlandırılan çekirdek standart sapmasıdır almaktadır.

*Python:*
```Python
hedefGoruntu = cv2.GaussianBlur(kaynakGoruntu,(100,100),0)
```

![Gblur](https://miro.medium.com/max/1400/1*gfW1y8c6a-ys3XF9xEnjqw.png)


**Laplace**

Görüntü üzerinde nesnelerin sınır çizgilerini belirlemek için kullanılır. Piksellerin renk farklılıklarından yararlanır ve bu sayede nesnelerin sınır çizgileri tespit edilmiş olur. Uygulamak için Laplacian() metodu kullanılır. Bu metot parametre olarak kaynak görüntü mat nesnesi tipinde, mat tipinde bir sonuç ve int tipinde derinlik değeri almaktadır.

*Python:*
```Python
hedefGoruntu = cv2.Laplacian(kaynakGoruntu,cv2.CV_64F)
```


**Sobel**

Görüntü üzerindeki kenarları elde etmek için kullanılır. Görüntü üzerindeki nesneleri kenarları belirleyerek ayrıştırmak istendiğinde bu filtreden yararlanılır.  Uygulamak için Sobel() metodu kullanılır. Bu metot parametre olarak kaynak görüntü mat nesnesi tipinde, mat tipinde bir sonuç, int olarak çıkış görüntü nesnesi için derinlik ve int tipinde türev olarak adlandırılan x, y değeri.

*Python:*
```Python
cikisGoruntu = cv2.Sobel(girisGoruntu,cv2.CV_8U,1,0,ksize=5)
```


![filters](https://www.bogotobogo.com/python/OpenCV_Python/images/EdgeDetect/SanFrancisco_out.png)



# Kenar Belirleme

Görüntü üzerinde kenar tespiti yapmak; o görüntüdeki nesneleri tespit etmek, saymak ve özelliklerini belirlemek amacıyla kullanılabilir. Kenar belirleme algoritmaları en temel anlatımıyla, görüntü üzerindeki piksellerin renk değerlerinin bir birlerinden farklılaşması ile belirlenir.

![edge](https://mesutpiskin.com/blog/wp-content/uploads/2017/04/edge_detection.png)

Yukarıdaki görsele baktığınızda farklılaşmanın nereden başladığını tahmin edebilir misiniz? 
Gördüğünüz üzere 4 ve 152 numaralı matris elemanları arasında keskin bir renk geçişi olmuş, bu renk geçişi (gürültü olmadığı taktirde) iki farklı nesnenin başlangıç ve bitiş çizgilerini ifade edebilir. İşte bu geçişler bizim için kenar çizgilerini ifade etmektedir. 
Örnek matrisimiz görüldüğü üzere gri (Gray) renk uzayına sahip bu renk uzayında matris elemanları yani pikseller 0-255 arasında renk değerlerine sahipti eğer görüntümüzü siyah-beyaz renk uzayına çevirir ve 0-1 aralığında renk kodları alması işimizi kolaylaştırmaz mı? İşte bu noktada kenar çıkarımı yapmadan Thresholding (Eşikleme) yapmamız işe yarayabilir. Bu uygulama şeklinde her algoritma kendisine has çıkarımlar yaparak tespit edebilir, bu yüzden görüntümüz de hangisinin daha iyi sonuç verdiğini deneyerek göreceğiz. 

![edge](https://miro.medium.com/v2/resize:fit:1400/1*3hDhkzqJStXTp37lS_M5aA.png)

Başlıca kenar belirleme algoritmaları:
* Canny
* Sobel
* Prewitt
* Lablacian
* Zero-Cross

Bu algoritmalar içerisinden Canny algoritması verdiği başarılı sonuçlar neticesinde en sık kullanılandır.

.Canny(input_mat, detected_edges_mat, lowThreshold, maxThreshold, kernel_size )

- input mat kenar tespiti yapacağımız matrisimiz, detected_edges_mat işlem sonucu kenarları tespit edilmiş mat nesnemiz, eşikleme yani thresholding yapacağımız için istediğimiz minimum değeri , maxThreshold ise eşikleme için kullanılmasını istediğimiz maksimum eşik değeri, kernel_size  parametresi ise çekirdek matrisi tanımlamaktadır bu rada önerilen matris değerlerini kullanabilir özel matris oluşturabilir istersek de boş bırakarak varsayılan çekirdek matrisin kullanılmasını sağlayabiliriz.

![edge detection](https://ars.els-cdn.com/content/image/1-s2.0-S0888327017304399-gr4.jpg)

**Canny:**

``` Python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('mevlana.jpg',0)
edges = cv2.Canny(img,50,150)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Orjinal'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()
```


![filters](https://circuitdigest.com/sites/default/files/inlineimages/u1/Edge-Detection-Methods-using-OpenCV.png)
