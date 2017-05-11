from Clases.Pedidos import Pedido
from Clases.Platos import Platillos
from Clases.Alumnos import Alumno
from Clases.Profesores import Profesor

Profesores = []
Alumnos = []
Platos = []
Personas = []

Pizza = Platillos("PIZZA","110")
Platos.append(Pizza)
Prusci = Profesor("Prusci","SteMen")
Profesores.append(Prusci)
Chuaman = Alumno("Judi","Judio","5to")
Alumnos.append(Chuaman)
Personas.append(Profesores)
Personas.append(Alumnos)

#-----------------------MENU--------------------------------------------#

print('Menu')
print('1)Agregar Alumno')
print('2)Agregar Profesor')
print('3)Agregar Plato')
Elegir = input()

#-----------------------1------------------------------------------#

if Elegir == 1:

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

ArchivoAlumnos = open("arch.txt", "w")

for item in Alumnos:
    ArchivoAlumnos.write(item.Nombre + '|' + item.Apellido + '|' + item.Division + '|' + item.DNI)
ArchivoAlumnos.close()

#------------------------------2-------------------------------#

if Elegir == 2:

    P = Profesor()

    print("Nombre del Alumno")

    P.Nombre = input()

    print("Apellido del Alumno")

    P.Apellido = input()

    Profesores.append(P)

ArchivoProfesores = open("archPr.txt", "w")

for item in Profesores:
    ArchivoAlumnos.write(item.Nombre + '|' + item.Apellido)
ArchivoProfesores.close()

#----------------------------3------------------------------------#

if Elegir == 3:

    Plato = Platillos()

    print("Nombre del Plato")

    Plato.Nombre = input()

    print("Precio del Plato")

    Plato.Precio = input()