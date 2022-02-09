largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = 1
n = 1
while i <= altura:
    while n <=largura:
        print("#", end = "")
        n = n+1
    i = i + 1
    print()
    n = 1
    
