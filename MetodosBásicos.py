
# En Python, hay varias funciones y métodos similares a min que se utilizan para realizar operaciones específicas. Algunos de ellos incluyen:

# min(iterable, *[, key, default]): Devuelve el elemento más pequeño de un iterable o el menor de dos o más argumentos.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
min_number = min(numbers)
print(min_number)

# max(iterable, *[, key, default]): Devuelve el elemento más grande de un iterable o el mayor de dos o más argumentos.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
max_number = max(numbers)
print(max_number)


# sum(iterable, /, start=0): Devuelve la suma de todos los elementos en el iterable, con un valor inicial opcional.
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(total_sum)

# sorted(iterable, *, key=None, reverse=False): Devuelve una nueva lista ordenada a partir de los elementos del iterable.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# len(s): Devuelve la longitud de un objeto (número de elementos).
string = "Hello, World!"
length = len(string)
print(length)


# any(iterable): Devuelve True si al menos un elemento del iterable es verdadero.
values = [False, False, True, False]
result = any(values)
print(result)

# all(iterable): Devuelve True si todos los elementos del iterable son verdaderos.
values = [True, True, True, False]
result = all(values)
print(result)

# abs(x): Devuelve el valor absoluto de x.
number = -42
absolute_value = abs(number)
print(absolute_value)

# pow(x, y[, z]): Devuelve x elevado a la potencia y; si se proporciona z, devuelve x elevado a la potencia y, módulo z.
result = pow(2, 3)
print(result)

# round(number[, ndigits]): Devuelve el número flotante redondeado a ndigits después del punto decimal. Si ndigits se omite o es None, se redondea al número entero más cercano.
number = 3.14159
rounded_number = round(number, 2)
print(rounded_number)

# isinstance(object, classinfo): Devuelve True si el objeto es una instancia (o subclase) de la clase dada.
value = 42
result = isinstance(value, int)
print(result)

# range([start], stop[, step]): Devuelve una secuencia inmutable de números entre los valores de inicio y parada, con el paso especificado.
numbers = list(range(1, 10, 2))
print(numbers)

# enumerate(iterable, start=0): Devuelve un objeto enumerado que produce una tupla de un contador y un elemento del iterable.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip(*iterables): Combina elementos de varios iterables en tuplas hasta que se agote el más corto.
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 35, 40]
for name, age in zip(names, ages):
    print(name, age)


# count(value): Devuelve el número de veces que aparece el valor en la lista.
numbers = [1, 2, 3, 4, 2, 2, 3, 4, 5]
count_of_twos = numbers.count(2)
print(count_of_twos)


# set(iterable): Devuelve un nuevo conjunto que contiene elementos únicos del iterable.
numbers = [1, 2, 3, 4, 2, 3, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# La función get() se utiliza principalmente para acceder a elementos
# get(key[, default]): Devuelve el valor asociado con la clave dada en el diccionario.
student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 75}

# Acceder al valor asociado con la clave 'Bob'
bob_grade = student_grades.get('Bob')
print(bob_grade)  # Salida: 90

# Si la clave no existe, se devuelve el valor predeterminado (None si no se proporciona).
david_grade = student_grades.get('David')
print(david_grade)  # Salida: None

# También se puede proporcionar un valor predeterminado si la clave no existe.
david_grade_default = student_grades.get('David', 'No grade available')
print(david_grade_default)  # Salida: 'No grade available'

# hex(x): Devuelve la representación hexadecimal del número x.
number = 42
hexadecimal = hex(number)
print(hexadecimal) # Salida: '0x2a'

# oct(x): Devuelve la representación octal del número x.
number = 42
octal = oct(number)
print(octal) # Salida: '0o52'

# bin(x): Devuelve la representación binaria del número x.
number = 42
binary = bin(number)
print(binary) # Salida: '0b101010'
