#TRABAJO PRACTICO 4
"""Ejercicio 1: """
# def es_primo(numero):
#     if numero <= 1:
#         return False
#     if numero <= 3:
#         return True
#     if numero % 2 == 0 or numero % 3 == 0:
#         return False
#     i = 5
#     while i * i <= numero:
#         if numero % i == 0 or numero % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def mostrar_primos_hasta_n(n):
#     print("Números primos entre 1 y", n, ":")
#     for num in range(2, n + 1):
#         if es_primo(num):
#             print(num)

# n = int(input("Ingrese un número: "))
# mostrar_primos_hasta_n(n)


"""Ejercicio 2: """
"""CICLO WHILE"""
# def hacer_sandwich():
#     condimentos = []
#     condimento = input("Ingrese un condimento para el sándwich (o 'salir' para detener): ")

#     while condimento.lower() != 'salir':
#         condimentos.append(condimento)
#         print(f"Se agregó {condimento} al sándwich.")
#         condimento = input("Ingrese otro condimento (o 'salir' para detener): ")

#     print("¡Su sándwich está listo con los siguientes condimentos:")
#     for c in condimentos:
#         print(c)

# hacer_sandwich()

"""TEST CONDICIONAL DENTRO DEL CICLO"""
# def hacer_sandwich():
#     condimentos = []

#     while True:
#         condimento = input("Ingrese un condimento para el sándwich (o 'salir' para detener): ")
        
#         if condimento.lower() == 'salir':
#             break
        
#         condimentos.append(condimento)
#         print(f"Se agregó {condimento} al sándwich.")

#     print("¡Su sándwich está listo con los siguientes condimentos:")
#     for c in condimentos:
#         print(c)

# hacer_sandwich()

"""Ejercicio 3: """

# def hacer_remera(tamaño, mensaje):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'.")

# # Punto A
# print("Punto A:")
# hacer_remera('M', 'Hola Mundo')  
# hacer_remera(mensaje='Python es genial', tamaño='S')  

# # Punto B
# def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'.")

# print("\nPunto B:")
# hacer_remera()  
# hacer_remera('XL', '¡Programar es divertido!')  

"""Ejercicio 4: """

# def fibonacci(n):
#     fib_series = [0, 1] 

#     while len(fib_series) < n:
#         next_number = fib_series[-1] + fib_series[-2] 
#         fib_series.append(next_number) 
#     return fib_series

# n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea generar: "))
# fibonacci_series = fibonacci(n)
# print(f"Los primeros {n} números de la serie de Fibonacci son:")
# print(fibonacci_series)






