#definindo função do computador escolhe jogada
def computador_escolhe_jogada(n, m):
    computadortira = 1
    while computadortira != m:
        if (n - computadortira) % (m+1) == 0:
            return computadortira
        else:
            computadortira += 1
    return computadortira

#definindo função do usuario escolhe jogada
def usuario_escolhe_jogada(n, m):
    jogada = False
    while not jogada:
        jogadortira = int(input("Quantas peças você vai tirar? "))
        if jogadortira > m or jogadortira < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogada = True
    return jogadortira

#definindo função campeonato
def campeonato():
    rodada = 1
    while rodada <= 3:
        print()
        print("**** Rodada", rodada, "****")
        print()
        partida()
        rodada += 1
    print()
    print("Placar: Você 0 X 3 Computador")
        
#definindo função partida
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vezdocomputador = False
    if n % (m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        vezdocomputador = True
    while n > 0:
        if vezdocomputador:
            computadortira = computador_escolhe_jogada(n, m)
            n = n - computadortira
            if computadortira == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", computadortira, "peças")

            vezdocomputador = False
        else:
            jogadortira = usuario_escolhe_jogada(n, m)
            n = n - jogadortira
            if jogadortira == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogadortira, "peças")
            vezdocomputador = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()

print("1 - para jogar uma partida isolada")

tipoDePartida = int(input("2 - para jogar um campeonato "))

if tipoDePartida == 2:
    print()
    print("Voce escolheu um campeonato!")
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        print("Voce escolheu partida isolada!")
        print()
        partida()
