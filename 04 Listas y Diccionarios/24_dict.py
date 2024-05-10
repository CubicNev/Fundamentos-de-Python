"""
Diccionarios
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

El nombre de esta estrucutra hace referencia a su funcionamiento, en un diccionario se busca una palabra para
saber su significado, esta palabra sirve como una llave y su definicion sería su valor.
"""
# Definicion con corchetes
my_dict = {}
print(type(my_dict))

my_dict = {
    # 'llave' : <valor>
    'avion': "bla bla bla",
    'name': 'Nicolas',
    'last_name': 'Molina Monroy',
    'age': 87
}

print(my_dict)
print(len(my_dict)) # Cuántos elementos hay en el diccionario

# Lectura de diccionario
print(my_dict['age']) # En vez de índice, se busca directamente con la llave
print(my_dict['last_name'])
print(my_dict.get('age')) # Mismo resultado, pero si no existe, puede manejarlo y devolver <None> Previenes errores.

# Ver si existe una llave dentro del diccionario
print('avion' in my_dict)
print('otroqueno' in my_dict)