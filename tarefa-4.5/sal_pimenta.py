import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def errocentro(par1, par2):
    return np.sqrt(((par1[0] - par2[0]) ** 2) +( (par1[1] - par2[1])**2))

def erroraio(r1, r2):
    return abs(r1-r2)

def errototal(par1, par2, r1, r2):
    return errocentro(par1, par2) + erroraio(r1,r2)

def min_filter(img: cv2.typing.MatLike, kernel_size: int=3):
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
imgFiltrada = cv2.medianBlur(imgOriginal, 7)
cv2.imwrite("out/filtro_median.png", imgFiltrada)
# print(calc_raio_centro(imgFiltrada))
(cx, cy, r) = (calc_raio_centro(imgFiltrada))
print((cx, cy, r))
imgCor = cv2.cvtColor(imgFiltrada, cv2.COLOR_GRAY2BGR)
imgCircle = cv2.circle(imgCor, (cx, cy), r, (0, 255, 0), 2)
cv2.imwrite("out/filtro_med_circle.png", imgCircle)

print("coordenadas estimadas: " + str((cx, cy)))
print("coordenadas reais: " + str((x,y)))
print("raio estimado: " + str(r))
print("raio real: " + str(raio))
print("erro centro:" + str(errocentro((cx,cy), (x,y))))
print("erro raio: " + str(erroraio(r, raio)))
print("erro total: " + str(errototal((cx,cy), (x,y), r, raio)))


# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.subplot(1, 2, 2)
# plt.imshow(imgResultante, cmap='gray')
# plt.title('PSNR = ' + str("%.2f" % cv2.PSNR(imgResultante, imgOriginal)))
# # plt.show()
# plt.savefig("comps/comp" + str(k) + ".png")
# cv2.imwrite("saidas/saida"+ str(k) + ".png", imgResultante)
