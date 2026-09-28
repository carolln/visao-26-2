import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def min_filter(img: cv2.typing.MatLike, kernel_size: int=3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.erode(img, kernel)

def max_filter(img: cv2.typing.MatLike, kernel_size: int=3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.dilate(img, kernel)
assert len(sys.argv) >= 3, "uso: atenuarRuido.py <Imagem original> <Número do ruído [0,5]>"
imgOriginal = cv2.imread(sys.argv[1], 0)
# print(sys.argv)

k = int(sys.argv[2])
assert imgOriginal is not None, "Imagem original invalida"
img = cv2.imread('img/ruido' + str(k) + '.png', 0)
assert img is not None, "Imagem com ruido inválida"
if k == 0:
    imgResultante = cv2.medianBlur(img, 3)
if k == 1:
    #imgResultante = cv2.GaussianBlur(img, (3, 3), 0)
    imgResultante = cv2.bilateralFilter(img, 7, 15, 15)
    # deixei o bilateral porque ficou com um psnr melhor!
elif k == 2:
    imgResultante = cv2.medianBlur(img, 3)
    # o filtro da mediana teve o melhor resultado
elif k == 3:
    imgResultante = cv2.medianBlur(img, 3)
elif k == 4:
    imgResultante = cv2.GaussianBlur(img, (7, 7), 0)
    #imgResultante = cv2.bilateralFilter(img, 12, 32, 32)
    # o ultimo e o primeiro tao com melhores indices mas eu achei esse segundo bem mais bonito!!

    #imgResultante = cv2.bilateralFilter(img, 25, 60, 60)
elif k == 5:
    imgResultante = cv2.medianBlur(img, 5)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(imgResultante, cmap='gray')
plt.title('PSNR = ' + str("%.2f" % cv2.PSNR(imgResultante, imgOriginal)))
# plt.show()
plt.savefig("comps/comp" + str(k) + ".png")
cv2.imwrite("saidas/saida"+ str(k) + ".png", imgResultante)
