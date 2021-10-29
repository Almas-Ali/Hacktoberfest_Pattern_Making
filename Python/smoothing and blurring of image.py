# smoothing operation is used to remove the noise from the image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Filter 2D convolution is one way to blur the image.
# LPF helps in removing the noise, blurring the image,etc.
# HPF helps in finding the edges in the images.
# Gaussian filter has pixel in the middle has higher weights.
# Median filter removes each pixel value by its median(best for salt and pepper noise).

img = cv2.imread('girl.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))   # this is also called averaging
gaussian_blur = cv2.GaussianBlur(img,(5,5),0)
median =  cv2.medianBlur(img,5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)

titles = ['Image','2D-Convolution','blur','gaussian blur','median','Bilateral Filter']
images = [img,dst,blur,gaussian_blur,median,bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

