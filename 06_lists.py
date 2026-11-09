### Lists ###

my_list = list()
my_other_list = [35, 1.77, "Andy", "Python"]    

print(my_other_list + my_list)

my_list= "Hola Python"
print(my_list[4])

del my_other_list[2]
print(my_other_list)

print(my_list)

# Ejercicio 1 #

municipio = ["valledupar", "aguachica", "codazzi", "bosconia", "curumani", "chimichagua"]
print(f"El municipio de {municipio[0]} y {municipio[-1]} son los más importantes del departamento del Cesar")

print(f"{municipio[2:5]}")

print(len(municipio))

print(municipio.index("bosconia"))


# Ejercicio 2 #

ventas = [125000, 98000, 143000, 87000, 156000]
ventas.append(172000)
print(ventas)


ventas_miercoles = 139000
ventas[2] = ventas_miercoles
print(ventas)

ventas_ordenadas = ventas.copy()
ventas_ordenadas.sort(reverse=True)
print(ventas_ordenadas)   
print(ventas) 

print(f"venta mas alta es {ventas_ordenadas[0]} y {ventas_ordenadas[-1]} es la mas baja")


#Ejercicio 3 #

registro = "Valledupar;2026;532956;Cesar"
datos = registro.split(";")
print(datos)

municipio, anio, poblacion, departamento = datos

print(f"La ciudad de {municipio} tiene {poblacion} habitantes en el departamento del {departamento}")

anio = (int(anio))
print(type(anio))
poblacion = (int(poblacion))
print(type(poblacion))


print(f"La ciudad de {municipio} tiene {poblacion} habitantes en el departamento del {departamento}")