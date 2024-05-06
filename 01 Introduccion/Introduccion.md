# Introducción

---

## ¿Porqué aprender Pyhton?

- Es de los lenguajes mas queridos, ocupo el 4to lugar, con el 43% de los votos en el [Stack Overflow Developer Survey 2021](https://survey.stackoverflow.co/2021) donde tuvo 34,155 de 71,547 votos.

- Es facil de aprender, su curva de aprendizaje no es tan pronunciada.

- Es de los lenguajes mejor pagados, esta en el top 20 con $71,105 USD al año.

- Areas dónde se usa python. [The State of Developer Ecosystem 2021](https://www.jetbrains.com/lp/devecosystem-2021/)
  - 51% Analisis de datos
  - 45% Web development
  - 40% Machine learnig
  - 36% DevOps
  - ... entre otros

- Tiene alta demanda laboral.

---

## Herramientas del curso (opcional)

**Replit:** Herramienta para programar desde navegador.
Crear un entorno de trabajo para trabajar con python.

---

## Primer programa

Todos los programas de Python tienen la extensión **.py**, también hay otros archivos que se encargan de administrar las dependencias, pero esos se verán después.

Tú escribes el código, la computadora lo **interpreta** y una forma de ver el resultado es por medio de la consola.

La primera función a usar será **print()** para imprimir un mensaje en la pantalla:

```python
print('Hola Mundo!')
```

Dentro de la función pueden ir desde cadenas, hasta calculos.

Otro aspecto importante a tomar en cuenta cuando se trabaja en Python es la **identación**. Por ahora no se debe tener ningun espacio o identación al inicio de la línea.

Los **comentarios** son partes que el programa ignora y no ejecuta, los toma como lo que son, comentarios sin más. Se pueden poner de dos formas:

1. Con el **hashtag(#)** que sirve para marcar una línea como comentario.

2. Con **comillas triples (''' o """)** para marcar un bloque de comentario, que conforma varias lineas.

Comunmente se usan para describir el codigo como buenas practicas, y así tu equipo de trabajo sabrá las funciones y objetivo del programa.

---

## Ejecucion en consola

Para ejecutar un archivo de python especifico en consola basta con escribir el comando `python` o `python3` seguido de el nombre del arcchivo a ejecutar con todo y extensión:

```shell
python script.py
```

***Nota:*** Replit corre el archivo `main.py` cuando se le da a `Run`, si se quiere correr otro archivo se debe hacer desde consola.

---

## Variables

Imagina que una variable es una caja con una etiqueta. Abstrayendo un poco puedes meter cosas en esta caja, como: zapatos, muebles, o [iguanodones anátomicamente inexacto](https://es.wikipedia.org/wiki/Iguanodon#/media/Archivo:Goodrich_Iguanodon.jpg). Respectivamente para facilidad puedes etiquetar las cajas para identificarlas.

La variables tienen un nombre y almacenan información. Son contenedores para almacenar datos.

### Creacion de variables

En Python no es necesario escribir el tipo de dato que se va a usar como en otros lenguajes, una variable es creada en el momento que se le asigna un valor. Es decir al escribir su "identificador" seguido de un valor se crea una variable.

```python
variable_x = "Hola Mundo!"
print(variable_x)
```

De la misma forma se puede cambiar su valor.
```python
variable_x = "Bye bye"
print("Nuevo valor:", variable_x)
```
Tambien se pueden ingresar datos desde el teclado usando la función `input`
```python
variable_x = input("Ingresa un mensaje: ")
print("Nuevo valor:", variable_x)
```
Como las variables no necesitan ser declaradas con un `tipo` en especifico, se puede hacer un cambio despues de crearla.
```python
uwu = 4 # uwu es de tipo int
uwu = "Hola" # uwu es de tipo str
print(uwu)
```

### Nombrandovariables

El nombre de una variable puede ser algo corto (como x o y), o mas descriptivo y largo (volumen_total, nombre, catalogo_proyectos). Se siguen las siguientes reglas:
* Empezar con una letra o un guion bajo.
* No puede empezar con un número.
* Solo puede tener caráctere alfa-númericos y guiones bajos.
* Las variables con sensibles a las mayúsculas.
* No pueden se palabras clave de Python.

Es importante saber que las variables son ***Sensibles a las mayúsculas***, es decir, las variables "A1" y "a1" no son las mimas:
```python
a1 = 0
A1 = "Aun no"
# A1 no sobrescribe a a1
```
