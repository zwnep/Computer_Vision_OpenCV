import cv2
from skimage import io

adresler=[
    "https://www.pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
    "https://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png"
]

for adres in adresler:
    print("%s yukleniyor"%(adres))
    resim=io.imread(adres)
    cv2.imshow('BGR format',resim)
    cv2.imshow('RGB format',cv2.cvtColor(resim,cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)