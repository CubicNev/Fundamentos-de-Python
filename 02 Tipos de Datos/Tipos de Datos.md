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

## Obtener el tipo de dato de una variable

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

Los string estan rodeados ya sea por comillas simples o comillas dobles.

`"hola"` es lo mismo que `'hola'`

Puedes imprimir un string como *literal* con la función `print()`

```python
print("Hello")
print('Hello')
```

Alternando entre las comillas puedes hacer un uso facil de uno u otro:

```python
print("I'm Carlos")
print('El dijo "No le sabes al POV"')
```

### Asignacion

```python
cadena = "Soy una cadena"
diavlo = 'DIAVLO! yo tambien soy una cadena'
```

### Strings multilinea

Usando las triples comillas se pueden tener strings largos, *i.e.*

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
```

## Numeros

Hay tres tipos de numeros:

* `int`
* `float`
* `complex`

De la misma forma que las cadenas, se crean asignando un valor:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

## Booleanos

Representan dos valores: `True` o `False`
Al evaluar expresiones puedes obtener cualquiera de estos dos valores, por ejemplo cuando comparas dos valores:

```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

### La mayoría de valores son True

Al hacer `bool(variable_o_valor)` normalmente te devolverá `True`, *i.e.*

* Cualquier string no vacío es `True`
* Cualquier numero es `True`, excepto si es `0`
* Cualquier list, tuple, sey y dictionary son `True`, excepto los vacios.

```python
# True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

### Asignación

```python
verdadero = True
falso = False
```

## Transformación (*Casting*)

Python es un lenguaje orientado a objetos, por loq ue usa clases para definir tipos de datos, incluyendo los datos primitivos.

Se tienen los siguientes constructores (hay más) para transoformar datos:

* `int()`
* `float()`
* `str()`

De tal forma que:

```python
x = int(1)   # x = 1
y = int(2.8) # y = 2
z = int("3") # z = 3

x = float(1)     # x = 1.0
y = float(2.8)   # y = 2.8
z = float("3")   # z = 3.0
w = float("4.2") # w = 4.2

x = str("s1") # x = 's1'
y = str(2)    # y = '2'
z = str(3.0)  # z = '3.0'
```
