# Proyecto: Piedra, papel o tijeras

El proyecto consiste en el juego "Piedra, Papel o Tijeras", el programa sigue la lógica del juego y permite jugar contra la computadora.

**Nombre del archivo principal:** `PPT.py`
**Descripción:** Es la abreviación de Piedra, Papel o Tijeras
**Metodología:** Incremental.

## Incremento 1

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
