# Processamento de imagens com OpenCv e Pillow

Trabalho de computação gráfica para teste de ferramentas de processamento de imagem.

### Binarização


- Este código faz a conversão de uma imagem colorida RGB para tons de cinza e em preto e branco. Para a binarização verificamos se o pixel selecionado na imagem em cinza é maior que 127, sendo ele maior, atribuimos o valor 255 para representar o branco na imagem.

```
def binarizacao(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_binaria = np.zeros_like(gray)
    img_binaria[gray > 127] = 255
     
    return img_binaria

```

### Cinza


- Este código faz a conversão da imagem RGB para o cinza utilizando a propriedade do OpenCV cvtColor, passando como parâmetro a imagem e a cor cinza.

```
img = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
```

### Girar

- Para girar a imagem foi utilizado a função rotate do OpenCV passando como parametro a imagem e o sentido para o lado a girar.


```
giro = cv2.rotate(image_resize, cv2.ROTATE_90_CLOCKWISE)
```

### Inverter

- Para inverter a imagem no sentido horizontal foi utilizado a função flip do OpenCV. Para inverter a imagem na vertical foi utilizado o Pillow para utilizar a funçaõ tranpose, passando como parâmetro a propriedade (`FLIP_TOP_BOTTO`), como foi feito a leitura da imagem utilizando OpenCV, teve que se fazer a conversão do tipo da imagem para ser manipulado pelo Pillow


```
img_horizontal = cv2.flip(image_resize, 1)

imagem_pil = Image.fromarray(cv2.cvtColor(image_resize, cv2.COLOR_BGR2RGB))
img_vertical_pillow = imagem_pil.transpose(Image.FLIP_TOP_BOTTOM)

```

### Média

- Para o calculo da média selecionamos a altura e largura da imagem para percorrer os pixels e fazer a operação, após isso é criado a área que será aplicado o filtro atribuindo a variável janela. Ao último loop é calculado o valor médio encontrado nessa janela com os pixels.


```
altura, largura, _ = imagem.shape
pad = tamanho_kernel // 2

for i in range(pad, altura - pad):
   for j in range(pad, largura - pad):
       janela = imagem[i - pad:i + pad + 1, j - pad:j + pad + 1]
       for k in range(3):  # Iterar sobre os canais de cor (R, G, B)
           img_filtrada[i, j, k] = np.mean(janela[:, :, k])
```

### Mediana 

- O cálculo da mediana é feito de maneira semelhante, fazendo o cálculo da mediana da nossa janela encontrada.


``` 
for i in range(pad, altura - pad):
    for j in range(pad, largura - pad):
        for k in range(canais):
            janela = imagem[i - pad:i + pad + 1, j - pad:j + pad + 1, k]
            mediana = np.median(janela)
            img_filtrada[i, j, k] = mediana

```

### RGB

- Para o cálculo dos canais RGB é utilizado a função split do OpenCV, onde é retornado os valores em tons de cinza para os três canais, após isso é utlizado a função merge para fazer a combinação dos canais em uma imagem colorida. Para isolar então os canais fazemos o merge com apenas os valores que queremos isolar, colorindo então a imagem com os valores RGB separados.

```
azul, verde, vermelho = cv2.split(image_resize)

img_azul = cv2.merge([azul, azul * 0, azul * 0])
img_verde = cv2.merge([verde * 0, verde, verde * 0])
img_vermelho = cv2.merge([vermelho * 0, vermelho * 0, vermelho])
```


