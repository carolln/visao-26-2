import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def min_filter(img: cv2.typing.MatLike, kernel_size: int=5):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.erode(img, kernel)
def calc_raio_centro(img: cv2.typing.MatLike) -> (int, int, int):
    m, n = img.shape
    max_contig_start_i = 0
    max_contig_start_j = 0
    max_contig_len = 0
    for i in range(m):
        contig = 0
        contig_start_i = 0
        contig_start_j = 0
        for j in range(n):
            if img[i][j] > 250:
                if contig == 0:
                    contig_start_i = i
                    contig_start_j = j
                contig+=1
                if contig >= max_contig_len:
                    max_contig_len = contig
                    max_contig_start_i = contig_start_i
                    max_contig_start_j = contig_start_j
            else:
                contig = 0
    center_x = round((max_contig_start_j)+(max_contig_len/2))
    center_y = max_contig_start_i
    raio = round(max_contig_len/2)
    return (center_x, center_y, raio)
                
    
assert len(sys.argv) >= 5, "uso: tarefa.py <Imagem> <centro x> <centro y> <raio original>"
imgOriginal = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
assert imgOriginal is not None, "Imagem invalida"

raio = float(sys.argv[4])
(x, y) = (float(sys.argv[2]), float(sys.argv[3]))
imgFiltrada = min_filter(imgOriginal)
cv2.imwrite("out/filtro_min.png", imgFiltrada)
(cx, cy, r) = (calc_raio_centro(imgFiltrada))
print((cx, cy, r))
imgCor = cv2.cvtColor(imgFiltrada, cv2.COLOR_GRAY2BGR)
imgCircle = cv2.circle(imgCor, (cx, cy), r, (0, 255, 0), 2)
cv2.imwrite("out/filtro_min_circle.png", imgCircle)


# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.subplot(1, 2, 2)
# plt.imshow(imgResultante, cmap='gray')
# plt.title('PSNR = ' + str("%.2f" % cv2.PSNR(imgResultante, imgOriginal)))
# # plt.show()
# plt.savefig("comps/comp" + str(k) + ".png")
# cv2.imwrite("saidas/saida"+ str(k) + ".png", imgResultante)
