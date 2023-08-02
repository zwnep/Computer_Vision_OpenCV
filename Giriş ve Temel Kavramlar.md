# Temel Kavramlar ve OpenCV'ye Giriş

Bazı görüntü işleme kavramların ne olduğunu açıklamaya çalıştım. Bu tanımlar ansiklopedik olarak değil, görüntü işlemede neyi ifade ettiklerini anlatmaya çalıştım.

**Dijital Görüntü:**
Dijital görüntü, sayısal formatta temsil edilen bir görsel bilgidir. Bir dijital görüntü, piksellerden oluşur ve her piksel, görüntünün belirli bir konumunda belirli bir renge veya gri tonlamaya sahip bilgiyi içerir.

Dijital görüntüler, fotoğraf makineleri, kameralar ve diğer görüntü alma cihazları tarafından yakalanır ve bir bilgisayara aktarılır. Bu görüntüler dijital piksel dizileri olarak saklanır ve işlenir.

Görüntü işleme, bu dijital görüntüleri analiz etmek, düzenlemek, iyileştirmek veya bilgi çıkarmak için çeşitli algoritmaların ve tekniklerin kullanıldığı bir alanı ifade eder.

Bu temel kavramları anlamak, görüntü işlemenin temellerini kavramak ve daha gelişmiş görüntü işleme tekniklerine adım atmak için önemlidir.


**Piksel:**
Piksel, "picture element" kelimelerinin kısaltmasıdır. Bir piksel, dijital bir görüntünün en küçük bileşenidir ve tek bir renk veya gri tonlama değerini temsil eder.

Renkli bir görüntüde, bir piksel genellikle kırmızı, yeşil ve mavi (RGB) bileşenlerin bir kombinasyonunu içerir. Her bileşen, 0 ile 255 arasında bir değer alabilir ve 0 siyah, 255 beyaz olacak şekilde renk yoğunluğunu temsil eder.

Gri tonlamalı bir görüntüde, her piksel sadece parlaklık değerine sahiptir ve bu parlaklık değeri 0 ile 255 arasında bir sayıdır, 0 siyah ve 255 beyaz olarak kabul edilir.


![piksel açıklama](https://www.tech-worm.com/wp-content/uploads/2016/02/piksel.jpg)


**FPS (Frame Per Second - Saniyedeki Kare Sayısı):**
FPS, bir video akışında veya animasyonda saniyede oynatılan kare sayısını ifade eder. Örneğin, 30 FPS, her saniyede 30 farklı karenin ekranda gösterildiği anlamına gelir. FPS, video akışının akıcılığını belirleyen önemli bir faktördür.

Düşük FPS değerleri, video akışının takılmasına ve akıcılığın azalmasına neden olabilir. Yüksek FPS değerleri, daha pürüzsüz ve doğal bir video deneyimi sunar, ancak bu, daha fazla işlem gücü gerektirir. Oyunlar ve hızlı hareket eden sahnelerde yüksek FPS değerleri önemlidirken, genel video akışında 24-30 FPS genellikle yeterlidir.


**Histogram:**
Histogram, bir görüntünün renk dağılımını veya gri tonlama değerlerini görselleştiren bir grafiktir. Bir görüntüdeki piksellerin belirli bir renk veya parlaklık değerine sahip olduğu frekansı gösterir. Yatay eksen, renklerin veya gri tonlama değerlerinin farklı düzeylerini, dikey eksen ise bu düzeylere sahip piksellerin sayısını gösterir.

Renkli bir görüntünün histogramı, kırmızı, yeşil ve mavi bileşenler için ayrı ayrı veya tek bir histogramda gösterilebilir. Gri tonlamalı bir görüntünün histogramı ise yalnızca parlaklık değerlerine dayanır.

Histogramlar, görüntünün kontrastı, parlaklığı, renk dağılımı ve aydınlık durumu gibi özellikleri hakkında önemli bilgiler sağlar. Ayrıca, görüntü üzerinde gerçekleştirilecek işlemler için ön işleme adımlarında ve sınıflandırma gibi görevlerde de kullanışlıdır.


![histogram açıklama](https://miro.medium.com/v2/resize:fit:846/1*ZsB5N4w-WUs0CiCUBcweRw.png)