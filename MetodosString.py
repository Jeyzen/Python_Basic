# capitalize(): Convierte la primera letra de la cadena en mayúscula.
s = "hola mundo"
print(f'{s.capitalize() =}')  # Output: "Hola mundo" (s.capitalize())  # Output: "Hola mundo"

# upper(): Convierte todas las letras de la cadena en mayúsculas.
s = "hola mundo"
print(f'{s.upper() =}')  # Output: "HOLA MUNDO" (s.upper())  # Output: "HOLA MUNDO"

# lower(): Convierte todas las letras de la cadena en minúsculas.
s = "HOLA MUNDO"
print(f'{s.lower() =}')  # Output: "hola mundo" (s.lower())  # Output: "hola mundo"

# title(): Convierte la primera letra de cada palabra en mayúscula.
s = "hola mundo"
print(f'{s.title() =}')  # Output: "Hola Mundo" (s.title())  # Output: "Hola Mundo"

# swapcase(): Convierte las mayúsculas en minúsculas y viceversa.
s = "HOLA MUNDO"
print(f'{s.swapcase() =}')  # Output: "hola mundo" (s.swapcase())  # Output: "hola mundo"

# count(): Cuenta el número de veces que aparece una subcadena en una cadena.
s = "hola mundo"
print(f'{s.count("o") =}')  # Output: 2 (s.count("o"))  # Output: 2

# startswith(): Verifica si una cadena comienza con una subcadena.
s = "hola mundo"
print(f'{s.startswith("hola") =}')  # Output: True (s.startswith("hola"))  # Output: True

# endswith(): Verifica si una cadena termina con una subcadena.
s = "hola mundo"
print(f'{s.endswith("mundo") =}')  # Output: True (s.endswith("mundo"))  # Output: True

# find(): Encuentra la primera ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.find("mundo") =}')  # Output: 6 (s.find("mundo"))  # Output: 6

# rfind(): Encuentra la último ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.rfind("mundo") =}')  # Output: 6 (s.rfind("mundo"))  # Output: 6

# index(): Encuentra la primera ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.index("mundo") =}')  # Output: 6 (s.index("mundo"))  # Output: 6

# rindex(): Encuentra la último ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.rindex("mundo") =}')  # Output: 6 (s.rindex("mundo"))  # Output: 6