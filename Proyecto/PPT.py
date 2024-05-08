"""
Proyecto: Piedra, papel o tijeras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Programa que simula el juego piedra, papel o tijera. Usa una modalidad de computadora vs jugador.
"""

user_option = input("piedra, papel o tijera: ").lower()
computer_option = 'piedra'

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
