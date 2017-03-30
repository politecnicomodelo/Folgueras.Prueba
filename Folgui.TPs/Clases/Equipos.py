

class Equipo(object):

    Nombre = ""
    Barrio = ""
    Disponibilidad =
    capitan = ""

    def __init__(self):
        self.Lista_Jugadores = []

    def Nombre(self, Nom):
        self.Nombre = Nom

    def Barrio(self, B):
        self.Barrio = B

    def Capitan(self, Cap):
        self.Capitan = Cap

    def agregarJugador(self, J):
        self.Lista_Jugadores.append(J)