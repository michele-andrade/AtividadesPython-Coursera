numero = input("Digite um número grande: ")
n = len(numero)
valor = int(n)
numeronovamente = int(numero)
soma = 0
i = 0
while i <= n:
      x = numeronovamente % 10
      soma = soma + x
      numeronovamente = numeronovamente // 10
      i = i + 1
print("A soma dos digitos é: ", soma)
