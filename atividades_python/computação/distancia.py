import math
ponto1 = float(input("Digite o ponto da coordenada x do plano cartesiano: "))
ponto2 = float(input("Digite o ponto da coordenada y do plano cartesiano: "))
ponto3 = float(input("Digite o outro ponto da coordenada x do plano cartesiano: "))
ponto4 = float(input("Digite o outro ponto da coordenada y do plano cartesiano: "))
raiz = ((ponto1 - ponto3)**2) + ((ponto2 - ponto4)**2)
distancia = math.sqrt(raiz)

if distancia >= 10:
   print("longe")
else:
   print("perto")

