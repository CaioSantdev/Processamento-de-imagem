import cv2
import numpy as np

def adicao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    novaImagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                novaImagem[x, y] += imagem1[x, y]
            
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                novaImagem[x, y] += imagem2[x, y]

    cv2.imwrite('resultadoSoma.png', novaImagem)

def subtracao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    novaImagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                novaImagem[x, y] += imagem1[x, y]
            
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                novaImagem[x, y] -= imagem2[x, y]

    cv2.imwrite('resultadoSubtracao.png', novaImagem)

adicao('./imagens/image.png', './imagens/imgBinaria.png')
subtracao('./imagens/image.png', './imagens/imgBinaria.png')