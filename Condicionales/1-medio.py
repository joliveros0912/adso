""" 1.Pedir 3 numeros e indicar cual de ellos es el valor del medio.
    Ej 11, 2  1000, el valor del medio es 11.
    No use operadores lógicos"""
    
num1 = int(input("Escriba primer número:  "))
num2 = int(input("Escriba segundo número:  "))
num3 = int(input("Escriba tercer número:  "))
if num1 == num2:
    if num1 == num3:
        print("los números son iguales")
    else:
        print("El número del medio es: ",num1)
elif num2 == num3:
    print("El número del medio es: ",num2)
elif num3 == num1:
    print("El número del medio es: ",num1)
elif num1 < num2:
    if num1 < num3:
        if num2 < num3:
            print("el numero del medio es :",num2)
        else:
            print("el numero del medio es: ",num3)
elif num2 < num3:
    if num2 < num1:
        if num3 < num1:
            print("el numero del medio es :",num3)
        else:
            print("el numero del medio es: ",num1)
elif num3 < num2:
    if num3 < num1:
        if num2 < num1:
            print("el numero del medio es :",num2)
        else:
            print("el numero del medio es: ",num1)
