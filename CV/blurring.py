import cv2
import numpy as np

img = cv2.imread('gatito.jpeg')

img_blur = cv2.blur(src=img, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)# sigmaX is Gaussian Kernel standard deviation 
median = cv2.medianBlur(src=img, ksize=5)
kernel3 = np.array([[0, -1,  0],
                    [-1,  5, -1],
                    [0, -1,  0]])
sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel3)

# Display using cv2.imshow()
cv2.imshow('Original', img)

cv2.imshow('f_Blurred', img_blur) 
cv2.imshow('Gaussian Blurred', gaussian_blur)
cv2.imshow('Median Blurred', median)
cv2.imshow('Sharpened', sharp_img)

cv2.imwrite('fblur.jpg', img_blur)
cv2.imwrite('gaussian_blur.jpg', gaussian_blur)
cv2.imwrite('median_blur.jpg', median)
cv2.imwrite('sharp_image.jpg', sharp_img)

cv2.waitKey()
cv2.destroyAllWindows()