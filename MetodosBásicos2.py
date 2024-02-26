# Ejemplo de diferentes usos de funciones en Python

# Función sorted: Ordena una lista de números
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = sorted(original_list)
print("1. Sorted:")
print("Original list:", original_list)
print("Sorted list:", sorted_list)
print()

# Función split: Divide una cadena en una lista de palabras
sentence = "Hola, ¿cómo estás?"
words = sentence.split(" ")
print("2. Split:")
print("Original sentence:", sentence)
print("Words:", words)
print()

# Función join: Une las palabras de una lista en una cadena
words = ['Hola,', '¿cómo', 'estás?']
joined_sentence = " ".join(words)
print("3. Join:")
print("Words:", words)
print("Joined sentence:", joined_sentence)
print()

# Función reverse: Invierte el orden de los elementos de una lista
original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print("4. Reverse:")
print("Original lists:", original_list)

print()

# Función pop: Elimina y devuelve el último elemento de una lista
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)
print("5. Pop:")
print("Popped element:", popped_element)
print("Updated list:", my_list)