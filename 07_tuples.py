# tuples ##

# Ejercicio 1 #

coordenadas = (10.4631, -73.2532)
print(f"Las coordenadas de la ciudad son latitud {coordenadas[0]}")
print(f"Las coordenadas de la ciudad son longitud {coordenadas[1]}")

print(len(coordenadas))
print(type(coordenadas))

#coordenadas[0] = 10.5 #TypeError: 'tuple' object does not support item assignment

#Ejercicio 2 #

dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
laborales = dias[0:5]
print(laborales) # devuelve una tupla

fin_de_semana = dias[-2:]
print(fin_de_semana)

print(dias.index("viernes"))

print(type(laborales))

# Ejercicio 3 #

departamentos = ("Cesar", "Magdalena", "La Guajira")
print(type(departamentos))
lista_departamentos = list(departamentos)
print(type(lista_departamentos))
lista_departamentos.append("Bolivar")
departamentos = tuple(lista_departamentos)
print(type(departamentos))
print(departamentos)

print(f"hay {len(departamentos)} departamentos y el ultimo es {departamentos[-1]}")
