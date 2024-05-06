"""
Booleanos
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Manejo de variables booleanas
"""
# Solo pueden tener True y False
is_single = True
print(type(is_single))
is_single = False
print(is_single)

# Convirtiendo True en False y False en True
print(not True)
print(not False)

# not es la operación logica que cambia al estado contrario
is_single = not is_single
print(is_single)