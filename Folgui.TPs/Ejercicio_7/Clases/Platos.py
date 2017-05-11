
class Platillos(object):

    def __init__(self, N = None, P = None):
        self.Nombre = N
        self.Precio = P

    def Mod_Platillos(self, N = None, P = None):
        if N:
            self.Nombre = N
        if P:
            self.Precio = P