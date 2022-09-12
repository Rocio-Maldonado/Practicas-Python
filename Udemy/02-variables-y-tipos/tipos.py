#Tipos de Datos
nada = None
cadena = "Hola soy Rocio"
cadena = "Desarrollador web"
entero = 99
flotante = 4.2
booleano = False
lista = [10 ,20 ,30, 100, 200]
listastring = [10, "treinta", 20, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre" : "Rocio",
    "apellido": "Maldonado",
    "curso" : "Master en pyhton"
}
rango = range(9)
dato_byte = b"probando"

#imprimir variable
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))

#convertir datos
texto = "Hola soy un texto"
numerito = str(123)
print(texto + " " + numerito)
print(type(numerito))

numerito = int(123)
print(type(numerito))

numerito = float(123)
print(type(numerito))