import cv2
import numpy as np

img = cv2.imread("gatito.jpeg")
print(img.shape)

# Define el tamaño de resize
up_width = 700
up_height = 500
up_points = (img, (up_width, up_height))


def resize_image_to_fit_dimensions(img, new_width, new_height):
    return cv2.resize(img, (new_width, new_height))

# Realiza el resize
resize_up = cv2.resize(img, (up_width, up_height))

 # Define the initial size of the image
original_width, original_height = img.shape[1], img.shape[0]
    
rows = int(input("Ingresa el número de filas: "))
columns = int(input("Ingresa el número de columnas: "))    
    # Calculate new dimensions to fit rows and columns
new_width = (original_width // columns) * columns
new_height = (original_height // rows) * rows

    # Resize image to fit the new dimensions
resized_img = resize_image_to_fit_dimensions(img, new_width, new_height)
print("Resized image shape:", resized_img.shape)

    # Calculate size of each slice
ancho_cuadro = resized_img.shape[1] // columns
alto_cuadro = resized_img.shape[0] // rows
  
for i in range(rows):
    for j in range((columns)):
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