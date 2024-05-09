# Listas

Es una coleccion con las siguientes características:

- Modificable
- Ordenada
- Permite elementos duplicados

## Creacion

Se crean usando parentesís cuadrados `[]`.

```python
lista = ["agua", "cereal", "papel"]
```

También se pueden crear con el constructor `list()`

```python
lista = list(("manzana", "platano", "cereza")) # nota los dobles parentesís
```

Como estan **ordenadas**, sus elementos estan indexados, el primero tiene el index `[0]`, el segundo `[1]`, etc. Al decir que esta ordenada, se refiere a que ya hay un orden definido y este no cambia.

Conforme se van agregando elementos estos se van agregando al final de la lista.

> 📝 **Nota:** Algunos métodos de `list()` va a cambiar el orden, pero en general el orden no cambia.

## Tipos de datos

Pueden contener cualquier tipo de dato:

```python
list1 = ["agua", "cereal", "papel"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

Y pueden contener diferentes tipos en una lista.

```python
types = [1, True, 'hola']
```

## Consulta de items

Se puede consultar por medio de los indíces.

```python
lista = ["apple", "banana", "cherry"]
print(lista[1]) # banana
```

> 📝 **Nota:**  El primer elemento tiene índice `[0]`.

De la misma forma se puede hacer un acceso por rangos.

```python
lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lista[2:5]) # ['cherry', 'orange', 'kiwi']
```

> 📝 **Nota:**  Recordar que no es inclusivo a la derecha, es decir se toma la notación `[n:m)`

Se puede verificar la existencia de algún elemento con el operador `in`.

```python
lista = ["apple", "banana", "cherry"]
print("apple" in lista) # True
```

## Cambiando items

Se hace por medio de indices, si es que se quiere cambiar uno en específico:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "platano" # ["apple", "platano", "cherry"]
```

Tambíen se pueden cambiar dentro de un rango.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["platano", "sandia"] # ['apple', 'platano', 'sandia', 'orange', 'kiwi', 'mango']
```

> 📝 **Nota:** Si pones más elementos de los que reemplazas, los nuevos se insertarán en donde los específiques y los restantes se van a mover más adelante. Y si agregas menos elementos de los que caben en el rango indicado, todo el rango sera reeplazado por los elemenots que pongas.

## Agregando items

### Con append()

Para agregar un elemento al final de la lista se usa el método `append(item)`

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # ["apple", "banana", "cherry", "orange"]
```

### Con insert()

También puedes insertar por medio del metodo `insert(indice, item)`, de esta forma los agregas sin reemplazar ningun otro elemento, solo los desplazas.

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # ['apple', 'banana', 'watermelon', 'cherry']
```

### Con extend()

Para agregar elementos de otra lista a la actual se usa el método `extend(list)`

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

> 📝 **Nota:** También funciona con otras estructuras, como tuplas.

## Eliminando items

### Con remove()

Usando `remove(item)` se elimina el elemento espicificado.

```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # ["apple", "cherry", "banana", "kiwi"]
```

### Eliminar con índices

Para eliminar un elemento usando su índice, se hace uso del método `pop(item)`

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # ["apple", "cherry"]
```

Si no se específica un índice se elimina el ultimo elemento.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop() # ["apple", "banana"]
```

#### Comando `del`

Este comando puede tanto eliminar un elemento.

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0] # ["banana", "cherry"]
```

Como toda la lista.

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

### Eliminando toda la lista

Para esto se usa el método `clear()`, el cual vacía toda la lista, esta aun existe pero no tiene elementos.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear() # []
```

## Métodos utiles

### reverse()

Invierte el orden de la lista.

```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse() # ['cherry', 'banana', 'apple']
```

### sort()

Va a ordenar de forma alfanumerica de forma ascendente.

> ⚠️ **Cuidado:** No ordena los elementos dentro de la lista son de distinto tipo.

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort() # [23, 50, 65, 82, 100]
```

> 📝 **Nota:** Si se quiere ordenar de forma descendente se debe invocar asi: `sort(reverse = True)`
