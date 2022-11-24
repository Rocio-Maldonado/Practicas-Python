"""
Ejercicio 7. Hacer iun programa que muestre todos los 
numeros impares entre dos numeros que elija el usuario
"""

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("ingresa el segundo numero: "))

if n1 < n2:
    for n in range(n1,n2+1):
        if n%2 == 1:
            print (n)
        n+=1
else:
    print("el primer numero debe ser menor al segundo numero")