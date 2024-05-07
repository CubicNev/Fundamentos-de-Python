"""
Operadores de comparación
Autor: Carlos Nevárez - CubicNev
Fecha: 7-Mayo-2024

Operadores de comparación. Regresan True o False.
"""
# > (Mayor que)
print(7 > 3) # True
print(3 > 7) # False
print(7 > 7) # False

# < (Menor que)
print(5 < 6) # True
print(6 < 5) # False
print(5 < 5) # False

# >= (Mayor o igual que)
print(2 >= 1) # True
print(2 >= 3) # False
print(2 >= 2) # True

# <= (Menor o igual que)
print(1 <= 2) # True
print(2 <= 1) # False
print(2 <= 2) # True

# == (Es igual a, estrictamente igualdad)
print(6 == 6) # True
print(5 == 2) # False

# != (Diferente de)
print(6 != 10) # True
print(6 != 6) # False

# Comparadores con Strings
print("Apple" == 'Apple') # True
print("Apple" == 'apple') # False, cambian en un caracter
print("1" == 1) # False, son tipos de datos diferentes

# Comparando con variables
age = 15
print(age >= 18)