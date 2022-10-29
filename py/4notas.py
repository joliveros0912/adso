from turtle import clear

"""Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente,
Suficiente, Bien, etc. Use la escala que prefiera,
pero cerciórese que tiene 5 valores"""

nota = float(input("Ingrese nota "))

if nota >= 0:
    nota1 = "Insuficiente"
if nota >= 2:
    nota1 = "Deficiente"
if nota >= 5:
    nota1 = "Bien"
if nota >= 7:
    nota1 = "Sobresalente"
if nota >= 9:
    nota1 = "Excelente"
if nota < 0 or nota > 10:
    print ("Error")
    exit()
print (nota1)