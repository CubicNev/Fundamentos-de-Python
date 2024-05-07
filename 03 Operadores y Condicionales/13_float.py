"""
Comparación de números flotantes
Autor: Carlos Nevárez - CubicNev
Fecha: 7-Mayo-2024

Python maneja la apreciación decimal de forma especial, este codigo ve los casos a tomar
en cuenta
"""
# Se tiene diferente precisión
x = 3.3
print(x) # 3.3
y = 1.1 + 2.2
print(y) # 3.3000000000003
print(x == y) # False

# Forma brusca, con strings
y_str = format(y, ".2g") # Hacer que solo tenga dos digitos
print('str =>', y_str) # 3.3
print(y_str == str(x)) # Se comparan, pero ambos deben ser del mismo tipo

print('*' * 10) # Separación, imprime linea divisora

print(y, x)

# Forma más matemática
tolerance = 0.00001
# Se resta x menos y para sacar la diferencia en una precisicón decimal, luego se compara bajo un margen de error
print(abs(x - y) < tolerance)

print('*' * 10)

# Tambíen se puede optar por redondear
y = round(y,1) # Redondea a un dígito
print(x == y)