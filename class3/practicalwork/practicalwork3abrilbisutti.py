#Trabajo Practico 3
"""Ejercicio 1
Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para 
un rango de números indicado por un usuario."""
# lista = list(range(1, 21))
# print (F"La lista es {lista}")

# primernumero=int(input("Ingrese su primer numero: "))
# ultimonumero= int(input("Ingrese su ultimo numero: "))
# lista_del_usuario=list(range(primernumero, ultimonumero+1))   #si o si tengo que crear range y hacerlo lista para que se guarden todos los datos
# print(lista_del_usuario)


"""Ejercicio 2
Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50"""
# numerosolicitado=int(input("Ingrese numero para multiplicarlo: "))
# lista= list(numerosolicitado * x for x in range(1,11))
# print (f"Los resultados son: {lista}")                       


"""Ejercicio 3
Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
caracteres."""
# cadena = input("Ingrese su frase o palabra: ")
# caracteres = []
# for caracter in cadena:
#     if caracter not in caracteres:
#         caracteres.append(caracter)
# print(caracteres)


"""Ejercicio 4
Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios. """

# frase = input("Ingrese su frase: ")
# lista_caracteres = []

# for letra in frase:
#     if letra != " ":
#         if letra not in lista_caracteres:
#             lista_caracteres.append(letra)

# print(lista_caracteres)






"""Ejercicio 5
Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
repite."""
# tupla=(1,2,3,4,5,6,7,3784798,35,7,43,2,76,4,8)
# numeros=int(input("Ingrese numero ; "))
# repeticiones=0
# for numero in tupla:
#     if numero==numeros:
#         repeticiones+=1
#         print(f"El numero {numeros} se repite {repeticiones} veces")

"""Ejercicio 6
Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero """
# tupla_meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
# while True:
#     numero_usuario=int(input("Ingrese numero del 1 al 12 para mostrar mes (0 para salir): "))
#     if numero_usuario==0:
#         print("Bye")
#         break
#     elif numero_usuario in range(1, len(tupla_meses)+1):
#         mes=tupla_meses[numero_usuario - 1]
#         print(f"El numero {numero_usuario} corresponde al mes {mes}")
#     else:
#         print("ERROR, numero no corresponde")

"""Ejercicio 7
Crea una tupla con números e indica el número con mayor valor y el que menor
tenga."""
# tupla=(5234,892178,36821,73681,7238,18823)
# numero_inicial=tupla[0]
# for numero in tupla:
#     if numero>numero_inicial:
#         numero_inicial=numero
#     else:
#         continue
# print(f"El numero mayor de esta tupla es: {numero_inicial}")










