import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('img/azimjon.png')
camera = cv2.VideoCapture(0)


def decode_qr(img):
    decoded_data = decode(img)
    if decoded_data:
        return decoded_data[0].data.decode('utf-8')
    else:
        return None


while True:
    _, frame = camera.read()
    decoded_data = decode_qr(frame)
    if decoded_data:
        cv2.putText(frame, decoded_data, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
