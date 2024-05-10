"""
Ciclo While
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

Los ciclos son una forma de repetir instrucciones cierto número de veces hasta que una condición se cumpla.
While se traduce a mientras. "Mientras la condición se cumpla, se ejecutan las instrucciones"
No se tiene muy claro el número de iteraciones que se va a hacer.
"""
# Sintaxis similar a un if
while True: # Ciclo infinito
    print('se ejecuto')
    break # Lo detengo a la fuerza

print("-"*10)
counter = 0
# Mientras el contador sea menor a 10, se va a ejecutar
while counter < 10:
    counter += 1
    print(counter) # Se repite 10 veces

print("-"*10)
counter = 0
# Rompiendo el flujo antes de que se cumpla la condición
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)

print("-"*10)
counter = 0
# El print no se ejecuta a menos que el contador sea menor a 15
while counter < 20:
    counter += 1
    if counter < 15:
        continue # Se salta el print
    print(counter)