# Renk Uzayları, Renk Uzayı Dönüşümü ve Histogram

Renk Uzayı: Renk çeşitliliğinin fazla olması nedeniyle bu renkleri gruplama ihtiyacı doğmuştur bu renkleri gruplamak ve standartlaştırmak için renk uzayı (color space) kavramı ortaya çıkmıştır. Her renk uzayı, renk kümesini tanımlamak için kendine özgü bir yapıya sahiptir. 
Örneğin siyah beyaz bir görüntüyü dijitalleştirmek için çok fazla kavrama gerek yoktur. Görüntü siyah ve beyaz olmak üzere 2 adet değişkene sahiptir. 300×300 boyutunda dijital siyah beyaz bir görüntü dijitalleştirilip renklendirilirken, 300×300 boyutunda bir dizi oluşturulur. Renklendirme işlemi için ise 2 adet değişken olduğu için 1 ve 0 yeterlidir. Fakat renkli bir resim üzerinde farklı renk tonları olacağı için 1 ve 0 ile bu görüntüyü tanımlamak yetersiz olacaktır. Bu farklı durumlar için çeşitli renk uzayları belirlenmiştir. 


![renk uzayları](https://1.bp.blogspot.com/-pNj_pUFmodc/U4YWumkGbOI/AAAAAAAADRk/-0Lgpyd3TPA/s1600/2.png)



**RGB Renk Uzayı:**
Bu renk uzayı Red Green Blue yani kırmızı, yeşil ve mavi renklerin baş harfi ile adlandırılmıştır. Renkler bir küp olarak tanımlanır bu tanımla sayesinde 3 değişkenli bir dizi elde edilir. Bu dizi elemanları olan hücreler yani pikseller, bir rengi tutabilmek için 3 renk olan kırmızı, yeşil ve mavinin belirli yoğunlukta karıştırılması ile elde edilen renk kodunu tutarlar.

![renk uzayı-rgb](https://mesutpiskin.com/blog/wp-content/uploads/2016/05/19.jpg)


**HSV Renk Uzayı:**
HSV Hue, Saturation, Value yani renk özü, doygunluk ve parlaklık olarak adlandırılmıştır. Anlaşıldığı üzere renk tanımlamalarını bu üç kavrama göre gerçekleştirir.

![renk uzayı-hsv](https://mesutpiskin.com/blog/wp-content/uploads/2016/05/19.jpg)


**CMYK Renk Uzayı:**
Cyan, Magenta, Yellow, Key rengin kısaltmasıdır. Buradaki key siyah rengi temsil etmektedir. CMYK renk uzayı, dijital renk tanımlamaları için belirtilen bu dört rengi karıştırarak yapmaktadır.

![renk uzayı-cmyk](https://malatyareklam.net/wp-content/uploads/2020/05/cmyk-vs-rgb-1-1.png)


**YUV Renk Uzayı:**
Y Luminance, U Chrominance1, V Chrominance2 kısaltmasıdır. Y siyah – beyaz U ve V ise mavi tabanlı renklilik ve kırmızı tabanlı renkliliği temsil eder. Renkler bu üç kavram ile temsil edilerek oluşturulurlar.

![renk uzayı-yuv](https://mesutpiskin.com/blog/wp-content/uploads/2016/05/23.jpg)


# Renk Uzayı Dönüşümü
OpenCV ile bu renk uzayları arasında dönüşüm işlemleri için cvtColor() metodu bulunmaktadır. cvtColor metodu parametre olarak iki adet mat nesnesi ve dönüşüm yapılacak olan renk uzayını almaktadır.

Code: Kaynak Renk Uzayı 2 Hedef Renk Uzayı

COLOR_RGB2BGR
COLOR_RGB2BGRA
COLOR_RGB2GRAY
COLOR_GRAY2RGB
OLOR_RGB2HLS
OLOR_HSV2RGB
OLOR_RGB2HSV
OLOR_RGB2Luv
COLOR_HSV2RGB
COLOR_RGB2YUV
COLOR_RGB2Lab



# Histogram ve Histogram Eşitleme

Histogram matematikdeki temel kavramlardan birtanesidir. Matematiksel tanımı: "Ölçülen bir istatistiksel sayısal değişkene, belirli değer aralıklarında kaçar kez rastlandığını gösteren grafik." Görüntü işlemedeki tanımıda çok farklı değildir. Görüntü matrisi üzerindeki her pixel değerinin görüntünün tamamındaki miktarıdır. Gri renk uzayına sahip̧ bir görüntüde (2 boyutlu bir matris) 0 dan 255’e kadar olan tonların görüntüde kaç adet bulunduğunu gösteren, görüntüdeki tüm bu piksellerin ışık değerleri ile x ekseninde ve y ekseninde pikseller ile oluşturulmuş çubuk grafiktir. RGB renk uzayına sahip renkli görüntülerde ise doğrudan bir histogram hesaplamak yerine Red-Green-Blue uzayları için kendi aralarında ayrı ayrı histogram hesaplanır, istenilirse RGB renkler 2 boyutlu bir matris gibi hesaplanır ve sonuçta oluşacak görüntü 2 boyutlu bir matrisin histogramını ifade edecek hale gelir.

Histogram eşitleme ile, sonuç olarak elde ettiğiniz grafiğe göre bir aralık seçmek; çok yüksek (yani fazla sayıda) olan matris değerlerini düşürerek, çok az olan matris değerlerini ise yükselterek görüntü üzerinde iyileştirme yapmaktır.


![renk uzayları](https://guzelemre.files.wordpress.com/2017/11/7.png)


# Histogramı Neden Kullanırız?

Düşünün elinizde bir fotoğraf var ve çok parlak çıkmış bu parlaklığı nasıl azaltırdınız? Histogram'dan yararlanarak parlak alanları bulabilir ve bu matrisleri bir alt seviyeye indirerek parlaklığı azaltabilirz. TV, Monitör vb. cihazlarda yer alan contrast ayarı (karşıtlık) hitogram kullanarak yapılmaktadır. Bunlar gibi bir çok örnek verilebilecek uygulama alanları mevcuttur.
