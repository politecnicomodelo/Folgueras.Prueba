
class Torneo(object):

    Nombre = ""


    def __init__(self):
        self.Lista_Equipos = []
        self.Lista_Partidos = []

    def Nombre_Torneo(self, N):
        self.Nombre = N

    def agregarEquipo(self, E):
        if E in self.Lista_Equipos:
            return False
        self.Lista_Equipos.append(E)
        return True