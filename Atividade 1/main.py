from PIL import Image


def get_pixels_vizinhos(imagem, xy):
    """
    Retorna uma lista com os valores dos pixel entorno das coordenadas X e Y, incluindo ele
    :param imagem: Image
    :param xy: tuple
    :return: list
    """

    x = xy[0]  # Coodernada do X pixel atual
    y = xy[1]  # Coodernada do Y pixel atual

    x_max = imagem.size[0]  # Coodernada maxima eixo Y
    y_max = imagem.size[1]  # Coodernada maxima eixo X

    lista = list()  # Cria uma lista vazia

    # Percorre os pixels ao redor das coodernadas
    for x_temp in range(x - 1, x + 2):
        for y_temp in range(y - 1, y + 2):
            # Verifica se as coodernadas são válidas
            if ((x_temp > -1) & (x_temp < x_max) & (y_temp > -1) & (y_temp < y_max)):
                coordenadas = (x_temp, y_temp)
                lista.append(imagem.getpixel(coordenadas))

    # Retorna os pixels válidos
    return lista


def mediana(imagem):
    """
    Retorna a imagem com o filtro de mediana aplicado
    :param imagem: Image
    :return: Image
    """

    def calculo_mediana(lista):
        """
        Retorna a mediana de uma lista de valores
        :param lista: list
        :return: int
        """

        lista.sort()  # ordena lista de forma crescente
        tamanho_lista = len(lista)

        # Lista com quantidade de itens par
        if (tamanho_lista % 2) == 0:
            return lista[tamanho_lista // 2]
        # Lista com quantidade de itens impar
        else:
            idx = tamanho_lista // 2
            return (lista[idx] + lista[idx + 1]) // 2

    # Nova imagem
    nova_imagem = Image.new("L", imagem.size)

    # Percorre toda a imagem
    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            coodernadas = (x, y)
            pixels_vizinhos = get_pixels_vizinhos(imagem, coodernadas)
            nova_imagem.putpixel(coodernadas, calculo_mediana(pixels_vizinhos))

    # Retorna a imagem com o filtro aplicado
    return nova_imagem


def media(imagem):
    """
    Retorna a imagem com o filtro media aplicado
    :param imagem: Image
    :return: Image
    """

    def calculo_media(lista):
        """
        Retorna media dos valores dos itens de uma lista(sem casas decimais)
        :param lista: list
        :return: int
        """
        return (sum(lista) // len(lista))

    # Nova imagem
    nova_imagem = Image.new("L", imagem.size)

    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            coodernadas = (x, y)
            pixels_vizinhos = get_pixels_vizinhos(imagem, coodernadas)
            nova_imagem.putpixel(coodernadas, calculo_media(pixels_vizinhos))

    return nova_imagem


def histograma(imagem):
    """
    Retorna o histograma da imagem
    :param imagem: Image
    return: list
    """

    # Cria uma lista de 256 posições para corresponder a cada tom de cor
    lista = list(range(256))

    # Percorre toda a imagem
    for x in range(imagem.size[0]):
        for y in range(imagem.size[1]):
            # Soma + 1 a contagem do tom do pixel
            idx = imagem.getpixel((x, y))
            lista[idx] = lista[idx] + 1

    # Retorna a lista com a contagem dos tons de cor
    return lista


if __name__ == "__main__":
    while True:
        opcao = (input("\nMenu\n"
                      "1 - Aplicar filtro media\n"
                      "2 - Aplicar filtro mediana\n"
                      "3 - Histograma da imagem\n"
                      "0 - Sair\n"
                      "\n"
                      "Opção: "))[0]

        # Carregando imagem caso a opcao for válida
        if opcao in "123":
            print("\nCarregando a imagem")
            imagem = Image.open("imagem.jpeg")

            # Aplicando filtro media
            if opcao == "1":
                print("Aplicando o filtro media")
                nova_imagem = media(imagem)
                nova_imagem.save("out_media.png", "png")

            # Aplicando filtro mediana
            elif opcao == "2":
                print("Aplicando o filtro mediana")
                nova_imagem = mediana(imagem)
                nova_imagem.save("out_mediana.png", "png")

            # Histograma
            elif opcao == "3":
                print("Histograma da imagem")
                hist = histograma(imagem)
                for x in range(256):
                    print("tom {}: {}".format(x, hist[x]))

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida")