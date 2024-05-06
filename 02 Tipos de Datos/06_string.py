"""
String
Autor: Carlos Nevárez - CubicNev
Fecha: 6-Mayo-2024

Manejo de String
"""

# Declarando variables como string
name = "Carlos"
nickname = str("Cubic")
print(name)
print(nickname)

# Concatenacion
user_name = name + nickname
print(user_name)

user_name = name + "_" + nickname
print(user_name)

# Casos especiales, alternando entre comilla simple y comilla doble
# quote = 'I'm Nicolas'
quoute = "I'm Nicolas"
print(quoute)

quoute2 = 'She said "Hello"'
print(quoute)

# Manipulación de formato (format), para darle estructura a nuestro texto
template = "Hola, mi nombre es " + name + " y mi nickname es " + nickname
print("v1:", template)

template = "Hola, mi nombre es {} y mi nickname es {}".format(name, nickname)
print('v2:', template)

template = f"Hola, mi nombre es {name} y mi nickname es {nickname}" # Es la más usada
print('v3:', template)

# Agregando un tercer dato
edad = 117
template = f"Hola, mi nombre es {name} y mi nickname es {nickname} y mi edad es {edad}"
print("v4", template)
