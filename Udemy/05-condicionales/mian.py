"""
#Condicional IF

SI se cumple la condicion
    Ejecutar grupo de instrucciones
SI NO 
    Se ejecuta otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

#Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor igual que
>= mayor igual que
"""

#Ejemplo1
print("***********EJEMPLO 1*************")
color = "azul"
#color = input("Adivina mi color favorito: ")

if color == "azul":
    print("Felicidades \n")
    print("El color es AZUL")
else:
    print("Color incorrecto!")

#Ejemplo2
print("\n***********EJEMPLO 2*************")
#year = 2020
year= int(input("\nEn que anio estamos? "))

if year <= 2021: 
    print("Estamos antes de 2021")
else:
    print("Es un anio posterior a 2021")
