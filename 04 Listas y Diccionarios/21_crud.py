"""
Métodos de Listas
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Se hace un CRUD con los métodos de las listas.
"""
# CRUD Create, Read, Update & Delete (Crear, Leer, Actualizar y Elminar)

# Crear
numbers = [1, 2 , 3 , 4 , 5]
# Leer
print(numbers[1])
# Actualizar
numbers[-1] = 10
print(numbers)

# Agregar/Crear elementos dinamicamente
numbers.append(700) # Lo agrega al final de la lista
print(numbers)

numbers.insert(0, 'hola') # Agrega al inicio (posicion [0]) de la lista
print(numbers)

numbers.insert(3, 'change') # Inserta en posición 3, no elimina, solo toma ese espacio y recorre lo demas a la derecha
print(numbers)

# Unir dos listas
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

# Consultar en que indice se encuentra un elemento
index = new_list.index('todo 2')
# Cambiando el elemento en la posicion encontrada
new_list[index] = 'todo changed'
print(new_list)

# Eliminando un elemento, bucandolo
new_list.remove('todo 1')
print(new_list)

# Eliminando el ultimo elemento
new_list.pop()
print(new_list)

# Elimina el elemento de la posción 0
new_list.pop(0)
print(new_list)

# Voltea todo
new_list.reverse()
print(new_list)

# Ordenamiento de elementos
numbers_a = [1, 4, 6 , 3]
numbers_a.sort() # ordena de menor a mayor
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort() # ordena en orden alfabetico
print(strings)

# El método sort no puede ordenar cuando tiene tipos mezclados
#new_list.sort()
