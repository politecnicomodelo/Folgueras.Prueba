

class Partido (object):


    Dia = None
    Equipo_1 = ""
    Equipo_2 = ""


    def __init__(self):
        self.Turno = [[False, False, False],[False, False, False],
                      [False, False, False],[False, False, False],
                      [False, False, False],[False, False, False]]

    def setTurno(self, Dia, Tiempo, Activo):
        self.Turno[Dia][Tiempo] = Activo

    def Dia_P(self, P):
        self.Dia = P

    def Equipo1(self, E1):
        self.Equipo_1 = E1

    def Equipo2(self, E2):
        self.Equipo_2 = E2