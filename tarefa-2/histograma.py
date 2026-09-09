import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img/foto06.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None
h, w = img.shape

output_img = np.full((h,2*w), 255, np.uint8)

histogram = [0 for _ in range(256)]
histogram_div = h*w

for i in range(h):
    for j in range(w):
        histogram[img[i][j]]+=1 

for i in range(256):
    histogram[i] = histogram[i]/histogram_div

histacc = [0 for _ in range(256)]

for i in range(1, 256):
    histacc[i] = histacc[i-1]+histogram[i]
manual_histogram = img.copy()
for i in range(h):
    for j in range(w):
        manual_histogram[i][j] = (255*(histacc[manual_histogram[i][j]]))
output_img = np.hstack([img, manual_histogram])
cv2.imwrite("output/side_by_side.jpg", output_img)
