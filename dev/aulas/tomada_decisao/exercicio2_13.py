num = float(input("Insira um número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if(num > num2 and num > num3):
    print(num)
elif(num2 > num and num2 > num3):
    print(num2)
else:
    print(num3)