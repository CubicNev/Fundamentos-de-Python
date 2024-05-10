# Tuplas

Es una estructura de datos que sirve para almacenar multiples elementos en una sola variable. Tiene las siguientes características:

- **Ordenada:** Los elementos tienen un orden definido, y ese orden no cambia.
- **Inmutable:** No se pueden hacer cambios al contenido de una lista, esto abarca agregar o eliminar y ese orden no cambiara.
- **Elementos repetibles:** Como son indexadas, pueden tener elementos con el mismo valor.

Para su declaración se usan parentesís, o bien su constructor.

```python
tupla = ("halo", "minecraft", "fortnite", "halo")
tupla = tuple(("halo", "minecraft", "fortnite"))
```

Si se quiere tener una tupla con un elemento se tiene que agregar una coma después del elemento. *i.e.*

```python
tupla = ("Hitori Bocchi",)
```

Puede contener ser de todo tipo de datos, e incluso una mezcla de distintos tipos.

```python
tuplaT = ("halo", "minecraft", "fortnite")
tuplaN = (23, 42, 7, 3, 2)
tuplaB = (True, False, False)
tuplaM = ("XD", False, "Ado", 1000)
```

Desde el punto de vista de python, las tuplas son un objeto con el tipo de dato `tuple`:

```text
<class 'tuple'>
```

## Acceso a los datos

Se puede acceder a un elemento individual haciendo uso de su indice, permitiendo todas las funcionalidades de la indexación de Python (Acesso simple, acceso con indices negativos, acceso con un rango de índices).

```python
tupla = ("halo", "minecraft", "COD", "elden ring", "fallout 4", "helldivers", "fortnite")
# Por indice
print(tupla[1]) # minecraft
# Por indice negativo
print(tupla[-1]) # fortnite
# Por rango de indices
print(tupla[2:5]) # ('COD', 'elden ring', 'fallout 4')
print(tupla[:4]) # ('halo', 'minecraft', 'COD', 'elden ring')
print(tupla[2:]) # ('COD', 'elden ring', 'fallout 4', 'helldivers', 'fortnite')
print(tupla[-4:-1]) # ('fallout 4', 'helldivers', 'fortnite')
```

### Comprobar la existencia de un elemento

Se usa la palabra reservada `in` para ver si un elemento se encuentra en una tupla.

```python
tupla = ("halo", "minecraft", "fortnite")
print("halo" in tupla) # True
```

## Hacer cambios

Como las tuplas son **inmutables** para cambiar sus valores es necesario cambiarla a una `lista` para hacer cambios, y luego convertirla de vuelta a tupla.

```python
tupla = ("halo", "minecraft", "fortnite")
l = list(tupla)
l.append("mario kart")
l[2] = "lego fortnite"
tupla = tupla(l)
```

### Sumar tuplas

Esta permitido sumar tuplas, de esta forma se pueden agregar items. Crea una nueva tupla con los items que deseas agregar.

```python
t = ("halo", "minecraft", "fortnite")
t_aux = ("god of war",)
t +=t_aux
print(t) # ('halo', 'minecraft', 'fortnite', 'god of war')
```

### Eliminar

Se sigue el mismo proceso para agregar elementos.

```python
t = ("halo", "minecraft", "fortnite")
l = list(t)
l.remove("halo")
t = tuple(l)
```

Si se quiere eliminar por completo se puede usar `del`

```python
tupla = ("halo", "minecraft", "fortnite")
del tupla
```

## Desempacar los elementos de una tupla

Cuando se crea una tupla con elementos se le llama "empacar" o "*packing*". Al extraer los alores en variables se le llama desempacar o "*unpacking*"

```python
tupla = ("halo", "minecraft", "fortnite")
(shooter, classic, service) = tupla
```

> ⚠️ **Cuidado**: El número de variables de coincidir con el número de elemetos en la lista

Si el numero de variables es menor al numero de elementos, se puede agregar un `*` al nombre de una variable y de esta forma los valores se asignaran en esta en forma de lista.

```python
tupla = ("halo", "minecraft", "COD", "elden ring", "fallout 4", "helldivers", "fortnite")
(shooter, classic, *other) = tupla

# Tambien es valido (shooter, *classic, other) = tupla
# El último valor se asigna a la ultima variable
```

## Operaciones

Las tuplas se pueden sumar y multiplicar

```python
# Suma de tuplas
j1 = ("halo", "minecraft", "fortnite")
j2 = ("COD", "elden ring", "fallout 4", "helldivers")
j3 = j1 + j2

# Multiplicación de tuplas
t = ("apple", "banana", "cherry")
tM = t * 2 # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

```

Tambíen se puede consultar el número de elementos dentro de una lista con `count()`. Para obtener el índice de un valor se usa `index(valor)`

Una opereación util es escoger un elemento al azar usando randoom.

```python
import random

options = ('piedra', 'papel', 'tijera')

# Se escoge una opcion de forma aleatoria
computer_option = random.choice(options)
```
