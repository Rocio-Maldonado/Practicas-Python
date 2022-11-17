"""
#FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES


"""
contador=0
resultado = 0

for contador in range (0,5):
    print("voy por el " +str (contador))

    resultado += contador

print(f' el resultado es: {resultado}')

#ejemplo tablas de multiplicar

print("#############ejemplo##############")

numero_usuario= int(input("De que numero quieres ver la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1

print(f"\n####TABLA DE MULTIPLICAR DEL NUMERO{numero_usuario}###")
for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("no se pueen mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Operacion finalizada")






