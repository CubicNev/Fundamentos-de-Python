# Diccionarios

Los diccionarios guardan datos en pares de llave-valor. Sus características son:

- Odenados (De Pyhton 3.6 en adelante)
- Modificables
- No permiten duplicación

Se crean usando `{}` o el constructor `dict()` y puede almacenar distintos tipos de datos.

```python
# Con {}
my_dict = {
    # 'llave' : <valor>
    'avion': False,
    'name': 'Nicolas',
    'last_name': 'Molina Monroy',
    'age': 87,
    "Educacion": ["Primaria", "Secundaria", "Bachillerato", "Licenciatura"]
}
# Con constructor
dict = dict(name = "John", age = 36, single = True)
```

## Accesando a los datos

Se puede acceder por medio del la llave, o por el método `get()` que soporta errores y devuelve `None` si no existe la llave.

```python
x = my_dict["name"]
y = my_dict.get("apellido")
```

> 📝 **Nota:** Si se desea validar la existencia de una llave se puede usar el operador `in`

### Obtenido todos los items

Se usa el método `items()`

```python
my_dict.items() # dict_items([('name', 'santi'), ('langs', ['python', 'javascript', 'rust'])])
```

### Obteniendo solo llaves

Se usa el metodo `keys()`

```python
my_dict.keys() # dict_keys(['name', 'langs'])
```

### Obteniendo solo valores

Se usa el metodo `values()`

```python
my_dict.values() # dict_values(['santi', ['python', 'javascript', 'rust']])
```

## Agregar items

Se hace usando una nueva llave y asignandole un valor

```python
dic = {
    "nombre": Humberto
    "edad": 87
}

dic["jubilado"] = True
```

## Actualizar el diccionario

Se hace por medio del método `update({key:value})`, cambiara los elementos dados en el argumento. Si no existen los agrega. De argumentos debes poner un diccionario o un objeto iterable con pares `llave:valor`

```python
dic = {
    "nombre": Humberto
    "edad": 87
}

update({"edad": 80})
```

## Eliminando

Existen varios métodos, el primero que veremos es `pop(llave)` que elimina el elemento con la llave especificada, para hacer algo similar se puede usar `del` (Que tambíen podrias eliminar el diccioario completo si no se especifica una llave):

```python
person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age': 99
}

person.pop('age') # argumento obligatorio

# Alternativa
del person['last_name']
```

Para eliminar el ultimo elemento insertado se usa el metodo `popitem()`

person.pop('age') # Poner si o sí la llave, argumentos obligatorios

```python
person.popitem()
```

Como se menciono anteriormente si se quiere eliminar por completo el diccionario se puede usar `del` sin especificar llaves, o bien, se puede usar `clear()` para solo **vaciarlo**.

```python
# Vacia
person.clear()
# Elimina
del person
```

## Extra

### `copy()`

Método para copiar el contenido de un diccionario a otro.

```python
person = {
    'name': 'nico',
    'last_name': 'molina',
    # Puede contener otros tipos de datos
    'langs': ['python', 'javascript'],
    'age': 99
}

user = person.copy()
# Alternativa:
user = dict(person)
```

### Diccionarios anidados

Como los diccionarios contienen todo tipo de datos, tambíen pueden contener diccionarios.

```python
# Forma 1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Forma 2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

El acceso se hace haciendo doble llave

```python
print(myfamily["child2"]["name"])
```

Y puedes recorrerlos de la siguiente forma:

```python
for llave, valor in myfamily.items():
  print(llave)

  for subvalor in valor:
    print(subvalor + ':', valor[subvalor])
```
