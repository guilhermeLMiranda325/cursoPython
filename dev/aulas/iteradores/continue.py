print()
print("Inicio")
i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue
    print(i)
    if(i > 5):
        break
else:
    print("Else")
print("Fim")
print()