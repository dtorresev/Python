import cv2

img = cv2.imread("gatito.jpeg")
cv2.waitKey(0)
down_w = 70
down_h = 50
down_pts = (down_w,down_h)
resize_down = cv2.resize(img,(down_w,down_h),interpolation=cv2.INTER_LINEAR)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.imwrite("gatito_resize.jpeg",resize_down)

img2 = cv2.imread("gatito_resize.jpeg")
cv2.imshow("image2",img2)
cv2.waitKey(0)

cv2.destroyAllWindows()