import cv2
import numpy as np

img = cv2.imread("../img/foto06.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None
h, w = img.shape
limiar_img = np.full(shape=img.shape, fill_value=0, dtype=np.uint8)

limiar = int(input("digite o limiar\n"))

limiar = max(0, min(255, limiar))
limiar_img = np.where(img>limiar, 255, 0).astype(np.uint8)
cv2.imwrite("../output/limiar.jpg", limiar_img)