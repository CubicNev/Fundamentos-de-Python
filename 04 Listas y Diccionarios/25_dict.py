"""
Diccionarios
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

Actualizacion y eliminacion de elementos dentro de un diccionario.
"""
# Declaración
person = {
    'name': 'nico',
    'last_name': 'molina',
    # Puede contener otros tipos de datos
    'langs': ['python', 'javascript'],
    'age': 99
}

print(person)

# Actualizacion de valores
person['name'] = 'santi' # Reemplazo
person['age'] -= 50 # Ajustes sobre valor actual
person['langs'].append('rust') # Agregando valores a la lista
print(person)

# Eliminacion de atributos, siempre usando llaves
del person['last_name']
person.pop('age') # Poner si o sí la llave, argumentos obligatorios

print(person)

# Métodos utiles
print('items')
print(person.items()) # Obtener los items de un diccionario, una lista en pares de tuplas, pares (clave, valor)

print('keys')
print(person.keys()) # Obtener las keys de un diccionario, lista con las llaves

print('values')
print(person.values()) # Una lista de solo los valores
