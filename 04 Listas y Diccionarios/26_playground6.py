"""
Playgrounde 6: Agrega, modifica y elimina elementos de un diccionario
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

En este desafío, se te proporcionará un diccionario llamado person que contiene información sobre una persona. Tu reto es realizar las siguientes operaciones en orden:

1. Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
2. Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
3. Eliminar el elemento del diccionario con la llave "age".
4. Imprimir una lista con las llaves del diccionario.
5. Imprimir una lista con los valores del diccionario.
"""
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
# 1
person["twitter"] = "@nicobytes"

# 2
person['name'] = "Felipe"

# 3
person.pop("age")

# 4
print(list(person.keys()))

# 5
print(list(person.values()))