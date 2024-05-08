"""
String Recargado
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Se hacen distintas operaciones con los Strings.
"""
# Mensaje inicial
text = 'Ella sabe programar en Python'

'''
# Ver si hay un subtexto dentro de text (Usando el operador in)
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien')

'''

# Para evaluar el tamaño de un string, en número de caracteres
size = len(text)
print(size)

# Métodos de String
print(text)
# De transformación
print(text.upper())
print(text.lower())
print(text.swapcase())
# De consulta
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.count('a'))
# De consulta y transformación
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
# Tranformación
print(text_2.capitalize())
print(text_2.title())
# Consulta
print(text_2.isdigit())
print("398".isdigit())