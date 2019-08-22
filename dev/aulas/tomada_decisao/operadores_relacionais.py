numero1 = input("Digite um número: ")
numero1 = int(numero1)

numero2 = input("Digite o segundo número: ")
numero2 = int(numero2)

if(numero1==numero2):#operador de igualdade
    print("O número %d é igual a %d. "%(numero1, numero2))
if(numero1!=numero2):#operador de diferença
    print("O número %d é diferente de %d "%(numero1, numero2))
if(numero1<numero2):#operador menor que
    print("O número %d é menor que o %d "%(numero1, numero2))
if(numero1>numero2):#operador de maior que
    print("O número %d é maior que o %d "%(numero1,numero2))
if(numero1>=numero2):#operador maior ou igual que
    print("O número %d é maior ou igual que %d "%(numero1, numero2))
if(numero1<=numero2):#operador menor ou igual que
    print("O número %d é menor ou igual que %d "%(numero1, numero2))