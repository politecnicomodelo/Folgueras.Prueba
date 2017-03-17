class alumno(object):
    nombre = " "
    apellido = " "
    FechaNaciemiento = None
    ListaNotas = []
    def setNombre(self, Nombre):
        self.nombre = str (Nombre)

    def setApellido(self, Apellido):
        self.apellido = str (Apellido)

    def setFechaN(self, fecha):
        self.FechaNaciemiento = fecha

    def agregarNota(self, Nota):
        self.ListaNotas.append(Nota)

    def menorNota(self):
        return min(self.ListaNotas)

    def mayorNota(self):
        return max(self.ListaNotas)

    def promedioNota(self):
        return sum(self.ListaNotas) / len(self.ListaNotas)

