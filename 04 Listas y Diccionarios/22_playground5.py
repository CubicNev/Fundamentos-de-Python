"""
Agrega, modifica y elimina elementos de una lista
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Con la lista proprcionada, realizar las siguientes operaciones:
1) Agregar la letra G al final de la lista.
2) Reemplazar la letra en la posición 0 con la letra Z.
3) Eliminar la letra C de la lista.
4) Imprimir la lista resultante al revés.
"""

letters = ['A', 'B', 'C', 'D', 'E', 'F']
# Escribe tu solución 👇
# 1
letters.append('G')
# 2
letters[0] = 'Z'
# 3
letters.remove('C')
# 4
letters.reverse()
print(letters)