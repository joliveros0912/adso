"""Escribir un programa que visualice la siguiente figura, utilizando ciclos.
El usuario decide cuantas líneas quiere imprimir

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *"""

x = int(input("Cuantas lineas desea imprimir? "))
a = "* "

for i in range(x):
        print(a)
        a += "* "