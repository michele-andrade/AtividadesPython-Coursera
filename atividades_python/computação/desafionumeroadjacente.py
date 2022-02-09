numero = int(input("Digite um número inteiro: "))
adjacente = True
numeroconvertido = str(numero)
leituradonumero = len(numeroconvertido)

while leituradonumero > 1 and adjacente: 
      ind_1 = numero % 10
      divisor = numero // 10
      ind_2 = divisor % 10
      if ind_1 != ind_2:
         numero = divisor
         leituradonumero = leituradonumero - 1
      else: 
         adjacente = False
if not adjacente:
   print("sim")
else:
   print("não") 
