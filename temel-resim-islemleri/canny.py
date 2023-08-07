import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread('car.jpg',0)
kenarlar=cv2.Canny(resim,50,200)

plt.subplot(121),plt.imshow(resim,cmap='gray')
plt.title('orjinal'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(kenarlar,cmap='gray')
plt.title('kenarlar'),plt.xticks([]),plt.yticks([])
plt.show()