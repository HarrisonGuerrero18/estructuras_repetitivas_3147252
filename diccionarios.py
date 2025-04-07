# Diccionarios:

# Son colecciones de datos.
# Cada elemento en un diccionario.
# Se puede dividir en 2 partes:

# 1. Clave: es un identificador único.
# 2. Valor: es el dato que se almacena.

# Ejemplo de diccionario:
# Para caracterizar un país:


pais = {
    "nombre": "Colombia",
    "capital": "Bogotá",
    "idioma": "Español",
    "continente": "América",
    "población": 50000000,
    "superficie": 1141748,
    "PIB per cápita": 21437,
    "moneda": "Peso colombiano",
    "ciudades": [
        "Bogotá",
        "Medellín",
        "Cali",
        "Barranquilla",
        "Cartagena",
        "Bucaramanga",
        "Pereira"
    ]
}

print(pais["nombre"])
print("es un país de ", pais["continente"])
print("el cual habla ", pais["idioma"], ".")
print("Su capital es: ", pais["capital"], ",")
print("su población es: ", pais["población"])   
print("su superficie es: ", pais["superficie"], "km².")
print("Su PIB per cápita es: ", pais["PIB per cápita"], "USD.")
print("Su moneda es: ", pais["moneda"])

print("Y sus ciudades principales son: ")


for ciudad in pais["ciudades"]:
    print(ciudad, end=", ")
