import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

path = "agac.jpeg"
img = cv2.imread(path)

#cvtColor(): Görüntüyü bir renk uzayından diğerine dönüştürür. 
#OpenCV’de 140 dan fazla dönüşüm metodu vardır. 
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#GaussianBlur filtresi görüntü üzerinde düzleştirme işlemi uygular.
#.GaussianBlur(kaynakGoruntu, hedefGoruntu, new Size(100,100),0);
#r. Bu metot parametre olarak kaynak görüntü mat nesnesi tipinde, mat tipinde bir sonuç ve Size tipinde uygulanacak olan bulanıklık değerini (çekirdek boyutu olarak da adlandırılır) ve SigmaX olarak adlandırılan çekirdek standart sapmasıdır almaktadır.
imgBugu = cv2.GaussianBlur(img,(5,5),5)

#Canny() fonksiyonu temel olrak piksellerin renk farklılaşmasından yararlanarak kenra tespiti yapmakta
imgCanny = cv2.Canny(img,100,100)

#dilate(): verilen görüntü üzerinde parametreler ile verilen alan içerisindeki sınırları genişletmektedir, 
#bu genişletme sayesinde piksel gurupları büyür ve pikseller arası boşluklar küçülür. 
#Görüntünün üzerinde kutucuk dolaştırarak sağlanır. Fakat beyaz yerleri inceltmek yerine kalınlaştırır.
#(işlem yapılacak görüntü, görüntünün üzerinde hareket edecek kutucuk ve ”iterations” değerini) alır. Bu “iterations” değeri, görüntüye kaç kez genişleme uygulanacağını belirler.
imgGen = cv2.dilate(imgCanny,kernel,4)


cv2.imshow("original",img)
cv2.imshow("gray",imgray)
cv2.imshow("bugulu",imgBugu)
cv2.imshow("canny",imgCanny)
cv2.imshow("genisletilmis",imgGen)


cv2.waitKey(0)
cv2.destroyAllWindows()