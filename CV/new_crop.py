import cv2
import numpy as np

img = cv2.imread("gatito.jpeg")
print(img.shape)

# Define el tamaño de resize
up_width = 700
up_height = 500
up_points = (img, (up_width, up_height))

# Realiza el resize
resize_up = cv2.resize(img, (up_width, up_height))

# Calcula el ancho y alto de cada cuadro
ancho_cuadro = resize_up.shape[1] // 3
alto_cuadro = resize_up.shape[0] // 2

rows = input("Ingresa el número de filas")
columns = input("Ingresa el número de columnas")
# Crea un bucle para recorrer cada cuadro
for i in range(int(rows)):
    for j in range(int(columns)):
        # Calcula las coordenadas del cuadro actual
        x_inicio = j * ancho_cuadro
        y_inicio = i * alto_cuadro
        x_fin = (j + 1) * ancho_cuadro
        y_fin = (i + 1) * alto_cuadro

        # Corta la imagen utilizando slicing
        cropped_image = resize_up[y_inicio:y_fin, x_inicio:x_fin]
        # Muestra y guarda la imagen cortada
        cv2.imshow(f"cropped_{i}_{j}", cropped_image)
        cv2.imwrite(f"cropped_{i}_{j}.jpeg", cropped_image)


cv2.waitKey(0)
cv2.destroyAllWindows()