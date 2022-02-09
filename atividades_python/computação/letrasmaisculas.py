import string
def maiusculas(frase):
    letramaiscula = ""
    for letra in frase:
        if letra in string.ascii_uppercase:
            letramaiscula = letramaiscula + letra
    return letramaiscula
