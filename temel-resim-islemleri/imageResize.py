import cv2
import numpy as np 

image = cv2.imread("car.jpeg")

h,w,c = image.shape
print("orijinal \nyükseklik: " ,h ,"\ngenişlik: " ,w)

#küçültme işlemi uygulayalım.
down_width = 300
down_height = 200
down_points =(down_width, down_height)
resize_down = cv2.resize(image, down_points)

up_width = 1400
up_height = 600
up_points = (up_width, up_height)
resize_up = cv2.resize(image, up_points)

cv2.imshow("normal_image",image)
cv2.imshow("resized_down_image",resize_down)
cv2.imshow("resized_up_image",resize_up)


#scaling factor-ölçeklendirme, biz fotoğrafı büyütüp küçülttüğümüzde 
#resmin kalitesinin bozulmamasını sağlamak amaçlı. Bozuk görüntüyü önler.

scale_up_x = 1.2
scale_up_y = 1.2
scale_down = 0.6

scaled_down = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
scaled_up = cv2.resize(image, None, fx=scale_up_x,fy=scale_up_y,interpolation= cv2.INTER_NEAREST)

#Yukarıdaki Python pasajında:

#Yatay ve dikey eksen boyunca yeni ölçeklendirme faktörleri tanımlıyoruz.
#Ölçekleme faktörlerinin tanımlanması, genişlik ve yükseklik için yeni noktalara sahip olma ihtiyacını ortadan kaldırır.
#Bu nedenle, dsize'ı None olarak tutuyoruz.


#INTER_NEAREST: nearest neighbor interpolation technique
#INTER_LINEAR: bilinear interpolation (default)
#INTER_LINEAR_EXACT
#INTER_AREA: resampling using pixel area relation
#INTER_CUBIC: bicubic interpolation over 4 x 4 pixel neighborhood


cv2.waitKey(0)
cv2.destroyAllWindows()