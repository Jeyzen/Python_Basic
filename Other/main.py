class Cliente(Persona): #Define el parametro para llamar al archivo padre
    def __init__(self, nombre, apellido, dni, telefono, categoria):  # declara los parametros nuevos
        super().__init__(nombre, apellido, dni, telefono)  # llama los datos de la clase padre
        self.categoria = categoria  # declara la nueva variable

class Empleado(Persona):    
    def __init__(self, nombre, apellido, dni, telefono, sueldo): 
        super().__init__(nombre, apellido, dni, telefono)  
        self.sueldo = sueldo  

class Persona:  # Define el nombre de la clase
    def __init__(self, nombre, apellido, dni, telefono):  # agrega los parametros
        self.nombre = nombre  # crea una variable y agrega valor
        self.apellido = apellido  # la variable self no es igual al parametro de la función
        self.dni = dni
        self.telefono = telefono

    def __str__(self):  #retorna el valor en string y hereda a las demas clases
        return self.nombre + " " + self.apellido + " - " + self.dni + " - " + str(self.sueldo)

personas = []  # define un arreglo vacio

def cargar():
    while True:
        opcion = str(input("¿Empleado o Cliente?: "))  # ingresa a la condicional if

        if opcion == "empleado":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            telefono = input("Telefono: ")
            sueldo = input("Ingrese sueldo: ")  # define nueva varible unica
            emp = Empleado(nombre, apellido, dni, telefono, int(sueldo))
            personas.append(emp)  # llama el array y guarda variable emp
        elif opcion == "cliente":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            telefono = input("Telefono: ")
            categoria = input("Ingrese categoria: ")
            cli = Cliente(nombre, apellido, dni, telefono, categoria)
            personas.append(cli)
        elif opcion =="show":
            for persona in personas:
                print(persona)
        else:
            break




for persona in personas:  #for que declara variable persona con datos del array personas
    print(personas) #imprime en orden los datos almacenados en el array
    pause = input("Teclea para continuar...")



cargar()
