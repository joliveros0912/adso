"""Determinar los divisores de un número introducido por teclado"""

n = int(input("Ingrese un numero. "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)