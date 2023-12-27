import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 0.25)
ret, frame1 = cap.read()
ret, frame3 = cap.read()
k = 0
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame3)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 12000:
            continue

        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

    #cv2.drawContours(frame1, contours, -1,(0,255,0), 2)  
    #cv2.imwrite(f'frame_{k}.jpg', frame1)
    k += 1
    cv2.imshow('feed', frame1)
    frame1 = frame3
    ret, frame3 = cap.read()

    if cv2.waitKey(40) == 27:
        break


cap.release()
cv2.destroyAllWindows()    
