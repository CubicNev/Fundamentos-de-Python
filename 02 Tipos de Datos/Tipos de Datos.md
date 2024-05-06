# Tipos de Datos en Python
La informacion que se guarda en las variables de python se pueden distinguir por tipo de dato, aunque no se especifique en su declaración explicitamente.

Python tiene los siguientes tipos de datos por default:
* Texto: `str`
* Numericos: `int`, `int`, `float`
* De secuencia: `list`, `tuple`, `range`
* Mapeo: `dict`
* Conjunto: `set`, `frozenset`
* Booleanos: `bool`
* Binarios: `bytes`, `bytearray`, `memoryview`
* None: `NoneType`

## Obtener el tipo de dato de una variable.
Se puede ver de qué tipo es una variable usando la funcion `type()`, *i.e.*

```python
x = 3
print(type(x))
```

## Asigando el tipo de dato
El tipo de dato se asigna cuando se le da un valor al dato:
| Ejemplo                                      | Tipo de dato           |
| ---------------------------------------------|------------------------|
| x = "Hello World"                            | `str`                  |
| x = 20                                       | `int`                  |
| x = 20.5                                     | `float`                |
| x = 1j                                       | `complex`              |
| x = ["apple", "banana", "cherry"]            | `list`                 |
| x = ("apple", "banana", "cherry")            | `tuple`                |
| x = range(6)                                 | `range`                |
| x = {"name" : "John", "age" : 36}            | `dict`                 |
| x = {"apple", "banana", "cherry"}            | `set`                  |
| x = frozenset({"apple", "banana", "cherry"}) | `frozenset`            |
| x = True                                     | `bool`                 |
| x = b"Hello"                                 | `bytes`                |
| x = bytearray(5)                             | `bytearray`            |
| x = memoryview(bytes(5))                     | `memoeryview`          |
| x = None                                     | `NoneType`             |

De la misma forma también se puede especificar el tipo de dato usando constructores.

## Strings básicos

## Numeros

## Booleanos

