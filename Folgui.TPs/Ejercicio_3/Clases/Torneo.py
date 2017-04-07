from .Partido import Partido

class Torneo(object):

    Nombre = ""
    contador1 = 0


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

    def hayPartido(self, e1, e2):
        for item in self.Lista_Partidos:
            if item.e1 == e1 and item.e2 == e2 or item.e1 == e2 and item.e2 == e1:
                return False
        return True

    def buscarDisp(self, e1, e2):
        for i in range(6):
            for j in range(3):
                if e1.Disp[i][j] and e2.Disp[i][j]:
                    return [i,j]
        return None

    def crearPartido(self):
        for e1 in self.Lista_Equipos:
            for e2 in self.Lista_Equipos:
                if e1 == e2:
                    continue
                if self.hayPartido(e1,e2):
                    continue
                diaTurno = self.buscarDisp(e1,e2)
                if diaTurno:
                    p = Partido()
                    p.Turno = diaTurno[1]
                    p.Dia = diaturno[0]
                    p.e1 = Equipo_1
                    p.e2 = Equipo_2
                    self.Lista_Partidos.append(p)


