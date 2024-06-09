import cv2

img = cv2.imread('images/nature.jpg')
image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)

giro = cv2.rotate(image_resize, cv2.ROTATE_90_CLOCKWISE)



cv2.imshow('imagem 90 graus', giro)
cv2.waitKey(0)