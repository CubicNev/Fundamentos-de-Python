"""
Operador lógico not
Autor: Carlos Nevárez - CubicNev
Fecha: 7-Mayo-2024

El operador lógico not invierte el valor booleano al que se le aplica.
"""
# not hace la negación de una operación booleana
print(not True)
print(not False)

# --------- NAND --------- #
print('NOT AND') # Da False solo si ambas son verdadero
print('not True and True =>', not (True and True)) # False
print('not True and False =>', not (True and False)) # True
print('not False and True =>', not (False and True)) # True
print('not False and False =>', not (False and False)) # True

# Ejemplo
stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000)) # Encuetras los puntos que no esten dentro de los límites