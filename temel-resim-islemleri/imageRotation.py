import cv2

image = cv2.imread("car.jpeg")
#print(image.shape)

height,width = image.shape[:2]
center = (height/2,width/2)

#döndürme matrisi hesaplama
rotationMatrix = cv2.getRotationMatrix2D(center, angle=45, scale=1)

#Şimdi, warpAffine() işlevini kullanarak hesaplanan döndürme matrisini görüntüye uyguladım.
#parameters:(the source image,the rotation matrix,the size of the output image)
rotationImage = cv2.warpAffine(image,rotationMatrix,dsize=(width,height))

#2.yol
img = cv2.imread("mars.jpeg")

rotImag = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)


cv2.imshow("original",image)
cv2.imshow("Rotated",rotationImage)
cv2.imshow("Rotated 2",rotImag)


cv2.waitKey(0)
cv2.destroyAllWindows()