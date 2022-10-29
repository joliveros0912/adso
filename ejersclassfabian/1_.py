# Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#3aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista."""
import random
vec=[]
cont1=0
suma=0
prom1=0
rdm=random.randint(10,25)
for i in range(rdm):
    vec.insert(i, round(random.random()*100))
    cont1+=1
    suma+=vec [i]
    prom1=suma//cont1
print("lista",vec)
print("promedio=",prom1)
for i in range(len(vec)):
    if vec[i]==prom1:
        print(vec[i],"es igual al promedio")
    elif vec[i]>prom1:
        print(vec[i],"es mayor al promedio")
    elif vec [i]<prom1:
        print(vec[i],"es menor al promedio")