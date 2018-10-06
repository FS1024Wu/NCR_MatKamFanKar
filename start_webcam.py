import cv2
import numpy as np
import os


def show_webcam(dir_path, mirror=False):
    face_cascade = cv2.CascadeClassifier(dir_path)

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))+ "\\data\\haarcascade_frontalface_default.xml"
    dir_path = "D:\\MEGA\\hackgsu\\NCR_MatKamFanKar\\data\\haarcascade_frontalface_default.xml"
    print(dir_path)
    show_webcam(dir_path=dir_path , mirror=True)



if __name__ == '__main__':
    main()