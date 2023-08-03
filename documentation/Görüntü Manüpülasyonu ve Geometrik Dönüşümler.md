# Görüntü Manüpülasyonu ve Geometrik Dönüşümler

Görüntü işleme süreci verilerin bilgisayarlar tarafından tanınmasıyla başlar. Görüntü formatındaki veri için öncelikle matris oluşturulur. Resimdeki her bir piksel değeri bu matrise işlenir. Sonuç olarak 200 x 200 boyutundaki bir resim için 200 x 200 boyutunda bir matris oluşturulur. Eğer bu resim renkli ise bu boyut 200x200x3 halini alır (RGB). Görüntü işleme sürecinde yapılan her manipülasyon aslında bir matris işlemidir. Örnek olarak verdiğimiz 200x200 boyutundaki resim üzerinde bir bulanıklaştırma işlemi yapılmak istendiğini varsayalım. Burada belirli bir filtre bütün matris üzerinde gezerek matris elemanlarının tamamının veya bir kısmının üzerinde işlem yapar. Bu işlem sonucunda resmin istenen bölümü veya tamamı bulanık bir hale gelir. Bu durum diğer görüntü işleme süreçleri için de geçerlidir.

Örnek olarak bazı projelerde bu verilerin renkli olmasının eğitime bir etkisi yoktur. Bu gibi durumlarda eğitimi renkli resimler ile gerçekleştirmek, eğitimin daha yavaş ve daha düşük performans ile yapılmasına sebebiyet verir.

Resimlerdeki kalitenin artırılması, görüntüler üzerinde restorasyonlar yapılması, gürültülerin temizlenmesi gibi bir çok işlem görüntü işleme süreçlerinin içerisinde yer almaktadır.

