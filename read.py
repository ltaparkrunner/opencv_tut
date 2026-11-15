import os
os.environ["QT_QPA_FONTDIR"] = "/usr/share/fonts"
import cv2 as cv

# img = cv.imread('opencv-course/Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Video', frame)

    if cv.waitKey(4) & 0xFF == ord('d'):
        break
capture.release()
# cv.waitKey(0)
cv.destroyAllWindows()