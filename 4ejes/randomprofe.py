from operator import contains
from random import random

import random
tam=int(input("cantidad"))
contador1=0
contador2=0
sumapar=0
sumaimpar=0
vec=[]
for i in range(tam):
    vec.insert(i, round(random.random()*100))
print(vec)
for i in range(len(vec)):
    if vec [i]%2==0:
        print(vec[i],"es par")
        contador1+=1
        sumapar+=vec[i]
    else:
        print(vec[i],"impar")
        contador2+=1
        sumaimpar+=vec[i]
print("pares hay",contador1)
print("impares hay",contador2)
print("la suma de los numeros pares es=",sumapar)
print("la suma de los numeros impares es=",sumaimpar)
promediopar=sumapar//contador1
promedioimpar=sumaimpar//contador2
print("promedio de pares es=",promediopar)
print("promedio de impares es=",promedioimpar)