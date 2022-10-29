"""Determinar cuales y cuantos números perfectos hay entre 1 y 1000?"""

suma = 0
cont = 0

for n in range(1,101):
    for i in range(1,n):
        if n % i == 0:
            suma += i
        if suma == n:
            cont += 1
            print (n)
print(cont)          