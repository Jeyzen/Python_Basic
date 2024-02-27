# Ejercicio:
# El ejercicio consiste en imprimir todas las posibles permutaciones de un string dado de tamaño específico en orden lexicográfico.
# Entrada:
# Se recibe una línea de entrada que contiene el string y un valor entero separados por un espacio.
# Salida:
# Se debe imprimir en líneas separadas todas las permutaciones del string de tamaño especificado, ordenadas lexicográficamente.
# Restricciones:
# El string contiene solo letras en mayúsculas.
# Ahora, veamos el código en Python explicado línea por línea:


from itertools import permutations

# Definimos una función llamada 'print_permutations'
def print_permutations(string, size):
    # Generamos todas las permutaciones del string de tamaño 'size'
    perms = permutations(string, size)
    
    # Ordenamos las permutaciones lexicográficamente y las imprimimos
    for perm in sorted(perms):
        print(''.join(perm))

# Pedimos la entrada al usuario
input_line = input("Ingresa el string y el valor entero separados por un espacio: ")
string, size = input_line.split()
size = int(size)

# Llamamos a la función con los argumentos proporcionados
print_permutations(string, size)

# from itertools import permutations: Importa la función permutations del módulo itertools, que se utiliza para generar todas las permutaciones posibles de una secuencia.
# def print_permutations(string, size):: Define una función llamada print_permutations que toma dos argumentos: string (el string original) y size (el tamaño de las permutaciones que queremos).
# perms = permutations(string, size): Genera todas las permutaciones posibles del string de tamaño especificado y las almacena en la variable perms.
# for perm in sorted(perms):: Itera sobre las permutaciones ordenadas lexicográficamente.
# print(''.join(perm)): Imprime cada permutación, uniendo los caracteres en un string antes de imprimirlo. Esto se hace utilizando el método join de strings.
# input_line = input("Ingresa el string y el valor entero separados por un espacio: "): Solicita al usuario ingresar el string y el valor entero separados por un espacio.
# string, size = input_line.split(): Divide la entrada en dos partes y asigna cada parte a las variables string y size.
# size = int(size): Convierte la variable size a un entero, ya que la entrada se toma como una cadena de caracteres.
# print_permutations(string, size): Llama a la función print_permutations con los argumentos proporcionados por el usuario.