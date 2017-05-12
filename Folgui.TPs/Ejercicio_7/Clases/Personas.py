class Persona(object):

    def __init__(self, N = None, A = None):
        self.Nombre = str(N)
        self.Apellido = str(A)

    def getDescuento(self):
        return 0

    def Mod_Persona(self, N = None, A = None):
        if N:
            self.Nombre = N
        if A:
            self.Apellido = A

