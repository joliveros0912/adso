# Escribe un programa que pida tres números y que escriba si
# son los tres iguales, si hay dos iguales o si son los tres distintos

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b and c == b:
    print ("los 3 números son iguales")
    exit()
if a == b or c == b or c == a:
    print ("Hay dos números iguales")
else: print ("Los 3 números son distintos")