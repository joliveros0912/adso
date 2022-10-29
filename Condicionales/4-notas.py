""" 4. Pedir una nota de 0 a 10 y mostrarla de la forma:
    Insuficiente, Suficiente, Bien, etc.
    Use la escala que prefiera, pero cerciórese que tiene 5 valores."""

nota = int(input("Escriba la nota del 0 al 10\n"))
if nota<0:
    print("Ingreso un rango de nota no equivalente")
elif nota<=2:
    print("Insuficiente")
elif nota>2 and nota<=4:
    print("suficiente")
elif nota>4 and nota<=6:
    print("Bien")
elif nota>6 and nota<=8:
    print("Eficiente")
elif nota>8 and nota<=10:
    print("Excelente")
else:
    print("Ingreso un rango de nota no equivalente")