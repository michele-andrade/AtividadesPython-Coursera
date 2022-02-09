numero = int(input("Digite um número inteiro: "))
primo = True
divisor = 2
while divisor < numero and primo:
      if (numero % divisor) == 0:
         primo = False
      else:
         divisor = divisor + 1 
if primo and numero != 1:
   print("primo")
else:
   print("não primo")
