import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def errocentro(par1, par2):
    return np.sqrt(((par1[0] - par2[0]) ** 2) +( (par1[1] - par2[1])**2))

def erroraio(r1, r2):
    return abs(r1-r2)

def errototal(par1, par2, r1, r2):
    return errocentro(par1, par2) + erroraio(r1,r2)

img = cv2.imread(sys.argv[1], 0)

vals = np.unique(img)


coordgt = (int(sys.argv[2]), int(sys.argv[3]))
rgt = int(sys.argv[4])
print(coordgt, rgt)

vals.sort()

#print(vals) #tem que ser 2 pelas especificacoes
# print(vals)

lista = []

# print(vals.shape)
# print(img.shape)


for i in range(img.shape[0]):
    pera = 0
    for j in range(img.shape[1]):
        if (img[i][j] == vals[1]):
            pera +=1
    if (pera != 0):
        lista.append((pera,i))

lista2 = []
for j in range(img.shape[1]):
    pera = 0
    for i in range(img.shape[0]):
        if (img[i][j] == vals[1]):
            pera +=1
    if (pera != 0):
        lista2.append((pera,j))

lista.sort()
lista2.sort()

# print(lista)
# print(lista2)

coords = (lista2[-1][1], lista[-1][1]) # coordenadas

# print(coords)

# diferenca de 
r = int((lista[-1][0] + lista2[-1][0])/4) # a media pra dar mais seguranca

print("coordenadas estimadas: " + str(coords))
print("coordenadas reais: " + str((coordgt)))
print("raio estimado: " + str(r))
print("raio real: " + str(rgt))
print("erro centro:" + str(errocentro(coords, coordgt)))
print("erro raio: " + str(erroraio(r, rgt)))
print("erro total: " + str(errototal(coords, coordgt, r, rgt)))


imgCor = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
imgCircle = cv2.circle(imgCor, (coords[0], coords[1]), r, (0, 255, 0), 2)
cv2.imwrite("out/clear.png", imgCircle)
