"""
Ciclo While
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 10-Mayo-2024

"""
'''
while True:
    print('se ejecuto')


counter = 0

while counter < 10:
    counter += 1
    print(counter)


counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)