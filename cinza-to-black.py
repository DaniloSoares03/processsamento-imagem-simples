import cv2
import numpy as np


def binarizacao(img):
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     img_binaria = np.zeros_like(gray)
     img_binaria[gray > 127] = 255
     
     return img_binaria


def openImage(img):
    img = cv2.imread(img)

    image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)
    return image_resize


def opencvBinary(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('imagem original', img)
    cv2.imshow('tons de cinza', gray)
    cv2.imshow('preto e branco', img_b)
    cv2.waitKey(0)


img = openImage('images/nature.jpg')
opencvBinary(img)

img_binary = binarizacao(img)

cv2.imshow('binarizacao', img_binary)
cv2.waitKey(0)