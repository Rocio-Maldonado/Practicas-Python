"""
#Condicional IF

SI se esta condicion:
    ejecutar grupo de instrucciones
SI NO: 
    Se ejecuta otro grupo de condiciones


if condicion:
    instrucciones
else:
    otras instrucciones



#OPERADORES DE CONTROL
== igual
=! diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

 """

 #EJEMPLO 1
print("*****************EJEMPLO 1*****************")

color = "rojo"
#color = input("Ingresa un color: ")

if color == "rojo":
    print("el color es ROJO")
else:
    print("El color no es ROJO")

    #EJEMPLO 2
print("*****************EJEMPLO 2*****************")

year = 2020
#year = int(input("En que anio estamos?"))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un anio anterior a 2021")


 #EJEMPLO 3
print("*****************EJEMPLO 3*****************")