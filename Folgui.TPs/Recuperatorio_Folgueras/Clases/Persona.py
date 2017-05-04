from .Familias import Familia

class Personas(object):

    Nombre = ""
    Fecha_N = None

    def __init__(self):
        self.Lista_Platos = []

    def setPersona(self, N, F):
        self.Nombre = N
        self.Fecha_N = F

    def agregarPlato(self, P):
        self.Lista_Platos.append(P)

    def TotalCalorias(self):
        Calorias = 0
        for item in self.Lista_Platos:
            Calorias += item.Cant_Calorias
        return Calorias
