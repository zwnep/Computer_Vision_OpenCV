import cv2

image = cv2.imread("tiger.jpeg")

satir,sutun,kanal = image.shape

imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray",imgGray)

ret,mask = cv2.threshold(imgGray,10,255,cv2.THRESH_BINARY)
cv2.imshow("mask",mask)

maskNot = cv2.bitwise_not(mask)
cv2.imshow("not mask",maskNot) #arkaplanı çıkartılmış hali


cv2.waitKey(0)
cv2.destroyAllWindows()
