from .Personas import Persona

class Alumno(Persona):

    def __init__(self, N = None, A = None, D = None, dni = None):
        Persona.__init__(self, N, A)
        self.Division = D
        self.DNI = dni

    def ModAlumno(self, N = None, A = None, D = None, dni = None):
        Persona.ModAlumno(N, A)
        if D:
            self.Division = D
        if dni:
            self.DNI = dni
