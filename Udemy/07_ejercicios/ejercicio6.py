"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla  y luego las multiplicaciones
"""

print("*******************Tablas de Multiplicar*******************")

resultado = 0
multiplicador = 1
n=1

for n in range(1,11):
    print(f"tabla del {multiplicador}")
    for n in range(1,11):
        resultado = multiplicador * n
        print(f"{multiplicador} x {n}= {resultado}")
        n+=1
    multiplicador+=1
    
## A better way:

for cabecera in range(1,11):
    print("*******************************")
    print(f"*********Tabla del {cabecera}**********")
    print("*******************************")
    
    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")
    


  
