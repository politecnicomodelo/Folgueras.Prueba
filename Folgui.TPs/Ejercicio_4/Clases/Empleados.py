from datetime import date

class Empleado (object):

    Nombre = ""
    Apellido = ""
    Fecha_N = None
    Telefono = ""


    def __init__(self):
        self.Lista_Asist = []
        self.Disponibilidad = []

    def setEmpleado(self, N, A, T, F):
        self.Nombre = N
        self.Apellido = A
        self.Telefono = T
        self.Fecha_N = F

    def Asistencias(self, date):
        self.Lista_Asist.append(date)

    def Disp(self, D):
        self.Disponibilidad = D

    def cant_Asist(self, mes, año):
        g = 0
        h = 0
        for item in self.Lista_Asist:
            if item.month == mes and item.year == año:
                g += 1

        for item2 in self.Disponibilidad:
            if item2:
                h += 1

        return g*100/h*4

