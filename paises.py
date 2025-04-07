# Colección de países:

paises = [
    {
        "nombre": "Colombia",
        "capital": "Bogotá",
        "idioma": "Español, Lenguas indígenas",
        "moneda": "Peso Congolombiano",
        "continente": "América del Sur",
        "población": "50 millones",
        "superficie": "1.142 millones km²",
        "PIB per cápita": "4.200 USD",
        "ciudades": [
            {
                "nombre": "Bogotá",
                "poblacion": "7.7 millones",
                "fundación": 1538
            },
            {
                "nombre": "Medellín",
                "poblacion": "2.5 millones",
                "fundación": 1616
            },
            {
                "nombre": "Cali",
                "poblacion": "2.2 millones",
                "fundación": 1536
            },
            {
                "nombre": "Barranquilla",
                "poblacion": "1.2 millones",
                "fundación": 1813
            },
        ]
    },

    {
        "nombre": "Ecuador",
        "capital": "Quito",
        "idioma": "Español, Quichua",
        "moneda": "Dólar estadounidense",
        "continente": "América del Sur",
        "población": "17 millones",
        "superficie": "283.561 km²",
        "PIB per cápita": "6.500 USD",
        "ciudades": [
            "Quito",
            "Guayaquil",
            "Esmeraldas",
            "Cuenca",
            "Pasto"
        ]
    },

    {
        "nombre": "Venezuela",
        "capital": "Caracas",
        "idioma": "Español",
        "moneda": "Bolívar",
        "continente": "América del Sur",
        "población": "30 millones",
        "superficie": "916.445 km²",
        "PIB per cápita": "4.500 USD",
        "ciudades": [
            "Caracas",
            "Maracaibo",
            "Barquisimeto",
            "Cúcuta",
            "San Cristóbal"
        ]
    },

    {
        "nombre": "Perú",
        "capital": "Lima",
        "idioma": "Español, Quechua",
        "moneda": "Nuevo Sol",
        "continente": "América del Sur",
        "población": "32 millones",
        "superficie": "1.285.216 km²",
        "PIB per cápita": "6.800 USD",
        "ciudades": [
            "Lima",
            "Arequipa",
            "Cusco",
            "Piura",
            "Trujillo"
        ]
    }
]


# Iterar cada país

for pais in paises:
    print("Nombre del país:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Idioma:", pais["idioma"])
    print("Moneda:", pais["moneda"])
    print("Continente:", pais["continente"])
    print("Población:", pais["población"])
    print("Superficie:", pais["superficie"], "km²")

    print("Ciudades principales de", pais["nombre"], ":")
    
    # Iterar sobre las ciudades
    for ciudad in pais["ciudades"]:
        print("-", ciudad)
    print()  
    
    if pais["nombre"] == "Colombia":
        for ciudad in pais["ciudades"]:
            print("Nombre de la ciudad:", ciudad["nombre"])
            print("Población:", ciudad["poblacion"])
            print("Año de fundación:", ciudad["fundación"])
            print()  # Línea en blanco entre ciudades
