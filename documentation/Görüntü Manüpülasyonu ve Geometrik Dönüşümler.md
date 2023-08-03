# Görüntü Manüpülasyonu ve Geometrik Dönüşümler

Görüntü işleme süreci verilerin bilgisayarlar tarafından tanınmasıyla başlar. Görüntü formatındaki veri için öncelikle matris oluşturulur. Resimdeki her bir piksel değeri bu matrise işlenir. Sonuç olarak 200 x 200 boyutundaki bir resim için 200 x 200 boyutunda bir matris oluşturulur. Eğer bu resim renkli ise bu boyut 200x200x3 halini alır (RGB). Görüntü işleme sürecinde yapılan her manipülasyon aslında bir matris işlemidir. Örnek olarak verdiğimiz 200x200 boyutundaki resim üzerinde bir bulanıklaştırma işlemi yapılmak istendiğini varsayalım. Burada belirli bir filtre bütün matris üzerinde gezerek matris elemanlarının tamamının veya bir kısmının üzerinde işlem yapar. Bu işlem sonucunda resmin istenen bölümü veya tamamı bulanık bir hale gelir. Bu durum diğer görüntü işleme süreçleri için de geçerlidir.

Örnek olarak bazı projelerde bu verilerin renkli olmasının eğitime bir etkisi yoktur. Bu gibi durumlarda eğitimi renkli resimler ile gerçekleştirmek, eğitimin daha yavaş ve daha düşük performans ile yapılmasına sebebiyet verir.

Resimlerdeki kalitenin artırılması, görüntüler üzerinde restorasyonlar yapılması, gürültülerin temizlenmesi gibi bir çok işlem görüntü işleme süreçlerinin içerisinde yer almaktadır.




**Piksel Manüpülasyonu**

Piksel kavramı hakkından daha önce bahsetmiştik, pikseller mat nesnesi içerisindeki dizi elemanlarına karşılık gelmektedir. Bir görüntü üzerinde işlem yapmak istediğimizde dizideki elemanları kullanmamız gerekmektedir. OpenCV içerisinde yer alan birçok metot piksel işlemlerini kendisi yapmaktadır. 
Örneğin bir görüntüyü kopyalamak istediğimizde copy metodunu kullanabiliriz fakat bu metotların nasıl çalıştığını anlamak için veya kendi algoritmanızı geliştirmek zorunda kaldığınızda bu bilgiler işinize yarayacaktır. Basit bir uygulama yazalım ve bu uygulama kameradan okunan görüntüyü mat nesnesi içerisinde tutalım ve bu nesneyi bir başka mat nesnesi içerisine kopyalayarak dosya sistemine kaydedelim. Bu örnek ile bir piksele nasıl ulaşabileceğimizi de öğrenmiş olacağız.

```python
import cv2
import numpy as np

def main():
    cv2.loadLibrary(cv2.Core.NATIVE_LIBRARY_NAME)
    imageArray = cv2.Mat()
    videoDevice = cv2.VideoCapture()
    videoDevice.open(0)

    if videoDevice.isOpened():
        _, imageArray = videoDevice.read()
        videoDevice.release()
    else:
        print("Video aygıtına bağlanılamadı.")
        return

    # Okunan görüntüyü kopyalamak için yeni bir mat nesnesi
    newimageArray = cv2.Mat()

    # Yeni nesnenin satır ve sutun sayısını alınan görüntünün satır sutun sayısına eşitliyoruz
    # create  metodu ile oluşturakacaj nat nesnesinin satır ve sütünunu veriyoruz.
    newimageArray.create(imageArray.rows(), imageArray.cols(), cv2.CvType.CV_8UC1)

    # Döngü ile alınan görüntü dizisinin tüm elemanları arasında dönüyoruz
    for i in range(imageArray.rows()):
        for j in range(imageArray.cols()):
            # put ile verilen indise yani piksele değer atanır
            # get ile verilen indisdeki piksel değeri okunur
            newimageArray.put(i, j, imageArray.get(i, j))

    cv2.Imgcodecs.imwrite("KopyaGoruntu.jpg", newimageArray)
    print("Görüntü dosya sistemine yazıldı.")

if __name__ == "__main__":
    main()

```

Bir piksele yani dizi elemanına erişmek için get() metodu, belirli indisteki bir piksele değer yazmak için ise set() metodu kullanılır.

Doğrudan hedef pikselin RGB değerlerini bu şekilde alabilir veya değiştirebiliriz. Unutmamanız gerek bir nokta ise OpenCV de RGB kodları BGR olarak tersen kullanılmaktadır, yani 255 255 0 sarı değerini atamak için 0 255 255 şeklinde tanımlamalıyız, aynı şekilde rgb kodunu çağırdığımızdada 0 255 255 olarak gelecektir.


```python
import numpy as np

# varsayılan bir dizi oluştur
rgb = np.array(matNesnesi.get(300, 200))

# Renk kodlarını bu dizide tutulmaktadır
r, g, b = rgb[0], rgb[1], rgb[2]

# 255 255 0 RGB kodunu bu 222 333 pikseline atar
matNesnesi.put(222, 333, np.array([255, 255, 0]))

```
RGB yerine farklı bir renk uzayı kullanılmışsa get metodu o renk uzayının renklerini döndürür. Örneğin siyah beyaz renk uzayına sahip bir görüntü ise, get metodu sonucunda 2 elemanlı bir double dizi oluşacaktır.


Mat sınıfı OpenCV'nin en temel sınıflarından birisidir. Genel olarak imread() ile okuduğumuz resimleri tuttuğumuz sınıflardır. 1, 2 ve 3 boyutlu diziler olarak düşünülenilir.
![Mat matris](/Users/zeynepdemirtas/Documents/GitHub/Computer_Vision_OpenCV/documentation/matris.png)



Bir görüntü üzerindeki beyaz pikselleri siyah olarak değiştirelim. Öncelikli olarak görüntüyü okuyup, tüm pikseller içerisinde dönerek RGB renk değeri beyaz yani 255,255,255 olanları bulup RGB siyah yani 0,0,0 ile değiştireceğiz. 

```python
import cv2
import numpy as np

 
frame = cv2.imread("car.jpeg")
#nump ile frame matrisi üzerinde kolayca karşılaştırma ve değer değiştirme yapabiliyoruz
frame[np.where((frame == [255,255,255]).all(axis = 2))] = [0,0,0]
#yeni görüntüyü kaydedelim
cv2.imwrite("car-output.jpeg", frame)

```



**Resim Boyutlarını Değiştirme**

Opencv ile görüntülerin boyutlarını değiştirebiliriz. İlk olarak shape methodunu kullanarak okuduğumuz resmin boyutunu öğrenebiliriz. 
Sonrasında bu boyutu birkaç şekilde değiştirebiliriz. Bu değişiklikleri OpenCV içerisinde bulunan resize methodu ile gerçekleştiririz. Bu fonksiyon içerisine ilk olarak boyutunu değiştirmek istediğimiz resmi sonrasında da yeni boyutları istemektedir.

```python
resminBoyutu = image.shape

img =cv2.resize(image,(1300,275))

```


OpenCV üzerinde resimlerin yönünü de değiştirebiliriz. Bu değişimi yapmak için flip methodunu kullanırız. Bu method içerisine ilk olarak değiştirmek istediğimiz resmi sonrasında da hangi eksende döndürmek istediğimizi girmemizi gerektirir.

```python
new_img = cv2.flip(new_img,0)

```
- 0: X ekseni Etrafında
- 1: Y ekseni Etrafında
- -1: Hem X hem Y ekseni Etrafında

