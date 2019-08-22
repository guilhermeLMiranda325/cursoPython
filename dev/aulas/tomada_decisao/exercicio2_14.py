num = float(input("Insira um número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if(num < num2 and num < num3):
    if(num2 < num3):
        print(num, num2, num3)
    else:
        print(num, num3, num2)
elif(num2 < num and num < num3):
    if(num < num3):
        print(num2, num, num3)
    else:
        print(num2, num3, num)
else:
    if(num < num2):
        print(num3, num2, num)
    else:
        print(num3, num2, num)