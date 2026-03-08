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


transporte = [
    150.00,
    200.00,
    170.00,
    220.00,
    120.00,
    210.00,
    160.00,
    190.00,
    140.00,
    230.00,
]
print(f"Moda's -> {encontrarModa(listaNumeros=transporte)}")
