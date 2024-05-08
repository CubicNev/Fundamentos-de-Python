"""
Indexing y Slicing
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Se continua con las operaciones que se pueden hacer con Strings, recordemos que los String son cadenas de caracteres.
O en otras palabras, los strings son arreglos de caracteres, por lo que se puede acceder a cualquier posición indicando su
posicion.

De esta forma podemos obtener posiciones especificas o subtextos.
"""
# indexing

text = "Ella sabe Python"
print(text[0]) # Devuelve el primer caracter
print(text[1])
# print(text[999]) # Fuera de rango, lanza error

# Para ir a la ultima posición
size = len(text)
print('size => ',size) # 16
print(text[size - 1]) # La ultima poscion es 16 - 1, porque empieza en cero

# Forma más rápida de ir a la ultima posición
print(text[-1])

# slicing

print(text[0:5]) # Ingresas en intervalos del texto
print(text[10:16])
print(text[:10]) # Desde el inicio hasta el 10, por defecto toma el cero
print(text[5:-1]) # Desde el 5 hasta el final, no es incluyente
print(text[5:]) # Desde el 5 hasta el final de la cadena
print(text[:]) # Da toda la cadena

# Saltos

print(text[10:16:1]) # Indica que tome edel 10 al 16, dando un salto (lo normal)
print(text[10:16:2]) # Indica que tome edel 10 al 16, dando dos salto
print(text[::2]) # Del inicio al final saltando de a 2 elementos