input_string = 'Hola'

result_list = []  # Se crea una lista vacía llamada result_list para almacenar los pares de caracteres.
for i in range(0, len(input_string), 2):  # Se utiliza un bucle for para iterar sobre el string con pasos de 2.
    result_list.append(input_string[i:i+2])  # Se toma un segmento de 2 caracteres y se agrega a result_list.
print(result_list)  # Se imprime la lista resultante.


print(result_list)

# OTRA VERSION DONDE AGREGA EL UNDERSCORE
def solution(s):
    if len(s) % 2 != 0: # SI LA LONGITUD DEL STRING ES IMPAR, AGREGA UN UNDERSCORE AL FINAL
        s += '_' # AGREGA UN UNDERSCORE AL FINAL

    pairs = [s[i:i+2] for i in range(0, len(s), 2)] # CREA UNA LISTA CON LOS PARES DE CARACTERES
    
    return pairs


# VERSION ALTERA SIN COMPRENSION DE LISTAS
def Solution(s):
    result = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        result.append(pair)


# result_list = []: Se crea una lista vacía llamada result_list que se utilizará para almacenar los pares de caracteres.

# for i in range(0, len(input_string), 2):: Se inicia un bucle for que recorre el string input_string desde el índice 0 
#hasta la longitud del string, avanzando de 2 en 2 (gracias al tercer argumento de range(0, len(input_string), 2)).

# i toma valores 0, 2, 4, etc., correspondientes a los índices de los caracteres en input_string.
# result_list.append(input_string[i:i+2]): Dentro del bucle, se toma un segmento de 2 caracteres de input_string utilizando la notación de segmentación [i:i+2], 
#donde i es el índice de inicio y i+2 es el índice de fin (no inclusivo). Este segmento se agrega a la lista result_list usando el método append.

# Por ejemplo, si i es 0, entonces input_string[0:2] tomará los caracteres en las posiciones 0 y 1.
# print(result_list): Después de que el bucle se ha ejecutado, la lista result_list contiene todos los pares de caracteres, y se imprime para mostrar el resultado.