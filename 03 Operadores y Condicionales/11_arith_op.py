"""
Operadores Aritmeticos
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Operadores aritmeticos de python, dependiendo del tipo de dato el funcionamiento
cambia.
"""
# Operaciones matemáticas
# Operador de suma: +
print(10 + 10)
# Operador de resta: -
print(10 - 5)
# Operador de multiplicación: *
print(10 * 2)
# Operador de división: *
print(10 / 2) # 5
# Modulo (Regresa el residuo)
print(10 % 2) # 0

# División inexacta
print(10 / 3)
# El módulo si da residuo distinto de cero
print(10 % 3)

# División que solo toma valores enteros
print(10 // 3)
# Exponencial: **
print(2 ** 3)

# Haciendo operaaciones más complejas
"""
Orden de operaciones (llendo de izquierda a derecha):
P - Paréntesis
E - Exponentes
M - Multiplicación
D - División
A - Adicción
S - Sustracción
"""
print(2 ** 3 + 3 - 7 / 1 // 4)
# Sigue este orden:
print(2 ** 3) # = 8
print((7 / 1) // 4) # = 1
print(8 + 3 - 1)

# Cuidado con estas divisiones, no es valido
print(10 / 0)

# Con strings
# Concatena
print('Hola' + ' mundo')
# Repite la cadena 3 veces
print('Hola' * 3)