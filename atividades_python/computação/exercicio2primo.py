def éprimo(k):
    i = 1
    while i<k:
        div = k%i
        i = i + 1
        if (k % i)==0:
            k = k - 1
        else:
            numeroprimo = k
    return(numeroprimo)

            
def maior_primo(k):
    primo = éprimo(k)
    return(primo)

