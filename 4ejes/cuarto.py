"""..."""
import random
x=random.randint(1,10)
n=0
contador=0
while n != x:
    n=int(input("escriba un numero"))
    contador+= 1
    if n>x:
        print(n,"es muy grande")
    else:
        print(n,"es muy pequeño")
    if n==x:
        print("el numero era",n)
    print("numero de intentos:", contador)