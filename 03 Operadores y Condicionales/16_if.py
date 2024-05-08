"""
Condicionales if
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Se usa if de distintas formas.
Para mas ejercicios ir a: https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
"""
if True:
    print('debería ejecutarse')

if False:
    print('nunca se ejecuta')

# Evaluación de varias opciones
pet = input('¿Cuál es tu mascota favorita? R: ')

if pet == 'perro':
    print('genial tienes buen gusto')
elif pet == 'gato':
    print('espero tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print('no tienes ninguna mascota interesante')

# Uso de if-else, y operador and
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')

# Ver si un número es par, propuesta 1
num = int(input('Ingrese un numero: '))
if (num % 2):
	print('Es impar')
else:
	print('Es par')

# Ver si un número es par, propuesta 2. Se usan operadores de bit y expresiones condiconales.
n = int(input('Ingrese un numero: '))
print("Es par") if ~n & 1 else print("Es impar")
