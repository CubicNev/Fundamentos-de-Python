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
<p style="color:blue"> True </p> | True | True
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
