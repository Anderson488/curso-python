# operadores aritmeticos

print( 3+4 )
print( 3/4 )
print( 10 % 4 )

print( 10 / 6 )
print( 10 // 6 )

print("Hola " + "Ander")
print("Hola Cr" + "7")

print("Hola " * 2)

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores comparativos

print(3 < 4)
print(3 == 4)

print(5 != 3, 5 >= 3 )

# Ejercicio 1.

anio_nacimiento = "2003"
anio_actual = 2026


#print (anio_nacimiento - anio_actual) # TypeError: unsupported operand type(s) for -: 'str' and 'int'
print (anio_actual - int(anio_nacimiento)) 

"""
El numero guardado como texto no sirve
por que no se puede calcular un int con
un str sin antes convertir el str
se resolvio haciendo la conversion a entero
"""

# Ejercicio 2.

print(17 / 5) #3.4 ✔
print(17 // 5) #3 ✔
print(17 % 5)#2 ✔
print(10 / 2)#5 ✘ la division da un float, aunque el resultado sea un entero al ser un float va con decimal
print(2 ** 10)#20 ✘
print(10 - 2 * 3)#24 ✘
print((10 - 2) * 3)#24 ✔

# Ejercicio 3.

huevos = 1250
cubeta = 30
valor_cubeta = 18500

print (1250 // 30) # se llenan 41 cubetas completas
print (1250 % 30) # Sueltos quedan 20 huevos
print (41 * 18500) #ingreso total 758500
print (1250 % 41) # true

# Ejercicio 4.

edad = 18
tiene_documento = True
tiene_autorizacion = False

puede_inscribirse = (edad)