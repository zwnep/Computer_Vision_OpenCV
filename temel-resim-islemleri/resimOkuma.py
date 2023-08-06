import cv2
#fotoğraftan görüntü okuma

#imread(): helps us read an image
#imshow(): displays an image in a window
#imwrite(): writes an image into the file directory


#imerad(filename, flags)
#cv2.IMREAD_UNCHANGED or -1
#cv2.IMREAD_GRAYSCALE or 0
#cv2.IMREAD_COLOR or 1 ---> default value is 1, which will read in the image as a Colored image.


img = cv2.imread("mars.jpeg")

print(img) #img yani resmi matrisler halinde yazdırıyoruz.
#Resimler 3 kanallı matristen oluşur. 3 renkli -mavi, kırmızı, yeşil-
print(type(img))

print(img.shape) #(yükseklik, genişlik, kanal sayısı) çıktısı

#ilk paramtre str olup gösterilecek pencere ismidir, ikinci parametre ise bizim görüntülemek istediğimiz 
cv2.imshow("image", img)
cv2.waitKey(2000) #2 sn bekledi.
cv2.destroyAllWindows()
