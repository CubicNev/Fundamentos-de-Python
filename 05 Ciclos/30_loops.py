"""
Ciclos Anidados
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

"""
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0][1])

for row in matriz:
    print(row)
    for column in row:
        print(column)