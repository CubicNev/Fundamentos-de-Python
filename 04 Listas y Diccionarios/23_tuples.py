"""
Tuplas
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Estrucutra de control inmutable.
"""
# Declaración, importante usar parentesís.
numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')

# Misma forma de consultar que una lista
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUDn't, no se puede hacer modificaciones solo es de lectura
# numbers.append(10) # invalido
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule')) # Buscar en qué posición esta el elemento zule
print(strings.count('nico')) # Contar cuantas veces hay un elemento en la tupla

# Para manipular podemos convertir una tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

# Se puede pasar de tupla a lista
my_tuple = tuple(my_list)
print(my_tuple)