import cv2

frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture(0) #0: kendi kameramızdan, 1 yazarsak harici bir kameradan veya kendi videomuzu verebiliriz.
#Sisteme bağşı ilk kamerayı döndürür

#Görüntünü oynayabilmesi için döngü olması gerekiyor.
while True:
    success,vid = cap.read() #cap.read() True-False döndürür.

    # False olursa yani video bağlantısı kesildiğinde veya video bittiğinde if not ret: bloğuna düşüp döngüden hatasız şekilde çıkacaktır.
    if not success:
        break

    #vid = cv2.resize()
    cv2.imshow("video1",vid)

    if cv2.waitKey(25) & 0XFF == ord("q"):
        break # "q" tuşuna basınca kapansın istiyoruz.


cap.release()
cv2.destroyAllWindows()
