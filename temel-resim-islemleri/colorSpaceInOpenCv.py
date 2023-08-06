import cv2
import numpy as np

#OpenCV’de 150'den fazla renk uzayı dönüştürme yöntemi bulunmaktadır.
# En popüler renk uzaylarından bazıları RGB nam-ı diğer BGR, YUV, HSV…

#RGB, renklerin Kırmızı, Yeşil ve Mavi değerlerinin doğrusal bir kombinasyonu ile elde edildiği ilave bir renk uzayıdır.
#Üç kanal da, yüzeye çarpan ışık miktarı ile ilişkilidir.

#HSV renk uzayı, 1970′ lerde RGB renk uzayına alternatif olarak için geliştirilmiştir.
# Özellikle görüntü tanıma uygulamalarında bazı durumlarda RGB’ den daha iyi sonuçlar alınmaktadır.

#HSV, bazı kaynaklarda HSB veya HSL olarak da geçer ve Hue, Saturation ve Value kelimelerinin baş harflerini ifade eder.
#Hue: Renk özünü ifade eden sayısal değer.
#Saturation: H ile seçilmiş olan rengin doygunluğunu ifade eden sayısal değer.
#Value (Brightness, Lightness): Parlaklığı ifade eden sayısal değer.

#HSV renk uzayının birçok kullanımında H değeri 0 – 255 aralığında, S ve V değerleri 0 – 100 aralığında seçilir.
# Ancak OpenCV’ de durum farklıdır. OpenCV; H değerini 0 – 179 aralığında, S ve V değerlerini 0 – 255 aralığında tutar.

#Normalde Opencv kütüphanesinde 150’den fazla renk uzayı değiştirme fonksiyonu mevcuttur fakat şuan biz temel olarak iki tane fonksiyonumuzdan bahsedelim.
#Birincisi cv2.cvtColor yani açılımı “convert color” da denebilir. Aldığı input görüntümüzün ismi ve değiştirilmek istenen renk uzayının ismidir.
#Diğer fonksiyonumuz ise cv2.inRange fonksiyonudur, bu foksiyonumuz ise girilen değerler arasındaki renkleri seçmeye yarar.
#Mesela mavi rengin taban ve tavan renklerini girersek fonksiyona, kolaylıkla mavi rengi görüntümüz arasından seçebiliri



#Renk uzayları arasında dönüştürmek için cvtColor fonksiyonunu kullanıyoruz.
#İlk argüman giriş görüntüsüdür ve ikinci argüman renk alanı dönüşümünü belirtir.


original = cv2.imread("brightAndDarkCupe.webp")
bright = cv2.imread("brightCupe.jpeg")

brightAndDarkLAB = cv2.cvtColor(original,cv2.COLOR_BGR2LAB)

brightAndDarkYCB = cv2.cvtColor(original,cv2.COLOR_BGR2YCR_CB)

brightAndDarkHSV = cv2.cvtColor(original,cv2.COLOR_BGR2HSV)


cv2.imshow("original",original)
cv2.imshow("lab",brightAndDarkLAB)
cv2.imshow("ycb",brightAndDarkYCB)
cv2.imshow("hsv",brightAndDarkHSV)


#renk uzaylarınnın örnek bir kullanımı
#yeşil rengin tespiti 

#Yeşil piksele yakın değerlere sahip tüm pikselleri görüntüden çıkarın.
#Her bir renk alanı için +/- 40 aralığı alabilir ve sonuçların nasıl göründüğünü kontrol edebiliriz.
#Yeşil piksellerin maskesini bulmak için inRange opencv işlevini kullanacağız ve 
#ardından maskeyi kullanarak görüntüden yeşil pikselleri almak için bitwise_and işlemini kullanacağız.
#Ayrıca, bir pikseli başka bir renk uzayına dönüştürmek için önce 1B diziyi 3B diziye dönüştürmemiz gerektiğini unutmayın.


#Amacımız bir görüntü alıp yeşil rengi ayırt etme ve yeşil olmayan yerleri karartma uygulaması yapalım.
#Adım adım;
#Görüntümüzü aldık
#Renk uzayını RGB’den HSV’ye çevirdik
#Yeşil rengimiz için eşik değerlerini girdik (mask’leme işlemi)
#Artık Yeşil renkli objemizle üzerinde istediğimiz gibi işlemimizi yapabiliriz.

bgr = [40,155,68]
thresh = 30

minBGR = np.array([bgr[0] - thresh,bgr[1] - thresh,bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh,bgr[1] + thresh,bgr[2] + thresh])

maskBGR = cv2.inRange(bright,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(bright,bright,mask=maskBGR)

cv2.imshow("Result BGR",maskBGR)

b,g,r = cv2.split(bright)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
















cv2.waitKey(0)
cv2.destroyAllWindows()