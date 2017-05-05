from .Personas import Persona

class Alumno(Persona):

    def __init__(self, N, A, D):
        Persona.__init__(self, N, A)
        self.Division = D

    def ModAlumno(self, N = None, A = None, D = None):
        Persona.ModAlumno(N, A)
        if D:
            self.Division = D