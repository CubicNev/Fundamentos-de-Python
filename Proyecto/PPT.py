"""
Proyecto: Piedra, papel o tijeras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Programa que simula el juego piedra, papel o tijera. Usa una modalidad de computadora vs jugador.
"""
# Importaciones
import random

# Opciones:
options = ('piedra', 'papel', 'tijera')

# Se lee la opción del usuario y se pasa a mnusculas
user_option = input("piedra, papel o tijera: ").lower()

# Valida que la opcion ingresada se encuentre dentro de las opciones
if not user_option in options:
    print('Esa opciones no es valida')

# Se escoge una opcion de forma aleatoria
computer_option = random.choice(options)

#Generan opciones para la computadora
print('User option:', user_option)
print('Computer option:', computer_option)

if user_option == computer_option:
    print("Empate!")
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print("user gano!")
    else:
        print('papel gana a piedra')
        print('computer gana!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra!')
        print("user gano!")
    else:
        print('tijera gana a papel')
        print("compuer gano!")
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print("user gano!")
    else:
        print('piedra gana a tijera')
        print("compuer gano!")
else:
    print("Opcion invalida: ", user_option)
