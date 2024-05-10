"""
Ciclos Anidados
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

Los ciclos anidados son ciclos dentro de otro ciclo
"""
# Lista anidada que puede también tomarse como una tabla con filas y columnas
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0][1])

# Itera por fila
for row in matriz:
    # Accede a una lista
    print(row)
    # Itera por columna,
    for column in row:
      # Accediendo a un elemento
        print(column)