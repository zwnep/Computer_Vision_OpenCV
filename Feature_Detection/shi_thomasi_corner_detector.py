# Shi-Thomasi

# Shi-Tomasi köşe tespit yöntemi Harris algoritmasının geliştirilmesi ile oluşturulmuştur. 
# Sadece seçme ölçütü farklı olmasına rağmen Harris yöntemine göre daha iyi sonuçlar vermektedir.

# Harris yöntemi doğruluktan ödün vererek zaman karmaşıklığı düşük çalışmaktadır. 
# Shi-Tomasi yönteminin zaman karmaşıklığı daha yüksek olmasına rağmen özdeğerleri hesapladığı ve sadece özdeğerlerin kendisini değerlendirdiği için doğruluğu Harris yöntemine göre daha yüksektir.

# R = min(y1,y2)

# denkleminde R fonksiyonun büyük pozitif değerde olması köşeye,
# (y1,y2) değerlerinin birisinden küçük olması kenara ve 
# (y1,y2) değerlerinin ikisinde de küçük olması ise düz bölgeye karşılık gelmektedir.





import numpy as np
import cv2 
from matplotlib import pyplot as plt

img = cv2.imread("chessboard.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,50,0.7,50)
corners = np.int32(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()
