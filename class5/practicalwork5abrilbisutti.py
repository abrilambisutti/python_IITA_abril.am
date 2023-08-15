
#Trabajo Practico
"""Ejercicio 1: Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3)."""

# def redondear(numero):
#     if numero > 3.50:
#         return int(numero) + 1
#     else:
#         return int(numero)

"""Ejercicio 2: Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado"""

# # Módulo redondeo
# class Redondeo:
#     @staticmethod
#     def redondear(numero):
#         if numero > 3.50:
#             return int(numero) + 1
#         else:
#             return int(numero)

# # Creación del módulo principal
# class SumaRedondeada:
#     @staticmethod         # decorador en Python que se utiliza para definir un método estático en una clase. Un método estático es un método que pertenece a la clase en lugar de una instancia de la clase. Esto significa que puedes llamar a un método estático sin tener que crear una instancia de la clase.
#     def suma_redondeada(a, b):
#         suma = a + b
#         return Redondeo.redondear(suma)

"""Ejercicio 3: Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema."""

# import datetime

# fecha_hora_actual = datetime.datetime.now()

# formato = "%Y-%m-%d %H:%M:%S"  # Formato: Año-Mes-Día Hora:Minutos:Segundos
# fecha_hora_formateada = fecha_hora_actual.strftime(formato)

# print("Fecha y Hora Actuales:", fecha_hora_formateada)


""" Ejercicio 4: 
Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""
# import random

# while True:
#     numero_par = random.randint(2, 10)  # Genera un número al azar entre 2 y 10
    
#     if numero_par % 2 == 0:
#         print("Número par generado:", numero_par)
#         break  # Salir del ciclo si se genera un número par

"""Ejercicio 5: Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica."""

# import random

# def bola_magica():
#     respuestas = [
#         "Es seguro que sí",
#         "Las chances son buenas",
#         "Puedes contar con ello",
#         "Pregúntame de nuevo más tarde",
#         "Concéntrate y pregunta de nuevo",
#         "No veo con claridad, intenta de nuevo",
#         "Mi respuesta es no",
#         "Mis fuentes me dicen que no"
#     ]
    
#     respuesta_elegida = random.choice(respuestas)
#     return respuesta_elegida

# #Usar
# pregunta = input("Hazme una pregunta: ")
# respuesta = bola_magica()
# print("Bola Mágica dice:", respuesta)


"""Ejercicio 6: Encuentre el tiempo de ejecución de los ejercicios anteriores."""

# import time
# import random
# import datetime

# # Ejercicio 1
# def ejercicio1(numero):
#     if numero > 3.50:
#         return int(numero) + 1
#     else:
#         return int(numero)

# numero_ejercicio1 = 3.7
# start_time = time.time()
# resultado_ejercicio1 = ejercicio1(numero_ejercicio1)
# end_time = time.time()
# print("Ejercicio 1 - Resultado:", resultado_ejercicio1)
# print("Tiempo de ejecución para el Ejercicio 1:", end_time - start_time, "segundos")
# print()

# # Ejercicio 2
# from paquete_redondeo.redondeo import redondear

# def ejercicio2(a, b):
#     suma = a + b
#     return redondear(suma)

# a_ejercicio2 = 3.2
# b_ejercicio2 = 4.8
# start_time = time.time()
# resultado_ejercicio2 = ejercicio2(a_ejercicio2, b_ejercicio2)
# end_time = time.time()
# print("Ejercicio 2 - Resultado:", resultado_ejercicio2)
# print("Tiempo de ejecución para el Ejercicio 2:", end_time - start_time, "segundos")
# print()

# # Ejercicio 3
# def ejercicio3():
#     fecha_hora_actual = datetime.datetime.now()
#     formato = "%Y-%m-%d %H:%M:%S"
#     fecha_hora_formateada = fecha_hora_actual.strftime(formato)
#     print("Ejercicio 3 - Fecha y Hora Actuales:", fecha_hora_formateada)

# start_time = time.time()
# ejercicio3()
# end_time = time.time()
# print("Tiempo de ejecución para el Ejercicio 3:", end_time - start_time, "segundos")
# print()

# # Ejercicio 4
# def ejercicio4():
#     while True:
#         numero_par = random.randint(2, 10)
#         if numero_par % 2 == 0:
#             print("Ejercicio 4 - Número par generado:", numero_par)
#             break

# start_time = time.time()
# ejercicio4()
# end_time = time.time()
# print("Tiempo de ejecución para el Ejercicio 4:", end_time - start_time, "segundos")
# print()

# # Ejercicio 5
# def ejercicio5():
#     def bola_magica():
#         respuestas = [
#             "Es seguro que sí",
#             "Las chances son buenas",
#             "Puedes contar con ello",
#             "Pregúntame de nuevo más tarde",
#             "Concéntrate y pregunta de nuevo",
#             "No veo con claridad, intenta de nuevo",
#             "Mi respuesta es no",
#             "Mis fuentes me dicen que no"
#         ]
        
#         respuesta_elegida = random.choice(respuestas)
#         return respuesta_elegida
    
#     pregunta = input("Hazme una pregunta: ")
#     respuesta = bola_magica()
#     print("Ejercicio 5 - Bola Mágica dice:", respuesta)

# start_time = time.time()
# ejercicio5()
# end_time = time.time()
# print("Tiempo de ejecución para el Ejercicio 5:", end_time - start_time, "segundos")
# print()






























