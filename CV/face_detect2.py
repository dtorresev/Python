import cv2

face_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

img = cv2.VideoCapture(0)

while True:
    ret,frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,6)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()