# variables

my_string_variables = "My String variable"
print(my_string_variables)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variables, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variables))


# Ejercicio 1.

nombre = "Anderson"
print(nombre)
print(type(nombre))

edad = 23
print(edad)
print(type(edad))

estatura = 1.75
print(estatura)
print(type(estatura))

sabe_programar = False
print(sabe_programar)
print(type(sabe_programar))

anio_nacimiento = "2003"
print(anio_nacimiento)
print(type(anio_nacimiento))

frase = 'Mi profesor dijo: "Python es facil"'
print(frase)


# Ejercicio 2. A

#2nombre, nombre completo, nombreCompleto, nombre_completo, class, _total.
# los nombre validos en python es nombre_completo y es el mas recomendado, los demas son invalidos porque llevan un numero adelante, tiene espacios, tienen una letra mayuscula o _adelante.

# Ejercicio 2. B

ciudad = "Valledupar"
ciudad = "Bogotá"
print(ciudad)

dato = 100
print(type(dato))
dato = "cien"
print(type(dato))

# Este codigo imprime primero la ciudad en este caso Bogota, y cien en str

# Ejercicio 3.

nombre, edad, estatura = "Anderson", 23, 1.75
print("me llamo:",nombre, "tengo",edad,"años","y mido",estatura,"metros")

print("me llamo: "+ nombre + " tengo " + str(edad) + " años " + " y mido " + str(1.75) + " metros")

# El error es TypeError: can only concatenate str (not "int") to str, la solucione fue cambiarlos a tipo str

# Ejercicio 4.

anio_actual = 2026
anio_nacimiento = 2003
print(anio_actual - anio_nacimiento)

# Ejercicio 5.

nombre = input("¿cual es tu nombre?")
anio_nacimiento = input("¿cual es tu año de nacimiento?")

print(nombre)
print(anio_nacimiento)

print("Hola:",nombre,"tienes",edad,"años","y tu nombre tiene:",len(nombre),"letras.")


