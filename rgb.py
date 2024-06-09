import cv2
import numpy as np

# Abre a imagem
img = cv2.imread("images/nature.jpg")

image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)

azul, verde, vermelho = cv2.split(image_resize)

img_azul = cv2.merge([azul, azul * 0, azul * 0])
img_verde = cv2.merge([verde * 0, verde, verde * 0])
img_vermelho = cv2.merge([vermelho * 0, vermelho * 0, vermelho])


cv2.imshow('imagem azul', img_azul)
cv2.imshow('imagem verde', img_verde)
cv2.imshow('imagem vermelha', img_vermelho)

cv2.imshow('imagem nova',image_resize)
cv2.waitKey(0)