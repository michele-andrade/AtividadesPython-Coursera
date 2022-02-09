def  ordenada ( lista ):
    next  =  0
    for i in range(len(lista)):
        próximo  =  i  +  1
        if próximo < len(lista):
            if lista[i] > lista[próximo]:
                return False
    return True
