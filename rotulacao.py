from PIL import Image
from collections import deque

def rotulacao(caminhoImagem):
    imagem = Image.open(caminhoImagem).convert("RGB")
    largura, altura = imagem.size
    
    imagemRotulada = Image.new("RGB", (largura, altura))
    pixelsImagem = imagem.load()
    pixelsImagemRotulada = imagemRotulada.load()

    visitado = [[False for _ in range(altura)] for _ in range(largura)]
    
    coresRotulos = [
        (255, 0, 0),    # Vermelho
        (0, 255, 0),    # Verde
        (0, 0, 255),    # Azul
        (255, 255, 0),  # Amarelo
        (255, 0, 255),  # Magenta
        (0, 255, 255)   # Ciano
    ]
    
    corIndex = 0

    def flood_fill(x, y, corRotulo):
        queue = deque([(x, y)])
        visitado[x][y] = True
        while queue:
            px, py = queue.popleft()
            pixelsImagemRotulada[px, py] = corRotulo
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = px + dx, py + dy
                if 0 <= nx < largura and 0 <= ny < altura:
                    if not visitado[nx][ny] and pixelsImagem[nx, ny] == (0, 0, 0):  # Somente pixels pretos
                        visitado[nx][ny] = True
                        queue.append((nx, ny))

    for x in range(largura):
        for y in range(altura):
            if pixelsImagem[x, y] == (0, 0, 0) and not visitado[x][y]:
                flood_fill(x, y, coresRotulos[corIndex % len(coresRotulos)])
                corIndex += 1
    
    imagemRotulada.save('imagemRotulada.png')

rotulacao('./imagens/image copy.png')
