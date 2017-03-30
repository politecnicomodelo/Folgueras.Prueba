
class Torneo(object):

    def __init__(self):
        self.Lista_Equipos = []
        self.Lista_Partidos = []

    def agregarEquipo(self, E):
        self.Lista_Equipos.append(E)