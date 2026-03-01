def contarElementos(
    listaNumeros, dicionarioQuantidades
):  # Conta e retorna um dicionario contado
    for number in listaNumeros:
        if number in dicionarioQuantidades:
            dicionarioQuantidades[number] += 1
        else:
            dicionarioQuantidades[number] = 1

    return dicionarioQuantidades


def encontrarModa(listaNumeros):  # Encontra a moda
    # Identificar multiplos valores maiores
    dicionarioQuantidades = dict()

    contarElementos(
        listaNumeros=listaNumeros, dicionarioQuantidades=dicionarioQuantidades
    )

    quantidadeDoElementoMaisRepetido = (
        0  # Gambiarra para guardar de forma externa ao loop o dado
    )
    indicesMaisRepetido = list()  # Possibilidade de pegar varias modas
    for indices in dicionarioQuantidades.keys():
        if dicionarioQuantidades[indices] > quantidadeDoElementoMaisRepetido:
            quantidadeDoElementoMaisRepetido = dicionarioQuantidades[indices]
            indicesMaisRepetido.clear()
            indicesMaisRepetido.append(indices)

        elif dicionarioQuantidades[indices] == quantidadeDoElementoMaisRepetido:
            indicesMaisRepetido.append(indices)

    return indicesMaisRepetido


arr = [1, 1, 1, 12, 3, 4, 5, 3, 2, 1]
print(f"Moda's -> {encontrarModa(listaNumeros=arr)}")
