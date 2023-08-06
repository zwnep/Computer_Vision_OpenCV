import cv2

#Kontur algılamayı kullanarak nesnelerin sınırlarını algılayabilir ve bunları bir görüntüde kolayca yerelleştirebiliriz.

#Bir cismin sınırındaki tüm noktaları birleştirdiğimizde bir kontur elde ederiz.
#Tipik olarak, belirli bir kontur, aynı renk ve yoğunluğa sahip sınır piksellerini ifade eder.
#OpenCV, görüntülerde kontur bulmayı ve çizmeyi gerçekten kolaylaştırır.

#findContours()
#DrawContours()


image = cv2.imread("contuorImage.png")

imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgGray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', thresh)



#Drawing Contours using CHAIN_APPROX_NONE

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()







cv2.waitKey(0)
cv2.destroyAllWindows()



