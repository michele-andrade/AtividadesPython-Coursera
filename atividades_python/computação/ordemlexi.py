def primeiro_lex(lista):
    contador = lista[0]
    for string in lista:
        if string < contador:
            contador = string
    return contador
            
