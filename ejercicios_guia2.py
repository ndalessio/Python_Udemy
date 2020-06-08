# Ejercicio 1: Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés, si no se cumple ninguna de las opciones anteriores, por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".

# message = str(input("Ingrese un mensaje: "))

# if len(message) > 10:
#     print(message)
# elif len(message) >= 5 and len(message) < 10:
#     print(message[::-1])
# else:
#     print('Su mensaje es demasiado corto')

# Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor. Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista.

# lista_numeros = [1 , 20, 50, 102, 45, 400, 21, 7, 3, 14]

# lista_numeros.sort()

# numero_mayor = lista_numeros[-1]
# numero_menor = lista_numeros[0]

# print(f"El numero mayor es {numero_mayor} y el numero menor es {numero_menor}")

# numeros_mayores_100 = []

# for i in lista_numeros:
#     if i > 100:
#         numeros_mayores_100.append(i)
# if len(numeros_mayores_100) >= 3:
#     for i in numeros_mayores_100:
#         print(numero)
# else:
#     for i in lista_numeros > 50:
#         print(i)

# Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir la resta entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto.

# numero1 = int(input("Ingrese numero 1: "))
# numero2 = int(input("Ingrese numero 2: "))

# if numero1 < numero2:
#     print(numero2 - numero1)
# elif numero1 > numero2:
#     print(numero1 + numero2)
# elif numero1 == numero2:
#     print(numero1 * numero2)


# Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.

# lista_numeros = []

# for i in range(6):
#     numero = int(input("Ingrese un numero: "))
#     lista_numeros.append(i)
# lista_numeros.sort()

# print(lista_numeros)

# Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}. Desafío: lograr cambiar las claves. Pista: si imprimen ítems del diccionario les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.

# meses = {1: "enero",
#          2: "febrero",
#          3: "marzo",
#          4: "abril",
#          5: "mayo",
#          6: "junio",
#          7: "julio",
#          8: "agosto",
#          9: "septiembre",
#          10: "octubre",
#          11: "noviembre",
#          12: "diciembre"}

# meses_numero = list(meses.values())
# meses_palabras = list(meses.keys())
# meses.clear()

# meses = dict(zip(meses_numero, meses_palabras))
# print(meses)

# Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles, una vez seleccionada la operación, introducir dos números y ejecutar la operación.

# opcion = input("Ingrese una de las siguientes opciones: suma, resta, multiplcacion, division:  ")
# numero1 = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese un numero: "))

# if opcion == "suma":
#     print(numero1 + numero2)
# elif opcion == "resta":
#     print(numero1 - numero2)
# elif opcion == "multiplicacion":
#     print(numero1 * numero2)
# elif opcion == "division":
#     print(numero1 / numero2)

# Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario, si no con nombre : nota). Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.

# notas = {"alumno1" : 7, "alumno2" : 8, "alumno3" : 4, "alumno4" : 5, "alumno5" : 9}

# for nombre, nota in notas.items():
#     if nota >= 7:
#         print(f"{nombre} : {nota} - Aprobado")

# Ejercicio 8: Pedirle al usuario que ingrese por teclado 3 números binarios de 8 bits, para cada uno imprimir su siguiente (número + 1) pero en sistema decimal. Recuerden que los números binarios están compuestos por 1 y 0.

# decimal = 0
# for i in range(3):
#     binario = input("Ingrese un número binario: ")
#     for bit in binario:
#         decimal += decimal + int(bit)
#     print(decimal + 1)
#     decimal = 0

# Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. Evaluar si puede realizar una compra de $2500, si puede indicar cuánto saldo le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para poder realizarla.

# monto = int(input("Ingrese el monto disponible en su tarjeta de credito: "))

# if monto >= 2500:
#     print(f"Puede realizar una compra por ${monto}. Luego de realizar la compra de $2500 le quedará ${monto - 2500}")

# if monto < 2500:
#     print(f"Su saldo es de ${monto}. Para realizar la compra requiere ${2500 - monto} más")

# Ejercicio 10: Utilizar el método range() para recorrer el iterable e imprimir solo los números impartes entre 1 y 40 inclusive.

# for i in range(1,40):
#     if i % 2 != 0:
#         print(i)