
class Vehiculo(object):

    Patente = ""
    Cantidad_Ruedas = ""
    Año_Farbicacion = None

    def __init__(self, P, C, A):
        self.Patente = P
        self.Cantidad_Ruedas = C
        self.Año_Farbicacion = A

