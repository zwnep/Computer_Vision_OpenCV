import cv2

#(Piksellerin renk farklılaşmasından yararlanarak kenar tespiti.)
#Piksel yoğunluğundaki ani değişiklikler kenarları karakterize eder. 
#Kenarları tespit etmek için komşu piksellerde bu tür değişiklikleri aramamız gerekiyor. 
#OpenCV'de bulunan iki önemli kenar algılama algoritmasını kullanarak keşfedelim: Sobel Edge Detection ve Canny Edge Detection. Teoriyi tartışacağız ve her birinin OpenCV'deki kullanımını göstereceğiz.

image = cv2.imread("tiger.jpeg",flags=0)
#Burada, kenarları tespit etmek için renk bilgisine ihtiyacınız olmadığı için renkli görüntüyü gri tonlamalı görüntü olarak okuyoruz.
#cv2.IMREAD_UNCHANGED  or -1
#cv2.IMREAD_GRAYSCALE  or 0
#cv2.IMREAD_COLOR  or 1

#Görüntüyü okuduktan sonra GaussianBlur() işlevini kullanarak da bulanıklaştırıyoruz.
#Bu, görüntüdeki gürültüyü azaltmak için yapılır. 
#Kenar algılamada, piksel yoğunluklarının sayısal türevlerinin hesaplanması gerekir ve bu tipik olarak 'gürültü' kenarlarla sonuçlanır.
#Başka bir deyişle, bir görüntüdeki komşu piksellerin yoğunluğu (özellikle yakın kenarlar) oldukça dalgalanarak, aradığımız baskın kenar yapısını temsil etmeyen kenarlara yol açabilir.

#Bulanıklaştırma, kenarlara yakın yoğunluk değişimini yumuşatarak görüntü içindeki baskın kenar yapısını tanımlamayı kolaylaştırır.
#Bulanıklaştırma derecesini belirten evrişim çekirdeğinin boyutunu (bu durumda 1 3×3 çekirdek) sağlıyoruz.

imgBlur = cv2.GaussianBlur(image,(3,3),sigmaX=0,sigmaY=0)

#cv2.imshow("original",image)
#cv2.imshow("GSblur",imgBlur)


#Sobel Kenar Algılama, kenar algılama için en yaygın kullanılan algoritmalardan biridir. 
#Sobel Operatörü, piksel yoğunluğundaki ani değişikliklerle işaretlenmiş kenarları algılar.

#Sobel(src, ddepth, dx, dy)

#Ddepth parametresi çıktı görüntüsünün hassasiyetini belirtirken, dx ve dy türevin her yöndeki sırasını belirtir. 
#Örneğin:

#Dx=1 ve dy=0 ise, 1. türev Sobel görüntüsünü x yönünde hesaplarız.

#Hem dx=1 hem de dy=1 ise, 1. türev Sobel görüntüsünü her iki yönde de hesaplarız.

sobelx = cv2.Sobel(imgBlur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
sobely = cv2.Sobel(imgBlur,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
sobelxy = cv2.Sobel(imgBlur,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=5)

cv2.imshow("Sobel X",sobelx)
cv2.imshow("Sobel Y",sobely)
cv2.imshow("Sobel X-Y combined",sobelxy)


#Canny Kenar Algılama
#Canny(image, threshold1, threshold2)
canny = cv2.Canny(imgBlur,threshold1=50,threshold2=100)
#threshold1-2 kenarları linklemek için kullanılıyor. Daha büyük değerler girilmesi demek daha kuvvetli kenarların bulunması demektir.
#kenarların tespit edilmesi için kullanılan eşiği belirtir. 


cv2.imshow("Canny",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()
