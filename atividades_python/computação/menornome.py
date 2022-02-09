def menor_nome(nomes):
    nome_menor = ''
    tamanho_menor = 100
    for nome in nomes:
        nome = nome.lstrip()
        nome = nome.rstrip()
        
        tamanho_nome = len(nome)
        if tamanho_nome < tamanho_menor:
            tamanho_menor = tamanho_nome
            nome_menor = nome
        
        
    return nome_menor.capitalize()
