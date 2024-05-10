# Ciclo for

Se usan para iterar, normalmente sobre una secuencia como una lista, tupla, diccionario, conjunto (`set`), o string

Se usa la palabra clave `for` y a diferencia que otros lensuajes se usa como un iterador.

```python
fruits = ["apple", "banana", "cherry"]
# Recorre la lista
for x in fruits:
    print(x)

# Recorre la cadena
for x in "banana":
    print(x)
```

## Intrucciones complementarias

Al igual que en el ciclo `while` se usan las instrucciones `break` para parar el ciclo, `continue` para saltar a la siguiente iteración, `else` para indicar que accion se realiza una vez terminado el ciclo.

Si se quiere usar para ejecutar un bloque cierto numero de veces se puede hacer uso de la función `range()`. Devuelve una secuencia de numeros, empieza con 0 por default e incremeneta en 1 por default, solo necesita que especifiques el número en el que debe terminar.

```python
for x in range(6):
    print(x)
"""
Salida:
0
1
2
3
4
5
"""
```

> 📝 **Nota:** No recorre hasta el 6, va del 0 al 5

Es posible especificar un rango: `range(2, 6)` que significa que recorrera del 2 al 6 sin incluir el 6.

```python
for x in range(2, 6):
    print(x)
```

Si se quiere hacer que los incrementos no sean de 1 en 1, se especifica un tercer parámetro `range(2, 30, 3)`

```python
for x in range(2, 30, 3):
    print(x)
```

Se puede tener un ciclo vacío, es decir que no haga nada, usando solo la palabra `pass` dentro del bloque. Se usa para que no marque errores si hacemos un ciclo vacío

```python
for x in [0, 1, 2]:
    pass
```

## For anidados

Mete un for dentro de otro!

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```
