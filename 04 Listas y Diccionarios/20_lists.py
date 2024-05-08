"""
Listas
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Se hace el manejo básico de listas
"""
# Declaración
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

# Lista de cadenas
tasks = ['make a dishes', 'play videogames']
print(tasks)

# Guardando distintos tipos de datos
types = [1, True, 'hola']
print(types)

# Se maneja por indices
print(numbers[0])
print(tasks[0])

# Las cadenas no se pueden modificar con indices (inmutables)
text = 'Hola'
# text[0] = 'W' # error, string inmutable

# Cambia 'make dishes' por 'watch platzi courses'
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

# Seleccion de subgrupos de elementos
print(numbers[:3])
# Saber si existe un elemento dentro de la lista
print(True in types)
print('hola' in types)
