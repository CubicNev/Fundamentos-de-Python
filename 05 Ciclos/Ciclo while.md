# Ciclo While

El ciclo `while` se ejecuta **mientras** ña condición dada sea verdadera.

```python
# Este ciclo es infinito
while True:
    print("ryoiki tenkai: fukuma mizushi")
```

> ⚠️ **Cuidado**: Aqui cobra relevancía la identación, se va a ejecutar todo lo que este identado después de la instruccion.

## Intrucciones complementarias

Para poder manipular mejor lo que hace el `while` podemos usar varias palabras clave.

`break` Detiene el ciclo incluso si la condición se sigue cumpliendo (que sea verdadera)

```python
while sorcerer in Domain:
    print("Nani!?")
    if DomainHaveFinish
        break
```

`continue` Puede parar la itereción en la que se encuentre y saltarse a la siguiente

```python
damage = 0
while sorcerer in Domain:
    damage += 10
    if damage < 100:
        continue
    print("Nani!?")
```

`else` Se usa para agregar un bloque de codigo que se ejecute una vez que la condicón deje de cumplirse.

```python
damage = 0
while sorcerer in Domain:
    damage += 10
    if damage < 100:
        continue
    print("Nani!?")
else:
    print("Use RCE")
```

> 📝 **Nota:** Si se usa `break` no pasara por lo que ejecute el `else`

## Ciclo anidado

Pon un ciclo dentro de otro!

```python
i, j = 10, 10
while i > 0:
    i -= 1
    while j > 0:
        j -= 1
```
