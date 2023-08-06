import cv2
import numpy as np
import matplotlib.pyplot as plt

#resimler aslında uint8 tipinde değerlerdir.

x = np.uint8([120])
y = np.uint8([25])

z = cv2.add(x,y)
print(z)



#ağırlıklı toplama 
img1 = np.zeros((300,300,3),np.uint8) + 255
cv2.circle(img1,(150,150),50,(255,0,0),-1)
cv2.imshow("img1",img1)

img2 = np.zeros((300,300,3),np.uint8) + 255
cv2.line(img2,(0,0),(300,300),(0,255,0),5)
cv2.imshow("img2",img2)

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow("DST",dst)




#bitwise işlemler
img3 = np.zeros((400,400),dtype=np.uint8)
white = (255,255,255)
cv2.rectangle(img3,(75,75),(325,325),white,-1)
#cv2.imshow("rectangle",img3)

img4 = np.zeros((400,400),dtype=np.uint8)
cv2.circle(img4,(200,200),175,white,-1)
#cv2.imshow("circle",img4)

bitwiseAnd = cv2.bitwise_and(img3,img4)
bitwiseOr = cv2.bitwise_or(img3,img4)
bitwiseXor = cv2.bitwise_xor(img3,img4)
bitwiseNot = cv2.bitwise_not(img3)

#birden fazla çıktımız olduğu için tek tek cv2.imshow() ile göstermek yerine
#matplotlib kütüphanesinden yararlanıyoruz.

titles = ["Rectangle","Circle","Bitwise And","Bitwise Or","Bitwise Xor","Bitwise Not"]
images = [img3,img4,bitwiseAnd,bitwiseOr,bitwiseXor,bitwiseNot]

for i in range(6):
    plt.subplot(2,3,i+1) #bir pencere oluşturduk. 2,3'lük 
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_RGB2BGR))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
