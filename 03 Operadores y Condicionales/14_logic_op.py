"""
Operadores lógicos
Autor: Carlos Nevárez - CubicNev
Fecha: 7-Mayo-2024

Se hace uso de los operadores logicos not y or, lo cuales siguien el comportamiento a sus homonimos en el algebra booleana
"""

# ------ Operador and ------ #
print('AND') # Solo da True si ambos lados es True, sigue la logica de algebra booleana
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

# Combinando con otros operadores
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

# Ejemplo de aplicacion: Ver si tengo el stock correcto
stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# ------ Operador or ------ #
print('OR') # Da True si alguno de los lados es True
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

# Ejeplo de aplicacion: Ver si el rol de empleado corresponde a administrador o vendedor
role = input('Digita el rol => ')

print(role == 'admin' or role == 'seller')