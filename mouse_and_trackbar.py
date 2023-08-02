import cv2

#OpenCV, sol tıklama ve sağ tıklama gibi çeşitli fare işlemlerini algılamak için bir fare olay algılama özelliği sağlar. 
#Bu ilk örnekte, adlandırılmış bir pencerede görüntülenen bir görüntü üzerinde bir dikdörtgen oluşturmak için fareyi nasıl kullanabiliriz görelim.

#dikdörtgen çizmek için noktaları depolanacağı dizileri oluşturalım.

top_left_corner = []
bottom_right_corner = []

def drawRectangle(action,x,y,flags,user,*userdata):

    global top_left_corner, bottom_right_corner

    if action == cv2.EVENT_LBUTTONDOWN:
        #sol mouse tıklandığında top left corner olarak işaretle
        top_left_corner = [(x,y)]
    elif action == cv2.EVENT_LBUTTONUP:  
        #sol mouse serbest bırakıldığında bottom right corner olarak işaretle
        bottom_right_corner = [(x,y)]

        cv2.rectangle(image,top_left_corner[0],bottom_right_corner[0],(255,255,255),5)  
        cv2.imshow("Window",image)

image = cv2.imread("jellyfish.jpeg")

temp = image.copy()

cv2.namedWindow("Window")

cv2.setMouseCallback("Window", drawRectangle)

#cv2.setMouseCallback(winname, onMouse, userdata)

k=0
while k!=113:
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Window", image)
cv2.destroyAllWindows()


#Resizing an Image Using the Trackbar

maxScaleUp = 100
scaleFactor = 1

windowName = "Resize Image"
trackbarValue = "Scale"

image = cv2.imread("jellyfish.jpeg")

cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)

def scaleImage(*args):
     
    scaleFactor = 1+ args[0]/100.0
     
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy=scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


#cv2.createTrackbar( trackbarName, windowName, value, count, onChange)

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)

cv2.imshow(windowName, image)


cv2.waitKey(0)
cv2.destroyAllWindows()
