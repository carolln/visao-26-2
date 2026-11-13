import cv2 as cv
import numpy as np

# CODE MADE AVAILABLE BY OPENCV!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# converting to hsv and tryna get this to work
# YIPPIEEEEEEEEEEEEEE THIS FINALLY WORKS!!!!!!!!!!!!!!!!!!

def nothing(x):
    pass
 
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.namedWindow('image')
 
# create trackbars for color change
cv.createTrackbar('H','image',0,179,nothing)
cv.createTrackbar('S','image',0,255,nothing)
cv.createTrackbar('V','image',0,255,nothing)
 
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
 
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
 
    # get current positions of four trackbars
    h = cv.getTrackbarPos('H','image')
    s = cv.getTrackbarPos('S','image')
    v = cv.getTrackbarPos('V','image')
    sw = cv.getTrackbarPos(switch,'image')

    calma = np.uint8([[[h,s,v]]])
    calma = cv.cvtColor(calma, cv.COLOR_HSV2BGR)
 
    if sw == 0:
        img[:] = 0
    else:
        img[:] = [calma[0][0][0],calma[0][0][1],calma[0][0][2]]
 
cv.destroyAllWindows()