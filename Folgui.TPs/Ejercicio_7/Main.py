from Clases.Pedidos import Pedido
from Clases.Platos import Platillos
from Clases.Alumnos import Alumno
from Clases.Profesores import Profesor

Profesores = []
Alumnos = []
Platos = []
Pedidos = []


def agregarAlumno():

    A = Alumno()

    print("Nombre del Alumno")

    A.Nombre = input()

    print("Apellido del Alumno")

    A.Apellido = input()

    print("Division")

    A.Division = input()

    print("DNI")

    A.DNI = input()

    Alumnos.append(A)


def abrirAlumnos():

    ArchivoAlumnos = open("arch.txt", "w")
    for item in Alumnos:
        ArchivoAlumnos.write(item.Nombre + " " + item.Apellido + " | " + item.Division + " | " + item.DNI + '\n')
    ArchivoAlumnos.close()


def BorrarAlumno():

    print("Ingrese el DNI del alumno a borrar")
    DNI = input()
    for item in Alumnos:
        if item.DNI == DNI:
            Alumnos.remove(item)
    print("Alumno Borrado")


def agregarProfesor():

    P = Profesor()

    print("Nombre del Alumno")

    P.Nombre = input()

    print("Apellido del Alumno")

    P.Apellido = input()

    Profesores.append(P)


def abrirProfesores():

    ArchivoProfesores = open("archPr.txt", "w")
    for item in Profesores:
        ArchivoProfesores.write(item.Nombre + " " + item.Apellido + '\n')
    ArchivoProfesores.close()


def BorrarProfesor():

    print("Ingrese el Nombre del Profesor a borrar")
    Nombre = input()
    for item in Profesores:
        if item.Nombre == Nombre:
            Profesores.remove(item)
    print("Profesor Borrado")


def agregarPlato():

    Plato = Platillos()

    print("Nombre del Plato")

    Plato.Nombre = input()

    print("Precio del Plato")

    Plato.Precio = input()

    Platos.append(Plato)


def abrirPlatos():

    ArchivoPlatos = open("archPla.txt", "w")
    for item in Platos:
        ArchivoPlatos.write(item.Nombre + ' | ' + item.Precio + '\n')
    ArchivoPlatos.close()


def BorrarPlatos():

    print("Ingrese el Nombre del Plato a borrar")
    Nombre = input()
    for item in Platos:
        if item.Nombre == Nombre:
            Platos.remove(item)
    print("Plato Borrado")


def CrearPedido():
    P = Pedido()

    print("Nombre del Plato")

    P.Plato = input()

    i = 0

    while i == 0:
        for item in Platos:
            if item.Nombre == P.Plato:
                Pedidos.append(P)
                i = 2
            else:
                print("Ingrese el nombre de un Plato existente")
                P.Nombre = input()


    print("Hora de entrega del pedido")

    P.Hora_Entrega = input()

    print("Fecha de Creacion")

    P.Fecha_Creacion = input()

    print("Persona que lo pidio")

    P.Entregado = input()

    PrecioPedido()

def PrecioPedido():
    a = 0
    for item in Pedidos:
        a += item.Precio
    Desc = (30*a)/100
    return a - Desc




Pizza = Platillos("PIZZA","110")
Platos.append(Pizza)
Prusci = Profesor("Prusci","SteMen")
Profesores.append(Prusci)
Chuaman = Alumno("Judi","Judio","5to","658423149")
Alumnos.append(Chuaman)

#-----------------------MENU--------------------------------------------#

def menu():
    while True:
        print('Menu')
        print('1)Agregar Alumno')
        print('2)Modificar Alumno')
        print('3)Borrar Alumnos')
        print('4)Agregar Profesor')
        print('5)Modificar Profesor')
        print('6)Borrar Profesor')
        print('7)Agregar Plato')
        print('8)Modificar Plato')
        print('9)Borrar Plato')
        print('10)Crear Pedido')
        print('11)Modificar Pedido')
        print('12)Borrar Pedido')
        print('Salir')
        Elegir = input()

        if Elegir == "1":

            agregarAlumno()

            abrirAlumnos()

        if Elegir == "3":
            BorrarAlumno()

        if Elegir == "4":
            agregarProfesor()

            abrirProfesores()

        if Elegir == "6":
            BorrarProfesor()

        if Elegir == "7":

            agregarPlato()

            abrirPlatos()

        if Elegir == "9":
            BorrarPlatos()

        if Elegir == "10":
            CrearPedido()

        if Elegir == "Salir":
            break

menu()
