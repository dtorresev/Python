import cv2

img = cv2.imread("gatito.jpeg")
size = img.shape
num = int(input("Número de divisiones:  "))
block_w= int(size[0]/num)
block_h = int(size[1]/num)

print("Tamaño de imagen: ",size[0:2])
print("Ancho de bloque: ", block_w)
print("Altura de bloque: ", block_h)

roi_w = size[0]
roi_h = size[1]

cv2.imshow("image",img)

for i in range(num*num):
    print(i)
    if i == 0:
        upper = 1 
        left = 1
    if i != 0:
        left = left + block_w
        upper = upper + block_h

    right = left + block_w if i < num  else roi_w
    lower = upper + block_h if i < num  else roi_h

    print(f"[{left}, {right}:{upper}, {lower}]")

    cropped_img = img[left:right,upper:lower]

    patch_filename = f"cropped_gatito_block_{i + 1}.jpg"
    cv2.imshow(f"Block {i + 1}", cropped_img)
    cv2.imwrite(patch_filename, cropped_img)
    cv2.waitKey(0)
    i = i + 1

print(f"Total patches created: {i}")
cv2.destroyAllWindows()