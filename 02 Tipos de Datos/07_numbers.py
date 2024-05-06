"""
Numeros
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Manejo de datos numericos
"""

# int's
lives = 3 # Vidas de un juego (buena practica: nombrar variables con nombres descriptivos)
print(type(lives))
age = 12
budget = 100

# floats
temperature = 12.12
print(type(temperature))

# Actualizando valores
lives = 2
print(lives)
lives = 1
print(lives)

# Haciendo operaciones aritmeticas
lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1 # Uso de operador que abrevia la operacion de arriba
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

# Numeros muy grandes
number = 4500000000000000000.1
print(number) # Imprime en numeración cientifíca

# Números muy pequeños
number_b = 0.0000000000000001
print(number_b) # Imprime en numeración cientifíca


# Reto: Calcular el promedio gastos mensuales (3 meses)
jan_budget = float(input("Presupuesto de enero: "))
feb_budget = float(input("Presupuesto de febrero: "))
mar_budget = float(input("Presupuesto de marzo: "))

print(f"El presupuesto promedio es {(jan_budget + feb_budget + mar_budget)/3}")