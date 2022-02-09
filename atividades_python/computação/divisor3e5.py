num = int(input("Digite um número inteiro: "))
div1 = num % 5 
div2 = num % 3
if (div1 == 0) and (div2 == 0):
   print("FizzBuzz")
else:
   print(num)