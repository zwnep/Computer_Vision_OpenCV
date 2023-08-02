import cv2

# SIFT

# Bir görüntünün, aydınlatma, döndürme ve ölçeklendirmeye karşı değişmeyen bölgesel özelliklerini belirleyip tanımlayan bir algoritmadır.
# Bu algoritma nesne tanımada, robotik haritalamada, görüntü birleştirmede, 3B modellemede, hareket tanımada ve video izlemede kullanılabilir. 
# 1999 yılında David Lowe tarafından yayınlanmıştır.

# Algoritma 4 ana adımdan oluşmaktadır:
# Ölçek Uzayındaki Ekstremumları Bulma
# Anahtar Noktanın Yerini Belirleme
# Oryantasyon Belirleme
# Anahtar Nokta Tanımlayıcıları



# 1) Ölçek Uzayındaki Ekstremumları Bulma

# Algoritmaya ilk olarak anahtar noktalarını(keypoints) bularak başlanır.
# Bu adım için Gaussian filtresi kullanılır. 

# Gaussian filtresi ile bulanık hale gelen görüntüler arasındaki farklar alınır.
# Farklı ölçeklerde alınan Gaussian farkının (DoG) ekstremum noktaları anahtar noktaları verir. 

# 2) Anahtar Noktanın Yerini Belirleme

# Algoritmanın ilk adımında bulduğumuz noktaların bazı kısımlarını temizlememiz gerekiyor. 
# Kenarlar bu kısma dahil olmamalı, bunu iki adımda gerçekleştiririz. 
# Anahtar noktalarda iki yönde gradyan alınır, eğer gradyanlar küçükse bölge flat bir bölgedir. 
# Eğer bir gradyan büyükken diğer gradyan küçükse, değişim tek taraflıdır yani burası bir kenardır. 
# Eğer iki gradyan da büyükse burası köşedir. 
# Kısaca burada bir eşik değeri belirlenir ve bu değerin altında kalan kısımlar, kenarlar, flat arealar eleniyor. 
# Burada Harris Köşe Dedektörü kullanılır.

# 3) Oryantasyon Belirleme

# Bu adımda, her bir anahtar noktaya, görüntüdeki eğim yönüne bakılarak bir ya da daha fazla oryantasyon atanır. 
# Gaussian uygulanılarak bulanıklaşan görüntüde, anahtar noktaların etrafındaki komşu bölgede yer alan her piksel için, eğimin büyüklüğüne ve yönüne bakılır. 
# Her bir kutusu 10 derece içeren 36 kutuluk bir histograma bulunan değerler yerleştirilir. 
# Histogramın zirve noktası, aradığımız oryantasyonu belirtir.

# 4) Anahtar Nokta Tanımlayıcıları

# İlk olarak, her biri 8 kutu içeren 4x4 piksel komşuluğunda oryantasyon histogramları oluşturulur. 
# Anahtar nokta etrafındaki 16x16'lık bir bölgede yer alan, oryantasyon ve büyüklük ile ilgili bilgi veren histogramlar hesaplanır. 
# Her bir histogram gerçek komşuluk bölgesinin 4x4'lük bir alt bölgesini içerir. 
# Her biri 8 kutu içeren, 16(4x4) histogramlar, toplamda 128 adet vektör belirtmiş olurlar. Bu vektörler, anahtar nokta tanımlayıcılarıdır.



