def maior_elemento(lista):
    maiorvalor = 0
    for x in lista:
        if x > maiorvalor:
            maiorvalor = x
    return maiorvalor
