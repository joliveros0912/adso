#Diseñar un programa que calcule área, logitud, diametro y
# circunferencia de un círculo

radio = float(input("radio = "))
pi = 3.1416

area = pi * radio**2
lon = 2 * pi * radio
dia = pi * 2
cir = pi * dia

print ("El área del círculo es: ", area)
print ("La longitud del círculo es: ", lon)
print ("El diametro del círculo es: ", dia)
print ("La circunferencia del círculo es: ", cir)