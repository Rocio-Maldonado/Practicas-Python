"""
Ejercicio 2. Escribir un script que
nos muestre por pantalla todos los
numeros pares del 1 al 120
"""

divisor = 1
dividendo = 2

for numero in range(1, 120):
    cociente = divisor % dividendo
    divisor += 1

    if cociente != 0:
        print(divisor)
    numero += 1

"""
contador = 1

for contador in range (1,121):
    if contador%2 == 0:
        print (contador)
"""
