# Proyecto: Piedra, papel o tijeras

El proyecto consiste en el juego "Piedra, Papel o Tijeras", el programa sigue la lógica del juego y permite jugar contra la computadora.

- **Nombre del archivo principal:** `PPT.py`
- **Descripción:** Es la abreviación de Piedra, Papel o Tijeras
- **Metodología:** Incremental.

## Incremento 1

**Fecha:** 8/Mayo/2024

Se agregan condiconales. La opcion que selecciona la computadora, de momento esta estática y se hace desde dentro del código. Pero la lógica ya esta implementada.

```python
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
```

## Incremento 2

**Fecha:** 8/Mayo/2024

Se valida que independientemente a lo que ingrese usuario, siempre se manejara el texto en minúsculas.

```python
user_option = input("piedra, papel o tijera: ").lower()
```

Se agrega una validación para cuando no se ingresa una de las opciones.

```python
if False:
    pass # Parte ya implementada arriba
else:
    print("Opcion invalida: ", user_option)
```

## Incremento 3

Se implementan tuplas para tener unicamente las tres opciones: pridra, papel o tijeras. Como las tuplas son **inmutables** nos sirve porque no usamos nada más que esas opciones.

```python
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
```

De la misma forma con tuplas se permite validar que la opcion ingresada se encuentre dentro de las opciones de la tupla, y también, se implementa una funcionalidad que ayuda a que la computadora elija de forma aleatoria una opción de la tupla.

## Incremento 4

**Fecha:** 10/Mayo/2024

Se agregan ciclos para que el juego tenga varias rondas. De forma que se determina un ganador cuando uno de los dos contrincantes gane al menos 2 veces.

- Se agrega un contador de rondas

```python
rounds = 1
```

- Se agrega dos contadores para contar cuantas wins lleva cada jugador

```python
computer_wins = 0
user_wins = 0
```

- Se agregan un aumento en el contador de wins del usuario cada vez que gana.

```python
user_wins += 1
```

- Se agregan un aumento en el contador de wins de la computadora cada vez que gana.

```python
computer_wins += 1
```

- Se agrega una validación para ver cuando alguno de los dos jugadores ha ganado dos veces:

```python
if computer_wins == 2:
    print(' COMPUTER WINS!!!!')
    break
elif user_wins == 2:
    print(' COMPUTER WINS!!!!')
    break
```

- Se agrega el depliegue de los contadores

```python
print('computer_wins:', computer_wins)
print('user_wins:', user_wins)
```

- Se agrega un `continue` dentro de la validación de opciones para saltar rondas cuando no se ingresa algo valido.

```python
# Valida que la opcion ingresada se encuentre dentro de las opciones
if not user_option in options:
    print('Esa opciones no es valida')
    continue
```
