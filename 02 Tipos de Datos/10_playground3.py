"""
Playground 3: Imprime el formato adecuado
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

En este desafío, se te proporcionará un código base encontrarás las variables name y age todas como strings.
Tu tarea es crear un formato de string que, como resultado, muestre un mensaje en la sección Terminal.
El mensaje deberá tener la siguiente forma:
Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años
"""
name = 'Juana'
print(name)
age = '10'
print(age)

total = int(age) + 10

template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
print(template)