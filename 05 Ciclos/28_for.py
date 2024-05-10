"""
Ciclo For
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

Se usa para iterar con base a un elemento.
"""

# for elemento_iterador in rango
for element in range(1, 21): # Itera del 1 al 20
    print(element)

print("-"*10)

# Tambíen se usa para recorrer estructuras
# Lista
my_list = [23, 45, 67, 89 ,43]
for element in my_list:
    print(element)

print("-"*10)
# Tupla
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)

# Diccionario
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
print("-"*10)
# Iterando, pero solo las llaves
for key in product:
    print(key, '=>', product[key])

print("-"*10)
# Iterando por los pares
for key, value in product.items():
    print(key, '=>', value)

# Lista de diccionarios (Estructura muy común en desarrollo)
people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

print("-"*10)
print("Iterando una lista de diccionarios: ")
for person in people:
    print('name =>', person['name'])