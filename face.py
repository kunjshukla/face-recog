import cv2
import argparse
face_cascade = cv2.CascadeClassifier('test.xml')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0),3)
        cv2.imshow('img' , img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break