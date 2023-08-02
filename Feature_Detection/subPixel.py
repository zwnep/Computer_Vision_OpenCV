#SubPixel Accuracy

import cv2 

# Bazen köşeleri maksimum doğrulukla bulmanız gerekebilir.
# OpenCV, alt piksel doğruluğuyla algılanan köşeleri daha da iyileştiren bir cv.cornerSubPix() işleviyle birlikte gelir.
# Her zamanki gibi, önce Harris köşelerini bulmamız gerekiyor. 
# Sonra bu köşelerin ağırlık merkezlerini geçiyoruz (bir köşede bir sürü piksel olabilir, ağırlık merkezlerini alıyoruz) onları rafine etmek için. 


# Subpiksel doğruluğu, köşe tespiti gibi görüntü işleme algoritmalarında elde edilen sonuçların daha hassas bir şekilde yerel birimlere konumlandırılması anlamına gelir.
# Görüntü işleme uygulamalarında, standart köşe tespiti algoritmaları, piksel düzeyinde köşe konumlarını tespit eder. 
# Ancak bazen, piksel düzeyindeki sonuçlar yetersiz olabilir ve daha yüksek doğruluk seviyesi gerekebilir.

# Subpiksel doğruluğu, köşe noktalarının konumlarının daha hassas bir şekilde belirlenmesini sağlar. 
# Standart köşe tespiti algoritmaları genellikle piksel merkezlerini köşe olarak tanımlar. 
# Ancak, gerçek köşe konumları, piksel merkezleri arasındaki konum farklarının alt piksel seviyesinde hesaplanmasıyla daha hassas bir şekilde bulunabilir.

# Subpiksel doğruluğu elde etmek için, genellikle piksel yoğunluk değerlerinin alt piksel seviyesinde interpolasyonunu içeren ek yöntemler kullanılır. 
# Bu yöntemler, yakındaki piksel yoğunluk değerlerini dikkate alarak, piksel merkezleri arasında doğru bir şekilde alt piksel seviyesinde konumlanmış bir köşe noktası elde etmeye çalışır.


#Sonuç olarak, subpiksel doğruluğu, standart köşe tespiti sonuçlarının daha hassas bir şekilde alt piksel seviyesinde konumlandırılmasını sağlayan bir yöntemdir ve daha yüksek doğruluk gerektiren görüntü işleme uygulamalarında önemli bir rol oynar.


image_path = "chessboard.jpeg"

def detect_corners(image_path):
    # Görüntüyü yükle
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Harris Köşe Tepki Fonksiyonunu hesapla
    corner_response = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Tepki fonksiyonunu artan düzenle
    corner_response = cv2.dilate(corner_response, None)

    # Tepki değeri eşiğini belirle
    threshold = 0.01 * corner_response.max()

    # Köşe noktalarını bul ve çiz
    corners = []
    for y in range(corner_response.shape[0]):
        for x in range(corner_response.shape[1]):
            if corner_response[y, x] > threshold:
                corners.append((x, y))
                cv2.circle(image, (x, y), 3, (0, 255, 0), -1)

    # Görüntüyü göster
    cv2.imshow("SubPiksel Köşe Tespiti", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_corners(image_path)
