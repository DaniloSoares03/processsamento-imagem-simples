import cv2
from PIL import Image

img = cv2.imread('images/nature.jpg')
image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)

img_horizontal = cv2.flip(image_resize, 1)

cv2.imshow('original', image_resize)

cv2.imshow('opencv horizontal', img_horizontal)

imagem_pil = Image.fromarray(cv2.cvtColor(image_resize, cv2.COLOR_BGR2RGB))

img_vertical_pillow = imagem_pil.transpose(Image.FLIP_TOP_BOTTOM)

img_vertical_pillow.show()

cv2.waitKey(0)
