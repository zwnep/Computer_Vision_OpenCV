import cv2
import numpy as np

# Neden bir görüntüyü blur hale getirmek isteriz?
# Çünkü bir görüntüdeki belirli gürültü türlerini azaltır. Bu nedenle bulanıklaştırmaya genellikle yumuşatma denir.

# Dikkat dağıtıcı bir arka planı kaldırmak için, mobil cihaz kameralarında “Portre” modunda yapıldığı gibi,
# bir görüntünün bölümlerini kasıtlı olarak bulanıklaştırabilirsiniz.

# Bir özdeş(Identity Kernel) matrisi özel yapan şey, onu başka herhangi bir matrisle çarpmanın orijinal matrisi döndüreceğidir.

image = cv2.imread("agac.jpeg")

identityKernel = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]])

# filter2D(src, ddepth, kernel)
# İlk argüman kaynak görüntüdür
# İkinci argüman, ortaya çıkan görüntünün derinliğini gösteren ddepth'dir. -1 değeri, son görüntünün de kaynak görüntüyle aynı derinliğe sahip olacağını gösterir.
# Son giriş argümanı, kaynak görüntüye uyguladığımız çekirdektir.

identity = cv2.filter2D(image, ddepth=-1, kernel=identityKernel)

cv2.imshow("Original", image)
cv2.imshow("Identity", identity)


# blurring an image
kernelBlur = np.ones((5, 5), np.float32) / 25
#neden 25'e böldük? 5x5 boyutlu çekirdek kullanıldığı içinher pikselin rengi, içinde bulunduğu 
#5x5'lik çekirdek matrisin içersinde yer alan ve birbiriyle komşu olan 25 pikselin renk ortalamasıyla değiştirilir.
#Dolayısıyla renkler keskinliğini kaybederek ortalama değerlere doğru kayar.
#Kerneol boyutları büyüdükçe bulanılık yoğunlaşır.

img = cv2.imread("masaüstü.jpeg")
imgBlur = cv2.filter2D(img, ddepth=-1, kernel=kernelBlur)

cv2.imshow("original", img)
cv2.imshow("blur", imgBlur)


#OpenCV fonk. ile bulanıklaştırma
#OpenCV'nin yerleşik blur() işlevini kullanarak bir görüntüyü de bulanıklaştırabiliriz.
#Esasen bir kolaylık işlevi, özellikle bir çekirdek tanımlamanıza gerek olmayan görüntüleri bulanıklaştırmak için kullanın.
#Aşağıdaki kodda gösterildiği gibi ksize input bağımsız değişkenini kullanarak çekirdek boyutunu belirtmeniz yeterlidir.
#Bulanıklaştırma işlevi daha sonra dahili olarak 5×5 bulanıklık çekirdeği oluşturacak ve bunu kaynak görüntüye uygulayacaktır.

imageBlurFonk = cv2.blur(img,ksize=(5,5))

cv2.imshow('Original', img)
cv2.imshow('Blurred', imageBlurFonk)


#Gaussian Blurring

#Bu teknik, ilk örnekte açıklanan düzgün ortalamanın aksine, ağırlıklı bir ortalama gerçekleştiren bir Gauss filtresi kullanır. 
#Bu durumda, Gauss bulanıklığı, çekirdeğin merkezinden olan mesafelerine bağlı olarak piksel değerlerini ağırlıklandırır. 
#Merkezden daha uzaktaki pikseller, ağırlıklı ortalama üzerinde daha az etkiye sahiptir. 

#GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])

#İlk argüman olan src, filtrelemek istediğiniz kaynak görüntüyü belirtir.
#İkinci argüman, Gauss çekirdeğinin boyutunu tanımlayan ksize'dır. Burada 5×5 çekirdek kullanıyoruz.
#Son iki argüman, her ikisi de 0 olarak ayarlanmış olan sigmaX ve sigmaY'dir. Bunlar, X (yatay) ve Y (dikey) yönde Gauss çekirdeği standart sapmalarıdır. 
#SigmaY'nin varsayılan ayarı sıfırdır. SigmaX'i sıfıra ayarlarsanız, standart sapmalar çekirdek boyutundan (sırasıyla genişlik ve yükseklik) hesaplanır.
#Ayrıca, her bağımsız değişkenin boyutunu sıfırdan büyük pozitif değerlere açıkça ayarlayabilirsiniz.

gaussian_blur = cv2.GaussianBlur(img, ksize=(5,5),sigmaX=0, sigmaY=0)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blurred', gaussian_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()
