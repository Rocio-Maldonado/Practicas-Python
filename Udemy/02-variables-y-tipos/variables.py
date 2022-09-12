""""
Una variable es un contenedor de informacion 
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""

#Crear variables y asignarle un valor
texto = "Master en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

#MOstrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("*************************")

#Sustitui el valor de algunas variables
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("*************************")

#Concatenacion
nombre = "Rocio"
apellidos = "Maldonado"
web="rociomaldonado.com"

print(nombre + " " + apellidos + " - " + web)
print(f'{nombre} {apellidos} - {web}')
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
print(nombre, apellidos, web)