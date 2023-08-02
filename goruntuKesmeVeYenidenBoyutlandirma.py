import cv2

path = "frozen_cave.jpg"

img = cv2.imread(path)
print(img.shape)

width, height = 400,400

#resim = cv2.resize(resim, (genislik, yukseklik))

imgRes = cv2.resize(img,(width,height))
imgCrop = img[50:440, 150:400] #(yükseklik,genişlik)
imgCropRes = cv2.resize(imgCrop,(img.shape[1],img.shape[0])) #kırpttıktan sonra orijinal resim boyutunda boyutlandırma


cv2.imshow("normal",img)
cv2.imshow("resized", imgRes)
cv2.imshow("cropped",imgCrop)
cv2.imshow("cropped resized",imgCropRes)


cv2.waitKey(0)
cv2.destroyAllWindows()