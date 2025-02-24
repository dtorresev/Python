# more info: https://learnopencv.com/contour-detection-using-opencv-python-c/
# more info: https://learnopencv.com/image-filtering-using-convolution-in-opencv/
import cv2
image = cv2.imread('gatito.jpeg')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_copy = image.copy()
image_copy1 = image.copy()
# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours on the original image
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,lineType=cv2.LINE_AA)
cv2.drawContours(image_copy1, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)

# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.imshow('None approximation', image_copy)
cv2.imshow('Simple approximation', image_copy1)

# see the results
cv2.imwrite('image_thres1.jpg', thresh)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.imwrite('contours_simple_image1.jpg', image_copy1)

cv2.waitKey(0)
cv2.destroyAllWindows()