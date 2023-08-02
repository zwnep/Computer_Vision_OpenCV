import cv2

#image tresholding - görüntü eşikleme
#(nesneleri izole etmek için)
#Giriş olarak verilen görüntü üzerinde uygulanan eşikleme tipine bağlı olarak, pikselleri verilen eşik değerine göre siyah ya da beyaz olarak günceller.

#Giriş olarak verilen görüntüyü ikili görüntüye çevirmek için kullanılan bir yöntemdir.
#İkili görüntü (binary), görüntünün siyah ve beyaz olarak tanımlanmasıdır.
#Morfolojik operatörler gibi görüntü üzerindeki gürültüleri azaltmak veya nesne belirlemek gibi farklı amaçlar için kullanılır. Giriş olarak verilen görüntü üzerinde uygulanan thresholding tipine bağlı olarak, pikselleri verilen eşik değerine göre siyah ya da beyaz olarak günceller.

#Küresel eşik algoritmaları, giriş olarak bir kaynak görüntü (src) ve bir eşik değeri (thresh) alır ve 
#kaynak piksel konumundaki (x,y) piksel yoğunluğunu eşik ile karşılaştırarak bir çıktı görüntüsü (dst) üretir.
#Src(x,y) > thresh ise, dst(x,y)'ye bir değer atanır. Aksi takdirde dst(x,y)'ye başka bir değer atanır.

#Küresel(Global) eşiklemenin en basit biçimine İkili(Binary) Eşik Tutma denir.

#Kaynak görüntüye (src) ve eşik değerine (thresh ) ek olarak, maksimum değer (maxValue) adı verilen başka bir giriş parametresi alır.

#Her piksel konumunda (x,y), o konumdaki piksel yoğunluğu bir eşik değeri olan harmanla karşılaştırılır.

#src(x,y) harmandan büyükse, eşikleme işlemi hedef görüntü pikseli dst(x,y) değerini maxValue olarak ayarlar.


srcImage = cv2.imread("thresholdingImage.jpeg", cv2.IMREAD_GRAYSCALE)

thresh = 0
maxValue = 255
 
th, dst = cv2.threshold(srcImage, thresh, maxValue, cv2.THRESH_BINARY)

#Ters İkili Eşik, İkili Eşik Tutmanın tam tersidir.
	
#threshold(src,dst, thresh, maxValue, THRESH_BINARY_INV)
