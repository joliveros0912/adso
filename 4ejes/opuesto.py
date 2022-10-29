"""pedir numeros, imprimirlo con el opuesto"""
n=1
contador=0

while n !=0:
    n=int(input("ingrese un numero"))
    if n !=0:
        print(n,"opuesto",-(n))
        contador+=1
    if n ==0: 
        print("el programa a finalizado")
print("se han ingresado",contador,"numeros")