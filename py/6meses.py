"""Pida un numero al usuario que representa días del año. Diga a que mes
del año corresponde así. Si el número es menor o igual a 31 indica que
esta en enero, Pero si el número por ejemplo es 32 indica que es el 1 de
febrero. No tenga en cuenta si el año es bisiesto, es decir siempre
febrero tiene 28 días."""

n = int(input("Inserte un número "))

if n > 365:
    print ("No aplica")
    exit()
if n > 0:
    mes = "enero"
    a = 31
if n > a:
    mes = "febrero"
    a += 28
if n > a:
    mes = "marzo"
    a += 31
if n > a:
    mes = "abril"
    a += 30
if n > a:
    mes = "mayo"
    a += 31
if n > a:
    mes = "junio"
    a += 30
if n > a:
    mes = "julio"
    a += 31
if n > a:
    mes = "agosto"
    a += 31
if n > a:
    mes = "septiembre"
    a += 30
if n > a:
    mes = "octubre"
    a += 31
if n > a:
    mes = "noviembre"
    a += 30
if n > a:
    mes = "diciembre"

print (mes)