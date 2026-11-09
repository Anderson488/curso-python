# Conditionals##

my_condition = True

if my_condition:
    print("The condition is True")



    my_condition = 5 * 1

    if my_condition == 10:
        print("Se ejecuta la condicion del segundo if")
              
    if my_condition > 10:
        print("Es mayor que 10")
    else:
     print("Es menor o igual a 10")

    print("La ejecuión continúa")


total_compra = 185000
es_cliente_frecuente = True
ciudad = "Valledupar"

# if / else: dos caminos
if total_compra >= 150000:
    print("Envío gratis")          # indentado: pertenece al if
else:
    print("Envío con costo")       # indentado: pertenece al else
print("Fin de la revisión de envío")   # sin indentar: se ejecuta siempre

if total_compra >= 500000:
    descuento = 0.15
elif total_compra >= 150000:
    descuento = 0.10               # 185000 cae aquí
elif total_compra >= 50000:
    descuento = 0.05
else:
    descuento = 0
print(f"Descuento aplicado: {descuento}")


## Ejercicio 1 ##

nota = 2.0
if nota >= 4.6:
    print("Superior")
elif nota >= 4.0:
    print("Alto")
elif nota >= 3.0:
    print("Basico")  
else:
    print("Bajo")   

    # El orden importa ya que dependiendo de eso da un valor u otro, por ejemplo si la nota es 4.0, se ejecuta el if de alto y el de bajo, pero no el de basico ya que no cumple la condicion.   

# Ejercicio 2 ##

cedula = "1065432198"

if not cedula:
    print("Falta cedula")

elif not cedula.isdigit():
    print("Cedula invalida: solo debe tener numeros")    

else:
    print("Cedula valida")                  

    # Ejercicio 3 ##

edad = int(input("Ingrese su edad: "))
tiene_documento = input("¿Tiene documento de identidad? (s/n): ")
tiene_autorizacion= input("¿Tiene autorizacion de un acudiente? (s/n) ")

if (edad >= 18 and tiene_documento == "s") or (edad < 18 and tiene_autorizacion == "s"):
     print("Inscripcion aprobada")

else:
    print("Inscripcion rechazada")     