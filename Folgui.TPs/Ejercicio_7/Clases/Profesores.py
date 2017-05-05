from .Personas import Persona

class Profesor(Persona):

    def __init__(self, N, A):
        Persona.__init__(self, N,A)
        self.Porcentaje_Descuento = 30

    def mod_Profesor(self, P = None, N = None, A = None):
        Persona.mod_Profesor(N, A)
        if P:
            self.Porcentaje_Descuento = P
