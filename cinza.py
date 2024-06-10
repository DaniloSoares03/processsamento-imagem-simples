import cv2

img = cv2.imread('images/nature.jpg')

image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    
cv2.imshow('cinza', gray)
cv2.waitKey(0)