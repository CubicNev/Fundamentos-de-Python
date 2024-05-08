# Manejo de Strings

---

## Métodos

Python tiene varios metodos nativos que nos hacen la vida más fácil al momento de manipular Strings.

> ⚠️ **Cuidado**: Todos los métodos devuelven nuevos valores, ninguno cambia la cadena original.

| Método | Descripción |
| --- | --- |
| `capitalize()` | Convierte el primer caracter a mayúscula |
| `casefold()` | Pasa todo el string a minúsculas |
| `center()` | Regresa un string centrado |
| `count()` | Devuelve el némero de veces que esta el valor específicado |
| `encode()` | Da una version codificada |
| `endswith()` | Devuelve `True` si el string termina con el valor específicado |
| `upper()` | Convierte el string a mayúsculas |
| `lower()` | Convierte el string a minúscilas |
| `swapcase()` | Convierte mayúsculas a minúsculas y viceversa |
| `startswith()` | Devuelve `True` si el string empieza con el valor específicado |
| `replace()` | Da un String en el que el valor específicado es reemplazado con otro valor especificado |
| `title()` | Convierte el primer carácter de cada palabra a mayúscula |
| `isdigit()` | Devuelve `True` si todos los caracteres del string son digitos |

> 💡 Para más metodos visitar: [Python - String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

## Indexig

Este concepto es aplicable a strings, pero también a otras estructuras de datos que se verán más adelante.

Los strings son arrays. Como muchos otros lenguajes de programación populares, los strings en Python son arreglos de bytes (carácteres).

Sin embargo, Python no tien un tipo de dato caracter, un solo caracter es simplemente un string de tamaño 1.

Se usan parentesís cuadrados `[]` para acceder a los elementos del string.

```python
a = "Python"
print(a[0]) # P
```

Tambien cuenta con una forma especial de indexacion, que es de izquierda a derecha, haciendolo con números negativos.

**Ejemplo:**

```python
a = "Python"
print(a[-1]) # n
```

De esta forma podemos inferir la siguiente tabla de indexacion.

**Ejemplo:**

|P|y|t|h|o|n|
|---|---|---|---|---|---|
|0|1|2|3|4|5|
|-6|-5|-4|-3|-2|-1|

## Slicing

Se pueden extraer subcadenas de un texto gracias al manejo por indices mencionado anteriormente. De esta forma se ingresa un rango del que se quiere extraer el subtexto.

**Ejemplo:**

```python
b = "Python"
print(b[2:4]) # th
```

> ⚠️ **Cuidado:** El rango se toma [n, m), es decir, toma un elemento antes del final. **No es inclusivo**.

### Cortando desde el inicio

Si no se esxcribe nada en donde debería estar el indice inicial, el rando empezara desde el primer caracter.

**Ejemplo:**

```python
b = "Python"
print(b[:2]) # Py
```

### Cortando hasta el final

Si se omite el indice que indica el final, el rango se irá hasta el final del String.

**Ejemplo:**

```python
b = "Python"
print(b[2:]) # thon
```

### Usando indexado negativo

Usar los indices negativos ayuda a cortar desde el final del String.

**Ejemplo:**

```python
b = "Python"
print(b[-3:-1]) # ho
```

### Cortando usando saltos

Normalmente se van haciendo saltos de uno en uno, pero si se desea hacer saltos de dos en dos o más, se debe agregar otros dos puntos a la derecha e indicar el número de saltos que se quieren hacer.

**Ejemplo:**

```python
b = "Bananananana" # 12 carácteres
print(b[1:10:2]) # aaaaa
```

|B|`a`|n|`a`|n|`a`|n|`a`|n|`a`|n|a|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|11|
