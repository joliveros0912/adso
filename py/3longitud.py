from turtle import clear


#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el
# número exceda los límites emita un mensaje y finalice el programa

n = int(input("Escriba un número entre 0 y 9.999: "))

if n < 0 or n > 9999:
    print ("El número excede los limites permitidos!")
else: print (len(str(n)))