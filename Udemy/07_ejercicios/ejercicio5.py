"""
Ejercicio 5. Hacer un programa que muestre
todos los numeros entre dos numeros que diga el usuario
"""

n1 = int(input("Inserta el primer numero: "))
n2 = int(input("Inserta el segundo numero: "))

if n1 < n2:
    for n in range(n1, (n2+1)):
        print(n)
else:
    print("El numero 1 debe ser menor al numero 2")
