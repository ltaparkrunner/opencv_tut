import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('opencv-course/Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue or frame is None:
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(4) & 0xFF == ord('d'):
        break
capture.release()
cv.waitKey(3000)
cv.destroyAllWindows()