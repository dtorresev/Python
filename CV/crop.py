import cv2 

img = cv2.imread("gatito.jpeg")
print(img.shape)
cv2.imshow("original", img)

cropped_img= img[80:200, 150:330]
cv2.imshow("cropped", cropped_img)
cv2.imwrite("cropped_gatito.jpg",cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

mi_lista = [10, 20, 30, 40, 50]

# Por ejemplo, empezar desde el segundo elemento (índice 1)
for i in range(1, len(mi_lista)):
    print(mi_lista[i])
