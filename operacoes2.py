import cv2
import numpy as np

def ajustar_tamanho(imagem1, imagem2):
    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    nova_imagem1 = np.zeros((largura, altura, 3), dtype=np.uint8)
    nova_imagem2 = np.zeros((largura, altura, 3), dtype=np.uint8)

    nova_imagem1[:imagem1.shape[0], :imagem1.shape[1]] = imagem1
    nova_imagem2[:imagem2.shape[0], :imagem2.shape[1]] = imagem2

    return nova_imagem1, nova_imagem2

def adicao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    imagem1, imagem2 = ajustar_tamanho(imagem1, imagem2)

    novaImagem = cv2.add(imagem1, imagem2)

    cv2.imwrite('resultadoSoma.png', novaImagem)

def subtracao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    imagem1, imagem2 = ajustar_tamanho(imagem1, imagem2)

    novaImagem = cv2.subtract(imagem1, imagem2)

    cv2.imwrite('resultadoSubtracao.png', novaImagem)

# Chamada das funções
adicao('./imagens/image.png', './imagens/imgBinaria.png')
subtracao('./imagens/image.png', './imagens/imgBinaria.png')
