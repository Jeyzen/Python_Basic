# capitalize(): Convierte la primera letra de la cadena en mayúscula.
s = "hola mundo"
print(f'{s.capitalize() = }')   # Output: "Hola mundo"

# casefold(): Convierte todas las letras de la cadena en minúsculas.
s = "Hola Mundo"
print(f'{s.casefold() = }') # Output: "hola mundo"

# upper(): Convierte todas las letras de la cadena en mayúsculas.
s = "hola mundo"
print(f'{s.upper() = }')  # Output: "HOLA MUNDO"

# lower(): Convierte todas las letras de la cadena en minúsculas.
s = "HOLA MUNDO"
print(f'{s.lower() = }')  # Output: "hola mundo"

# title(): Convierte la primera letra de cada palabra en mayúscula.
s = "hola mundo"
print(f'{s.title() = }')  # Output: "Hola Mundo"

# swapcase(): Convierte las mayúsculas en minúsculas y viceversa.
s = "HOLA MUNDO"
print(f'{s.swapcase() = }')  # Output: "hola mundo"

# count(): Cuenta el número de veces que aparece una subcadena en una cadena.
s = "hola mundo"
print(f'{s.count("o") = }')  # Output: 2

# startswith(): Verifica si una cadena comienza con una subcadena.
s = "hola mundo"
print(f'{s.startswith("hola") = }')  # Output: True

# endswith(): Verifica si una cadena termina con una subcadena.
s = "hola mundo"
print(f'{s.endswith("mundo") = }')  # Output: True

# find(): Encuentra la primera ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.find("mundo") = }')  # Output: 5

# rfind(): Encuentra la último ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.rfind("mundo") = }')  # Output: 5

# index(): Encuentra la primera ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.index("mundo") = }')  # Output: 5

# rindex(): Encuentra la último ocurrencia de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.rindex("mundo") = }')  # Output: 5

# replace(): Reemplaza todas las ocurrencias de una subcadena en una cadena.
s = "hola mundo"
print(f'{s.replace("mundo", "python") = }')  # Output: "hola python"

# strip(): Elimina los espacios al principio y al final de una cadena.
s = "   Hola Mundo!   "
print(f'{s.strip() = }')  # Output: "Hola Mundo!"