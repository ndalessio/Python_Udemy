"""
Ejercicio 3: Crear una función que, a partir de un mensaje,
nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.
"""

def mensaje(msj):
    lista_numeros = []
    for caracter in msj:
        if caracter.isdigit():
            lista_numeros.append(caracter)

    print(lista_numeros)

mensaje("Tengo 28 años, en agosto cumplo 29.")


