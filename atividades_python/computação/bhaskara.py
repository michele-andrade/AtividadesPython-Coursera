import math
a = float(input("Digite o valor do coeficiente a "))
b = float(input("Digite o valor do coeficiente b "))
c = float(input("Digite o valor do coeficiente c "))
delta = (b**2) - (4*a*c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raiz1 = (- b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    if delta == 0:
       print("a raiz desta equação é", raiz1)
    else:
        if raiz1 < raiz2: 
           print("as raízes da equação são", raiz1, raiz2)
        else:
           print("as raízes da equação são", raiz2, raiz1)

