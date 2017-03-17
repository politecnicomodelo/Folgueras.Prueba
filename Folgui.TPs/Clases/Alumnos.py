from .Materia import materias

class alumno(object):

    nombre = " "
    apellido = " "
    FechaNaciemiento = None
    ListaNotasA = []
    ListaDeMaterias = []

    def ___init___(self):
        self.ListaDeMaterias = []


    def Nombre(self, Nombre):
        self.nombre = str(Nombre)

    def Apellido(self, Apellido):
        self.apellido = str(Apellido)

    def setFechaN(self, fecha):
        self.FechaNaciemiento = fecha

    def setMateria(self, Mate):
        nuevaMateria = materias()
        nuevaMateria.NombreM(Mate)
        self.ListaDeMaterias.append(Mate)

    def encontrarMateria(self, Mat):
        for item in self.ListaDeMaterias:
            if item.nombre == Mat:
                return item

    def agregarNotasM(self, mat, i):
        self.encontrarMateria(mat).ListaNotasA(i)

    def promMateria(self, n):
        return float(sum(self.encontrarMateria(n).ListaNotasA) / len(self.encontrarMateria(n).ListaNotasA))

    def promAlumno(self):
        a = 0
        for item in self.ListaDeMaterias:
            a += item.promMateria(item.nombre)
            return float(a/self.ListaDeMaterias)

    def menorYmayorProm(self):
        a = []
        for item in self.ListaDeMaterias:
            a.append(item.promMateria(item.nombre))
            return min(a), max(a)

    def agregarNota(self, h):
        self.ListaNotasA.append(h)

    def menor_nota(self):
        return min(self.ListaNotasA)

    def mayor_nota(self):
        return max(self.ListaNotasA)

    def prom(self):
        return sum(self.ListaNotasA) / len(self.ListaNotasA)

