
# Ejercicio 1: Crear un programa que devuelva por pantalla el string "Hola Mundo!"

#print("Hola Mundo!")

# Ejercicio 2: Crear un programa en el cual se almacene en una variable el string "Hola Mundo!" y luego se imprima por pantalla dicha variable.

#saludo = "Hola Mundo!"
# print(saludo)

# Ejercicio 3: Crear un programa que pregunte al usuario su nombre y edad y luego imprima esos datos en renglones distintos.

#nombre = input("¿Cuál es tu nombre?")
#edad = input("¿Cuántos años tenés?")
# print(nombre)
# print(edad)

# Ejercicio 4: Crear un programa que pregunte al usuario su nombre y devuelva "¡Hola {nombre}!"

# nombre = input("Cuál es tu nombre?")
# #print("Hola" + nombre + "!")
# print(f"Hola {nombre}!")

# Ejercicio 5: Crear un programa que pida al usuario ingresar 2 números por teclado y devuelva por pantalla la suma de ellos en un renglón, la resta en otro, el producto en otros y la división en otro.

# numero1 = int(input("ingrese un número"))
# numero2 = int(input("ingrese otro número"))

# suma = (numero1 + numero2)
# resta = (numero1 - numero2)
# producto = numero1 * numero2
# division = numero1 / numero2

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Producto: {producto}")
# print(f"División: {division}")

# Ejercicio 6: Crear un programa que calcule cuánto dinero tendré al cabo de un mes si deposito hoy 2000 en el banco y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.

# deposito = 2000
# interes = deposito * 5 / 100
# saldo = deposito + interes
# print(saldo)

# Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla.

# sueldo_hora = 400
# horas_por_dia = 8
# dias_por_semana = 5
# semanas_por_mes = 4

# print(sueldo_hora * horas_por_dia * dias_por_semana * semanas_por_mes)

# Ejercicio 8: Crear un programa que almacene en una lista las siguientes materias: Historia, Matemática, Lengua y Geografía. Luego devolver por pantalla la última materia almacenada.

# materias = ["Historia", "Matematica", "Lengua", "Geografia"]
# print(materias[-1])

# Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros y devuelva una lista con ellos.

# numero1 = input("Ingrese un numero: ")
# numero2 = input("Ingrese un numero: ")
# numero3 = input("Ingrese un numero: ")
# numero4 = input("Ingrese un numero: ")
# numero5 = input("Ingrese un numero: ")

# lista_numeros = [numero1, numero2, numero3, numero4, numero5]
# print(lista_numeros)

# Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y nos devuelva una lista sin las vocales, sin modificar la original.

# abecedario = "abcdefghi"
# vocales = ["a", "e", "i", "o", "u"]

# abecedario_sin_vocales = ''

# for letra in abecedario:

#     if letra not in vocales:
#         abcedario_sin_vocales = abecedario_sin_vocales + letra
#         print(abcedario_sin_vocales, end=' ')

# Ejercicio 11: Crear una lista con varios números, luego ordenarlos de manera creciente y devolver por pantalla la lista ordenada y cuál es el menor y cuál el mayor.

#lista_numeros = [55, 20, 14, 1, 9, 0]
# Solucion 1
# lista_numeros.sort()
# print(lista_numeros)

# Solucion 2
# numeros = [3, 20, 14, 1, 9, 0]
# print(numeros)
# ordenado = False

# while ordenado == False:
#     for i in range(len(numeros)-1):
#         ordenado = True
#         if numeros[i] > numeros[i + 1]:
#             aux = numeros[i]
#             numeros[i] = numeros[i + 1]
#             numeros[i + 1] = aux
#             ordenado = False

# print(numeros)

# Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

# Ejercicio 13: Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

# monedas = {'Euro':'€',
#             'Dollar':'$',
#             'Yen':'¥'}

# moneda = input("Introduzca una divisa: ")
# print(monedas.get(moneda.title(), "La divisa no está."))

# Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.

# nombre = input("¿Cuál es su nombre?: ")
# edad = input("¿Cuál es su edad?: ")
# direccion = input("¿Direccion?: ")
# telefono = input("¿Telefono? :")

# datos_personales = {'nombre' : '',
#                     'edad' : '',
#                     'direccion' : '',
#                     'telefono' : ''}

# datos_personales['nombre'] = nombre
# datos_personales['edad'] = edad
# datos_personales['direccion'] = direccion
# datos_personales['telefono'] = telefono

# print(datos_personales)

# Ejercicio 15: Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# Solucion 1

# creditos_asignaturas = {
#     'Matematica': 6,
#     'Fisica': 4,
#     'Quimica': 5
# }

# print(f"Matematica tiene {creditos_asignaturas['Matematica']} creditos")
# print(f"Fisica tiene {creditos_asignaturas['Fisica']} creditos")
# print(f"Quimica tiene {creditos_asignaturas['Quimica']} creditos")

# total_creditos = creditos_asignaturas['Matematica'] + creditos_asignaturas['Fisica'] + creditos_asignaturas['Quimica']

# print(f"El total de creditos es: {total_creditos}")

# Solucion 2

# for key, value in creditos_asignaturas.items():
#     print(
#         f"La materia {key} tiene {value} creditos")


# Ejercicio 16: Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# datos = {
#         'nombre': '',
#         'edad': '',
#         'telefono': '',
#         'mail': ''
#         }

# datos['nombre'] = input("¿Nombre? ")
# print(datos)
# datos['edad'] = input("¿Edad? ")
# print(datos)
# datos['telefono'] = input("¿Telefono? ")
# print(datos)
# datos['mail'] = input("¿Mail? ")
# print(datos)
