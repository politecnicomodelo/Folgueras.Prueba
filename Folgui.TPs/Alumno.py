from Clases.Alumnos import alumno
from datetime import date

a = alumno()
a.setNombre = "Pepito"
a.setApellido = "Lawea"
a.setFechaN = (date(2017,3,4))
a.agregarNota (10)
a.agregarNota (8)
a.agregarNota (4)
a.agregarNota (7)
print (a.promedioNota())


