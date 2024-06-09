import cv2
import numpy as np

def carregar_imagem(img):
    img = cv2.imread(img)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img



def filtro_media(imagem, tamanho_kernel):
    altura, largura, _ = imagem.shape  # Adicionando o terceiro elemento para lidar com canais de cor
    pad = tamanho_kernel // 2
    img_filtrada = np.zeros_like(imagem, dtype=np.float32)  # Usamos float32 para evitar overflow

    for i in range(pad, altura - pad):
        for j in range(pad, largura - pad):
            janela = imagem[i - pad:i + pad + 1, j - pad:j + pad + 1]
            for k in range(3):  # Iterar sobre os canais de cor (R, G, B)
                img_filtrada[i, j, k] = np.mean(janela[:, :, k])

    img_filtrada = np.uint8(img_filtrada)  # Convertendo de volta para uint8 (imagem em cores)
    return img_filtrada




img = carregar_imagem('images/nature.jpg')
image_resize = cv2.resize(img, (600, 600), interpolation=cv2.INTER_AREA)
img_filtrada = filtro_media(image_resize, 5)
cv2.imshow('imagem original', image_resize)
cv2.imshow('media ', img_filtrada)
cv2.waitKey(0)