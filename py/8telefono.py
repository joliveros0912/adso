"""Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo 
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que 
permita calcular el costo de una llamada dados los minutos de duración"""

minutos = float(input("Cantidad de minutos: "))
banderazo = minutos * 200
costo = (minutos - 3) * 50

if minutos <= 3:
    print (banderazo)
else:
    banderazo = 3 * 200
    print (banderazo + costo)