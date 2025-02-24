import cv2
import numpy as np

img = cv2.imread('gatito.jpeg')

if img is None: 
    print('Could not find image')

#Identity kernell
kernel1 = np.array([
    [ 0, 0, 0 ],
    [ 0, 1, 0 ],
    [ 0, 0, 0 ]])

kernel2 = np.ones((5,5),np.float32)/25

identity = cv2.filter2D(src = img, ddepth = -1,kernel = kernel1)
blurred  = cv2.filter2D(src = img, ddepth =-1, kernel = kernel2)

cv2.imshow('Original', img)
cv2.imshow('Identity', identity)
cv2.imshow('Kernel blur', blurred)

cv2.imwrite('Identity.jpg',identity)
cv2.imwrite('Blur_kernel.jpg',blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()