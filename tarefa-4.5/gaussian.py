import cv2 as cv
import numpy as np

KSIZE = 3

img = cv.imread('img/C_gaussiano_r060.png', cv.IMREAD_GRAYSCALE)
img_blur = cv.GaussianBlur(img, (KSIZE, KSIZE), 0)

# Thresholds aleatõrios
img_edges = cv.Canny(img_blur, 0, 100)

h,w = img.shape

n_white = 0
sumx, sumy = 0, 0
max_x, min_x, = -float('inf'), float('inf')
max_y, min_y = -float('inf'), float('inf')

for i in range(h):
    for j in range(w):
        if (img_edges[i,j] == 255):
            if (j < min_x):
                min_x = j
            elif (j > max_x):
                max_x = j
            
            if (i < min_y):
                min_y = i
            elif (j > max_y):
                max_y = i
            
            sumx += i
            sumy += j
            n_white += 1


print(round(sumx/n_white), round(sumy/n_white), round((max_x-min_x + max_y-min_y) / 4))

# C,C_gaussiano_r060.png,gaussiano,120.0,688,397,60