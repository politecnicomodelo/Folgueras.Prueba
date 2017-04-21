from .Vehiculos import Vehiculo

class Auto(Vehiculo):

    Descapotable = False

    def __init__(self, P, A):
        Vehiculo.__init__(self,P,4,A)

    def EsDescapotable(self, D):
        self.Descapotable = D
