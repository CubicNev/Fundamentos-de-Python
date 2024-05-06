"""
Tipos de datos
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Se ven los principales tipos de datos de Python
"""

# string (cadenas de texto, puede usarse comillas dobles o comillas simples)
name = "Juan"
name = 'Carlos'
print('name =>',name)
print(type(name)) # Imprimir el tipo de dato

# int (Entero)
age = 12
print('age =>', age)
print(type(age))

# boolean (Solo usan True o False)
is_single = True
print('is single =>', is_single)
print(type(is_single))

# inputs
age = input('¿Cuál es tu edad? R:')
print('age =>', age)
print(type(age)) # Despliega que es de tipo String ya que se uso input


