import cv2
import numpy as np

image = cv2.imread("car.jpeg")

image_copy = image.copy()

#(yükseklik,genişlik,kanal) [0]->yükseklik, [1]->genişlik
imgheight = image.shape[0]
imgwidth = image.shape[1]

M = 76
N = 104
x1 = 0 
y1 = 0

for y in range(0,imgheight,M):
    for x in range(0,imgwidth,N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break

        y1 = y + M
        x1 = x + N

        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1

            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)

        elif y1 >= imgheight: # when patch height exceeds the image height
            y1 = imgheight - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)

        elif x1 >= imgwidth: # when patch width exceeds the image width
            x1 = imgwidth - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)

        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)


cv2.imshow("Cropped Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()