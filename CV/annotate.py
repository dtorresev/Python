import cv2
img = cv2.imread("gatito.jpeg")
cv2.imshow('Original image', img)

h,w= img.shape[:2]

if img is None:
    print('Image does not exist')

#Make a copy for each modification
imgLine = img.copy()
imageCircle = img.copy()
imageFilledCircle = img.copy()
imageRectangle = img.copy()
imageText = img.copy()

#Point A - Inicio de imagen
pointA =(1,80)
#Point B - Ubicado al punto máximo de la imagen en su ancho
pointB = (w,80)

cv2.line(imgLine,pointA,pointB,(255,255,0),thickness=3, lineType = cv2.LINE_AA)

circle_center = (int(w/2),int(h/2))
radius = 50 
# Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
# Display the result
filled_radius =35
# draw the filled circle on input image
cv2.circle(imageFilledCircle, circle_center, filled_radius, (255, 0, 0), thickness=-1,lineType=cv2.LINE_AA)

start_point =(1,int(h/2))
end_point =(50, int(2*h/3))
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point,(0, 0, 255), thickness= 3, lineType=cv2.LINE_8)

#let's write the text you want to put on the image
text = 'Meow'
# write the text on the input image
cv2.putText(imageText, text, (1,(int(h/2))), fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 2, color = (250,0,0))

#Display the modified copies
cv2.imshow('Image Line',imgLine)
cv2.imshow("Image Circle",imageCircle)
cv2.imshow('Image with Filled Circle',imageFilledCircle)
cv2.imshow('imageRectangle', imageRectangle)
cv2.imshow("Image Text",imageText)

cv2.waitKey(0)

cv2.destroyAllWindows()