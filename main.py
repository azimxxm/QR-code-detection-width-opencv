import cv2
import numpy as np
from pyzbar.pyzbar import decode


# img = cv2.imread('img/azimjon.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('db.txt', 'r') as f:
    db = f.read().splitlines()


while True:

    success, img = cap.read()
    for barcode in decode(img):
        my_Data = barcode.data.decode('utf-8')
        print(my_Data)

        if my_Data in db:
            print('Access Granted')
            cv2.putText(img, 'Access Granted', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            color = (0, 255, 0)
        else:
            print('Access Denied')
            cv2.putText(img, 'Access Denied', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            color = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (color), 5)
        cv2.putText(img, my_Data, (barcode.rect.left, barcode.rect.top), cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 100, 50), 3)
    
    cv2.imshow('RESULT', img)
    cv2.waitKey(2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




