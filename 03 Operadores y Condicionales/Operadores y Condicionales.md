# Operadores y Condicionales

Los operadores se usan para realizar operqaciones en variables y valores.

Python divide los operadores en los siguientes grupos:

* Arimeticos
* Asiganación
* Compración
* Logicos
* Identidad
* Membership
* Bitwise

---

## Operadores aritméticos

Los operadores aritmeticos se usan con valores numericos para hacer operaciones matemáticas comunes.

Operador | Nombre | Ejemplo
--- | --- | ---
`+` | Suma | `x + y`
`-` | Resta | `x - y`
`*` | Multiplicacion | `x * y`
`/` | Division | `x / y`
`%` | Módulo | `x % y`
`**` | Exponenciación | `x ** y`
`//` | División piso | `x // y`

Hay que tomar en cuenta la jeraquía de operadores que usa Python, llendo de izquierda a derecha.

* `P` - Paréntesis
* `E` - Exponentes
* `M` - Multiplicación
* `D` - División
* `A` - Adicción
* `S` - Sustracción

---

## Operadores de comparación

Se usan para comparar dos valores y establecer una relación entre ellos. Devuelven un valor booleano (`True` o `False`) basado en la condición.

Operador | Nombre | Ejemplo
--- | --- | ---
`==` | Igual a | `x == y`
`!=` | Diferente a | `x != y`
`>` | Mayor que | `x > y`
`<` | Menor que | `x < y`
`>=` | Mayor o igual a | `x >= y`
`<=` | Menor o igual a | `x <= y`

---

## Operadores lógicos

Los operadores lógicos se usan para combinar sentencias condicionales. Siguen la lógica de la operación logica a la que hacen referencia.

Operador | Descripcion | Ejemplo
--- | --- | ---
`and` | Regresa `True` si ambas sentencias con verdaderas | `X and Y`
`or` | Regresa `True` si una de las sentencias es verdadera | `X or Y`
`not` | Regresa `Falso` si la sentencia es verdera, la revierte | `not X`

> 📝 **Nota:** `X`,`Y` son sentencias como: *a > b*, *a == b*, ...

Las tablas de verdad de las operaciones lógicas son:

a | b | AND
--- | --- | ---
True | True | True
True | False | False
False | True | False
False | False | False

a | b | OR
--- | --- | ---
True | True | True
True | False | True
False | True | True
False | False | False

a | NOT
--- | ---
True | False
False | True

---

## Condicionales

Ya se han visto las operaciones de comparación (también conocidas como operaciones condicionales). Estás usualmente se usan dentro de **sentencias if** y ciclos.

> 📝 **Nota:** Recordar que se pueden combinar operaciónes de comparación con operadores lógicos (`and`, `or` y `not`).

Las *sentencias if* se escriben usando la palabra clave `if` seguido de una operacion que regrese `True` o `False`, y al final se añaden dos puntos `:`.

Entonces se hace se la siguiente forma:

```python
a, b = 33, 200 # Declaración multiple
if b > a:
    print("b es mayor que a")
```

> ⚠️ **Cuidado**: Python usa *espacios* o *tabulaciónes* al inicio de una línea para marcar un bloque de código. De esta forma dentro de los bloques `if` se marca todo lo que se realiza dentro del if **identando** las operaciones.

### elif

La palabra clave `elif` es la forma en la que se le indica a Python que si la condición previa no se cumplio, entonces intente otra condición.

```python
a, b = 33, 200
if b > a:
    print("b es mayor que a")
elfi a==b:
    print("a y b son iguales")
```

### else

La palabra clave `else` es la forma de decir "Si nada de lo anterior se cumple, entoces haz esto"

```python
a, b = 33, 200
if b > a:
    print("b es mayor que a")
elif a==b:
    print("a y b son iguales")
else:
    print("a es mayor que b")
```

### Operadores ternarios

**if corto:** Si solo se va a ejecutar una instruccion puedes poner esa intrucción en la misma línea que la condiconal `if`.

```python
if a > b: print("a es mayor que b")
```

**if-else corto:** Si solo se va a ejecutar una instruccion en el `if`, y una en el `else`, se puede hacer en una sola línea.

```python
print("A") if a > b else print("B")
```

Estas tecnicas tambíen son conocidas como **Expresiones condicionales**. También se pueden usar multiples `else` en la misma línea.

```python
print("A") if a > b else print("=") if a == b else print("B")
```

### Últimos detalles

Los if´s se pueden anidar, ya que siguen siendo bloques de código.

```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

Si se quiere tener un bloque `if` vacío (por alguna razón), se puede poner la palabra clave `pass` para que no nos marque error.

```python
if b > a:
  pass
```
