import cv2
img = cv2.imread("gatito.jpeg")
h,w= img.shape[:2]
center = (w/2,h/2)

r_mat = cv2.getRotationMatrix2D(center=center, angle = 180, scale = 1)

r_img = cv2.warpAffine(src= img, M = r_mat,dsize=(w,h))

cv2.imshow('Original image', img)
cv2.imshow('Rotated image', r_img)

cv2.waitKey(0)
cv2.imwrite('rotated_img.jpg',r_img)