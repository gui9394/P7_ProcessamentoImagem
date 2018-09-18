from PIL import Image


def get_pixels_vizinhos(imagem, xy):
    """
    Retorna uma lista com os valores dos pixel entorno das coordenadas 'x y', incluindo ele.
    :param imagem: Image
    :param xy: tuple
    :return: list
    """

    x = xy[0]
    y = xy[1]

    x_max = imagem.size[0]
    y_max = imagem.size[1]

    lista = list()

    for x_temp in range(x - 1, x + 2):
        for y_temp in range(y - 1, y + 2):
            if ((x_temp > -1) & (x_temp < x_max) & (y_temp > -1) & (y_temp < y_max)):
                coordenadas = (x_temp, y_temp)
                lista.append(imagem.getpixel(coordenadas))

    return lista


def filtro_mediana(imagem: Image):
    """
    Retorna a imagem com o filtro de mediana aplicado.
    :param imagem: Image
    :return: Image
    """

    def mediana(lista:list):
        """
        Retorna a mediana de uma lista de valores.
        :param lista: list
        :return: int
        """

        lista.sort() # ordena lista de forma crescente
        tamanho_lista = len(lista)

        # Lista com quantidade de itens par
        if (tamanho_lista % 2) == 0:
            return lista[tamanho_lista // 2]
        # Lista com quantidade de itens impar
        else:
            idx = tamanho_lista // 2
            return (lista[idx] + lista[idx + 1]) // 2

    nova_imagem = Image.new("L", imagem.size) # nova imagem

    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            coodernadas = (x, y)
            pixels_vizinhos = get_pixels_vizinhos(imagem, coodernadas)
            nova_imagem.putpixel(coodernadas, mediana(pixels_vizinhos))

    return nova_imagem


def filtro_media(imagem: Image):
    """
    Retorna a imagem com o filtro media aplicado.
    :param imagem: Image
    :return: Image
    """

    def media(lista:list):
        """
        Retorna media dos valores dos itens de uma lista(sem casas decimais).
        :param lista: list
        :return: int
        """
        return (sum(lista)//len(lista))

    nova_imagem = Image.new("L", imagem.size) # nova imagem

    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            coodernadas = (x, y)
            pixels_vizinhos = get_pixels_vizinhos(imagem, coodernadas)
            nova_imagem.putpixel(coodernadas, media(pixels_vizinhos))

    return nova_imagem

# Carregando imagem
img = Image.open("0.jpeg")

# Aplicando filtro media
img0 = filtro_media(img)
img0.save("out_media.png", "png")

# Aplicando filtro mediana
img1 = filtro_mediana(img)
img1.save("out_mediana.png", "png")