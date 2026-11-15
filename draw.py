import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)
# 1. Paint the image a certain colour
blank[200:250, 350:400] = 255,255,0
# cv.imshow('Green', blank)
# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,250), (100, 250, 100), thickness=2)
# cv.rectangle(blank, (0,0), (250,250), (100, 250, 100), thickness=cv.FILLED)
# cv.rectangle(blank, (0,0), (250,250), (100, 250, 100), thickness=-1)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (100, 250, 100), thickness=-1)
#cv.imshow('Rectangle', blank)

# 3. Draw a cicle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (100, 100, 250), thickness=-1)
# cv.imshow('Circle', blank)
# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (250, 100, 250), thickness=4)
# cv.imshow('Line', blank)

# 5. Draw text
cv.putText(blank, 'Hello, my name is Jason!!!', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 0.5, (250, 100, 100), 2)
cv.imshow('Text', blank)
# img = cv.imread('opencv-course/Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)

cv.waitKey(0)
cv.destroyAllWindows()