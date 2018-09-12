from PIL import Image


def pixels_vizinhos(imagem: Image, xy:tuple):
    pixels = list()
    x_max = imagem.size[0]
    y_max = imagem.size[1]

    for x in range(xy[0]-1, xy[0]+2):
        for y in range(xy[1]-1, xy[1]+2):
            if ((x > -1) & (x < x_max) & (y > -1) & (y < y_max)):
                pixels.append(imagem.getpixel((x, y)))

    return pixels


def filtro_mediana(imagem:Image):
    def mediana(lista:list):
        lista.sort()
        tamanho_lista = len(lista)

        if (tamanho_lista % 2) == 0:
            return lista[tamanho_lista // 2]
        else:
            meio_0 = lista[tamanho_lista // 2]
            meio_1 = lista[(tamanho_lista // 2) + 1]
            return (meio_0 + meio_1) // 2

    nova_imagem = Image.new("L", imagem.size)

    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            nova_imagem.putpixel((x, y), mediana(pixels_vizinhos(imagem, (x, y))))

    return nova_imagem


def filtro_media(imagem:Image):
    def media(lista:list):
        return (sum(lista)//len(lista))

    nova_imagem = Image.new("L", imagem.size)

    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            nova_imagem.putpixel((x, y), media(pixels_vizinhos(imagem, (x, y))))

    return nova_imagem


img = Image.open("0.jpeg")

img0 = filtro_media(img)
img0.save("media.png", "png")

img1 = filtro_mediana(img)
img1.save("mediana.png", "png")


"""
histograma com grafico
"""