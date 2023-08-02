import cv2
import numpy as np

image = cv2.imread("frozen_cave.jpg")

#resmin yükseklik ve genişliğini alalım.
height,width = image.shape[:2]

#translation matrixini oluşturalım.(bir numpy array'i)
tx, ty = width/2, height/2 #istenilen bir değer verilebilir; w/4, h/4 vb.
translationMatrix = np.array([
    [1,0,tx],
    [0,1,ty]
],dtype=np.float32)

translatedImage = cv2.warpAffine(image,translationMatrix,(width,height))


cv2.imshow("original",image)
cv2.imshow("translated",translatedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

