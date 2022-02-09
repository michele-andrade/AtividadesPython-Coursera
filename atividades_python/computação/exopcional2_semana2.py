segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = segundos // 86400
segundosrestantes = segundos % 86400
horas = segundosrestantes // 3600
segundosrestantes_a = segundosrestantes % 3600
minutos = segundosrestantes_a // 60
segundosfinal = segundosrestantes_a % 60

print(dia, "dias,", horas, "horas,", minutos, "minutos e", segundosfinal, "segundos.")
