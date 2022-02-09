def busca(lista, elemento):
    primeiro  =  0
    ultimo =  len(lista) -  1
    while primeiro <= ultimo:
        i = (primeiro + ultimo) // 2
        print(i)
        if lista[i] == elemento:
            return i
        else:
            if lista[i] > elemento:
                ultimo = i -1
            else:
                primeiro = i + 1
    return False 
