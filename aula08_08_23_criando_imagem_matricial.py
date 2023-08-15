import numpy as np
import cv2
import math

#criar uma imagem em tons de cinza
imagem = np.zeros((200, 200), np.uint8)

#exibindo a image
cv2.imshow("Imagem 1", imagem)

#se IDLE ou Anaconda:
#cv2.imshow('janela1', imagem)

imagem[100:121, 100:121]=255
imagem[130:151, 100:121]=137
cv2.imshow("Imagem 2", imagem)

# criar uma imagem com 3 canais (canais de cores)
color = np.ones((200, 200, 3), np.uint8) * 150
cv2.imshow("Imagem 3", color)

#os canais de cores em openCV são na ordem: BGR (0, 1, 2)

color[50:101, 100:121, 0] = 255
color[50:101, 100:121, 1] = 0
color[50:101, 100:121, 2] = 0

cv2.imshow("Imagem 4", color)

color = cv2.line(color, (0,0), (200, 200), (17,200,180), 8)

cv2.imshow("Imagem 5", color)

"""Exercício 1. Praticar os comandoas para a criação de uma imagem com os seguintes elementos:

*   Céu
*   Montanhas
*   Sol brilhando
*   Gramado


"""

paisagem = np.ones((200, 200, 3), np.uint8) * 150

paisagem[0:160, 0:200, 0] = 255
paisagem[0:160, 0:200, 1] = 187
paisagem[0:160, 0:200, 2] = 84

paisagem[160:200, 0:200, 0] = 0
paisagem[160:200, 0:200, 1] = 87
paisagem[160:200, 0:200, 2] = 36

# Obtém as dimensões da imagem
height, width = paisagem.shape[:2]

# Coordenadas da imagem
center_x = width // 2
center_y = height // 5

# Raio do círculo
radius = 12

red_color = (0, 225, 255)

cv2.circle(paisagem, (center_x, center_y), radius, red_color, -1)

# numero de raios de sol
steps = 10
angle = 3.1415926 * 2 / steps

# raios de sol
for i in range(steps):
    x = (int(math.sin(angle * i) * 30)) + center_x
    y = (int(math.cos(angle * i) * 30)) + center_y
    cv2.line(paisagem, (center_x, center_y), (x, y), (0, 225, 255), 1)


for i in range(80):
  paisagem = cv2.line(paisagem, (40,50), (i, 160), (77,119,143), 8)

for i in range(80):
  paisagem = cv2.line(paisagem, (140,100), (i+100, 176), (77,119,143), 8)


cv2.imshow("Paisagem", paisagem)
cv2.waitKey(0)
cv2.destroyAllWindows()