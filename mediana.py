import cv2
import numpy as np

def carregar_imagem(img):
    img = cv2.imread(img)
    return img

def filtro_mediana(imagem, tamanho_kernel):
    altura, largura, canais = imagem.shape
    pad = tamanho_kernel // 2
    img_filtrada = np.zeros_like(imagem)

    for i in range(pad, altura - pad):
        for j in range(pad, largura - pad):
            for k in range(canais):
                janela = imagem[i - pad:i + pad + 1, j - pad:j + pad + 1, k]
                mediana = np.median(janela)
                img_filtrada[i, j, k] = mediana

    return img_filtrada

img = carregar_imagem('images/nature.jpg')
image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)
img_filtrada = filtro_mediana(image_resize, 5)

cv2.imshow('Imagem Original', image_resize)
cv2.imshow('Filtro de Mediana', img_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()
