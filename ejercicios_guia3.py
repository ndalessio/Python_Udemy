#Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.

# def min_seg(horas):
#     minutos = horas * 60
#     seg = horas * 3600
#     print(f"{horas} horas son {minutos} minutos y {seg} segundos.")

# min_seg(10)
# min_seg(24)

#Ejercicio 2: Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.

# def pares():
#     pares = []
#     for i in range(101):
#         if i % 2 == 0:
#             pares.append(i)
#     return pares

# print(pares())

#Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.

# def numbers_in(message):
#     numbers = []
#     for caracter in message:
#         if caracter.isdigit():
#             numbers.append(caracter)

#     print(numbers)

# numbers_in("Holas5sasjdj8")


#Ejercicio 4: Crear una función que, a partir de 4 números, devuelva el mayor producto de dos de ellos. Imprimir resultado por pantalla.

# def biggest_product(number1, number2, number3, number4):
#     list = [number1, number2, number3, number4]
#     list.sort()
#     for number in list:
#         if number == 0:
#             list.pop(number)
#             biggest_prod = list[-2] * list[-1]
#         else:
#             biggest_prod = list[-2] * list[-1]
#     print(biggest_prod)

# biggest_product(1, 2, 3, 4)

#Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números, False si hay al menos uno de los parámetros ingresados que no es un número, y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.



#Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números, False si hay al menos uno de los parámetros ingresados que no es un número, y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.

#Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title. Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"

#Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no. En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", en caso contrario, devolver "La palabra no es un palíndromo".

#Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si la distancia es de 400km. Luego crear una función que, a partir de esos datos, devuelva cuánto significa eso en pesos si el litro de nafta está 60$.

#Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas. Luego crear una función que nos informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).

#Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.