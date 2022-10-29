"""3. Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene.
    Cuando el número exceda los límites emita un mensaje y finalice el programa"""

num1 = int(input("Escriba un número entre 0 y 9999\n"))
if num1 >=0 and num1<10000:
    if num1<10:
        print ("El número tiene 1 cifras")
    elif num1<100:
        print ("El número tiene 2 cifras")
    elif num1<1000:
        print ("El número tiene 3 cifras")
    else:
        print ("El número tiene 4 cifras")
else:
    print("El número digitado no esta entre 0 y 9999\n Fin del programa")
