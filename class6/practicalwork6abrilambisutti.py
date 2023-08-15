#Trabajo Practico

"""Ejercicio 1: escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo."""

# class Rectángulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def calcular_area(self):
#         return self.base * self.altura


"""Ejercicio 2: Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

# class Mate:
#     def __init__(self, n):
#         self.cantidad_cebadas_restantes = 0
#         self.estado = "vacío"
#         self.n = n
    
#     def cebar(self):
#         if self.estado == "lleno":
#             raise Exception("¡Cuidado! ¡Te quemaste!")
        
#         if self.cantidad_cebadas_restantes < self.n:
#             self.estado = "lleno"
#             self.cantidad_cebadas_restantes += 1
#         else:
#             print("Advertencia: el mate está lavado.")
    
#     def beber(self):
#         if self.estado == "vacío":
#             raise Exception("¡El mate está vacío!")
        
#         self.estado = "vacío"
#         self.cantidad_cebadas_restantes -= 1
#         if self.cantidad_cebadas_restantes == 0:
#             print("Advertencia: el mate está lavado.")
    
"""Ejercicio 3: Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho"""
# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self, corcho=None):
#         self.corcho = corcho

# class Sacacorchos:
#     def __init__(self):
#         self.corcho_extraido = None
    
#     def destapar(self, botella):
#         if botella.corcho is None:
#             raise Exception("La botella ya está destapada.")
#         if self.corcho_extraido is not None:
#             raise Exception("El sacacorchos ya contiene un corcho.")
        
#         self.corcho_extraido = botella.corcho
#         botella.corcho = None
    
#     def limpiar(self):
#         if self.corcho_extraido is None:
#             raise Exception("No hay un corcho en el sacacorchos para limpiar.")
        
#         self.corcho_extraido = None

"""Ejercicio 4: Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método."""

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
    
#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")
    
#     def abrir_restaurante(self):
#         print(f"¡El restaurante {self.restaurante_nombre} está ahora abierto!")

# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores
    
#     def mostrar_sabores(self):
#         print("Sabores disponibles:")
#         for sabor in self.sabores:
#             print("- " + sabor)

"""Ejercicio 5: Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada
"""
# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
    
#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             raise Exception("El personaje está derrotado.")
    
#     def mover(self, direccion, distancia):
#         if direccion == "izquierda":
#             self.posicion -= distancia * self.velocidad
#         elif direccion == "derecha":
#             self.posicion += distancia * self.velocidad

# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque
    
#     def atacar(self, personaje_objetivo):
#         personaje_objetivo.recibir_ataque(self.ataque)

# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha
    
#     def cosechar(self):
#         return self.cosecha


"""Ejercicio 6: Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

# class Usuario:
#     def __init__(self, nombre, apellido, edad, ciudad, ocupacion):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.ocupacion = ocupacion
    
#     def describir_usuario(self):
#         print(f"Información de {self.nombre} {self.apellido}:")
#         print(f"Edad: {self.edad}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"Ocupación: {self.ocupacion}")
    
#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} ¡Bienvenido/a de nuevo!")


# usuario1 = Usuario("Juan", "Pérez", 30, "SALTA A", "Ingeniero")
# usuario2 = Usuario("María", "Gómez", 25, "BUENOS AIRES B", "Estudiante")
# usuario3 = Usuario("Luis", "Rodríguez", 40, "CORRIENTES C", "Médico")


# usuario1.describir_usuario()
# usuario1.saludar_usuario()
# print()

# usuario2.describir_usuario()
# usuario2.saludar_usuario()
# print()

# usuario3.describir_usuario()
# usuario3.saludar_usuario()


"""Ejercicio 7: Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, ciudad, ocupacion, privilegios):
#         super().__init__(nombre, apellido, edad, ciudad, ocupacion)
#         self.privilegios = privilegios
    
#     def mostrar_privilegios(self):
#         print(f"Privilegios de {self.nombre} {self.apellido}:")
#         for privilegio in self.privilegios:
#             print("- " + privilegio)


# admin1 = Admin("Laura", "Martínez", 35, "TUCUMAN", "Administradora", ["puede postear en el foro", "puede borrar un post", "puede banear usuario"])

# admin1.mostrar_privilegios()


"""Ejercicio 8: Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios."""


# class Privilegios:
#     def __init__(self, privilegios):
#         self.privilegios = privilegios
    
#     def mostrar_privilegios(self):
#         print("Privilegios:")
#         for privilegio in self.privilegios:
#             print("- " + privilegio)

# class Usuario:
#     def __init__(self, nombre, apellido, edad, ciudad, ocupacion):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.ocupacion = ocupacion
    
#     def describir_usuario(self):
#         print(f"Información de {self.nombre} {self.apellido}:")
#         print(f"Edad: {self.edad}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"Ocupación: {self.ocupacion}")
    
#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} ¡Bienvenido/a de nuevo!")

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, ciudad, ocupacion, privilegios):
#         super().__init__(nombre, apellido, edad, ciudad, ocupacion)
#         self.privilegios = Privilegios(privilegios)

# privilegios_admin = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
# admin1 = Admin("Laura", "Martínez", 35, "NEUQUEN", "Administradora", privilegios_admin)

# admin1.privilegios.mostrar_privilegios()


"""Ejercicio 9: Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó."""

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
    
#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")
    
#     def abrir_restaurante(self):
#         print(f"¡El restaurante {self.restaurante_nombre} está ahora abierto!")

# IMPORTAR CLASE RESPTAURANTE:

# main.py

"""from restaurante import Restaurante"""

# Crear una instancia de la clase Restaurante
"""mi_restaurante = Restaurante("La Delicia", "Comida Italiana")"""

# Llamar a un método de la instancia
"""mi_restaurante.describir_restaurante()"""
