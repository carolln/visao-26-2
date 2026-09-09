import cv2
import matplotlib.pyplot as plt
import numpy as np
# coordinates tl tr br bl

source_coordinates = np.array(
    [
    [52, 122], 
    [473, 27], 
    [663, 653],
    [162, 777],
    ],
       np.float32)
destination_coordinates = np.array([
    [0, 0], 
    [400, 0],
    [400, 500], 
    [0, 500], 
    ], np.float32)

img = cv2.imread("img/livro.jpg")

assert img is not None

transform = cv2.getPerspectiveTransform(src=source_coordinates, dst=destination_coordinates)

a = cv2.warpPerspective(img, transform, (400, 500))

cv2.imwrite("output/perspective.jpg",a)