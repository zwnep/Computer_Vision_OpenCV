import cv2
import numpy

#opencv içinde kırpma için belirli bir fonk. yoktur ama numpy kütüphanesini kullanarak kesme işlemleri yapılır.

image = cv2.imread("agac.jpeg")
print(image.shape)

cv2.imshow("original",image)

#cropped = img[start_row:end_row, start_col:end_col]

cropped_img = image[500:3500,500:2500] #(yükseklik, genişlik)

cv2.imshow("cropped",cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

