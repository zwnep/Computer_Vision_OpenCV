import cv2

#Nasıl kullanılabiliriz:
#Demolarınıza bilgi ekleme
#Nesne algılama durumunda nesnelerin etrafına sınırlayıcı kutular çizmek
#Görüntü segmentasyonu için farklı renklerle pikselleri vurgulama

#Görüntülere geometrik şekiller ve metinlerle nasıl açıklama ekleneceğini görmüş olacağız.

image = cv2.imread("mars.jpeg")
print(image.shape)

imageWithLine = image.copy()

pointA = (2300,470)
pointB = (3000,470)
cv2.line(imageWithLine,pointA,pointB,(255,255,0),4)

#daire çizme
imageWithCircle = image.copy()

circleCenter = (2660,1300)
radius = 600
cv2.circle(imageWithCircle,circleCenter,radius,(255,255,255),20,lineType=cv2.LINE_AA)

#dikdörtgen çizme
imageWithRectangle = image.copy()

baslangıc = (2300,470)
son = (3000,2000)
cv2.rectangle(imageWithRectangle,baslangıc,son,(255,255,255),20)

#elips çizme
imageWtihElips = image.copy()

#elips çizerken yarıçap belirtmemize gerek yoktur.
#ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color, thickness)
#majör ve minör axes yani yarıçap ölçülerini belirtmemiz gerekir.
elipsCenter= (2660,1300)
axis = (400,100)
axis2 = (500,900)
cv2.ellipse(imageWtihElips,elipsCenter,axis,90,0,360,(255,255,255),20)
cv2.ellipse(imageWtihElips,elipsCenter,axis2,45,0,360,(255,255,255),20)

#adding text
#putText(image, text, org, font, fontScale, color)
#İlk argüman giriş görüntüsüdür.
#Bir sonraki argüman, görüntüye açıklama eklemek istediğimiz gerçek metin dizesidir.
#Üçüncü bağımsız değişken, metin dizesinin sol üst köşesinin başlangıç konumunu belirtir.
#Sonraki iki bağımsız değişken yazı tipi stilini ve ölçeğini belirtir.

imageWithText = image.copy()

text = "happy mars!!"
org = (500,300)
cv2.putText(imageWithText,text,org,fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=10,color=(255,0,0),thickness=5)



cv2.imshow("açıklamalı",imageWithLine)
cv2.imshow("daireli",imageWithCircle) #içi dolu bir daire çizmek istersek cv2.imshow("daireli",imageWithCircle,imageFilledCircle)
cv2.imshow("dikdörtgenli",imageWithRectangle)
cv2.imshow("elipsli",imageWtihElips)
cv2.imshow("textli",imageWithText)


cv2.waitKey(0)
cv2.destroyAllWindows()