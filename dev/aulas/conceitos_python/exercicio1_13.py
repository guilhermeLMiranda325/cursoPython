dias = int(input("Insira a quantidade em dias:"))
horas = int(input("Insira a quantidade em horas:"))
minutos = int(input("Insira a quantidade em minutos:"))
segundos = int(input("Insira a quantidade em segundos:"))

dias_segundos = dias * 86400
horas_segundos = horas * 3600
minutos_segundos = minutos * 60
soma = dias_segundos + horas_segundos + minutos_segundos + segundos

print("O total em segundos é:", soma)