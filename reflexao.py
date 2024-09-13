import cv2

def reflexaoHorizontal(imagem):
    imagem = cv2.imread(imagem)
    altura, largura, _ = imagem.shape
    imagemReflexao = imagem.copy()

    for y in range(altura):
        for x in range(largura // 2):
            temp = imagemReflexao[y, x].copy()  
            imagemReflexao[y, x] = imagemReflexao[y, largura - 1 - x]  
            imagemReflexao[y, largura - 1 - x] = temp  

    cv2.imwrite('imagemReflexaoHorizontal.png', imagemReflexao)

def reflexaoVertical(imagem):
    imagem = cv2.imread(imagem)
    altura, largura, _ = imagem.shape
    imagemReflexao = imagem.copy()

    for x in range(largura):
        for y in range(altura // 2):
            temp = imagemReflexao[y, x].copy()  
            imagemReflexao[y, x] = imagemReflexao[altura - 1 - y, x]  
            imagemReflexao[altura - 1 - y, x] = temp  
    
    cv2.imwrite('imagemReflexaoVertical.png', imagemReflexao)

reflexaoHorizontal('./imagens/image.png')
reflexaoVertical('./imagens/image.png')

