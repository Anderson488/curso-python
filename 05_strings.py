#anio_nacimiento = input("¿cual es tu anio de nacimiento?")

#print (f"tienes {2026 - int(anio_nacimiento)}") 
#ValueError: invalid literal for int() with base 10: 'dos mil tres'
#El error se produce por que no es un entero lo que se la da de input si no un str


# Ejercio 1.

radicado = "CO-VUP-2026-00873"

print (f"pais {radicado [0:2]}, la ciudad {radicado[3:6]}, el anio {radicado[7:11]}, y consecutivo {radicado[12:17]}")
print(len(radicado), int(radicado[7:11]) + 1)

# Ejercicio 3.

cedula = "1065432198"
telefono = "315-222-8322"
correo = "ANGEL.DATOS@CORREO.COM"

print(cedula.isnumeric())
print(telefono.startswith("3"))
print(telefono[0:1])

print(correo.lower())

correo_limpio = "ANGEL.DATOS@CORREO.COM"
print(correo_limpio.capitalize())
print(correo)
print(telefono.count("-"))

# Ejercicio 3.

municipio = "valledupar"

print(municipio.upper())
print(municipio.upper[0:3]) 

print()



