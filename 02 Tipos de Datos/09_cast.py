"""
Tranformacion
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Transformación de tipos de datos
"""
# Variable de tipo string
name = "Nicolas"
print(type(name))
# Cambio dinamico de string a entero
name = 12
print(type(name))
# Cambio dinamico de entero a booleano
name = True
print(type(name))

# Cuidado con el tipo de datos que haces en operaciones
# Concatena
print("Nicolas" + " Molina")
# Suma
print(10 + 20)

# Error: print("Nicolas" + 12)
print("Nicolas" + "12")

# Número a String
age = 12
# Pasa entero a string para concatenar
print("Mi edad es " + str(age))
# Concatenando usando formateo de texto, hace la transformacion en "automatico"
print(f"Mi edad es {age}")

# String a Número
# Entrada de edad, entra como entero
age = input('Escribe tu edad => ')
print(type(age))
# Transformar edad entero
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')