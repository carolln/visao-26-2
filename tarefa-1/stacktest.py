import cv2
import numpy as np

h, w = (10, 20)
_i, _j = np.ogrid[:h, :w]

arr_grey: np.ndarray = np.full((h, w, 1), 255, dtype=np.uint8)
grey_line = (_i == _j)
arr_grey[grey_line] = 0
cv2.imwrite("img/stackgreyline.jpg", arr_grey)

arr: np.ndarray = np.full((h, w, 3), (127, 0, 127), dtype=np.uint8)
_line = (_i == _j)
arr[_line] = (255, 255, 255)
cv2.imwrite("img/stackcolorline.jpg", arr)
arr_grey = cv2.cvtColor(arr_grey, cv2.COLOR_GRAY2BGR)
img = np.hstack([arr_grey, arr])
cv2.imwrite("img/stacktest.jpg", img)