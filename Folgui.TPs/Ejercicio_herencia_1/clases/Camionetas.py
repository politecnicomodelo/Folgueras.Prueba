from .Vehiculos import Vehiculo

class Camioneta(Vehiculo):

    Capacidad_Carga = ""

    def __init__(self, P, A):
        Vehiculo.__init__(self,P,4,A)

    def setCapacidad(self, C):
        self.Capacidad_Carga = C