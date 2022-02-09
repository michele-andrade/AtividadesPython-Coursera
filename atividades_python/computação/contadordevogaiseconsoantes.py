def conta_letras(frase, contar="vogais"):
    ocorrencia = 0
    if contar == "vogais":
        for letra in frase:
            if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
                ocorrencia +=1
    elif contar == "consoantes":
        for letra in frase:
            if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != " ":
                ocorrencia +=1
    return ocorrencia 
