
class Empresa(object):

    Nombre = ""

    def __init__(self):
        self.Lista_Empleados = []

    def agregarEmpleado(self, E):
        self.Lista_Empleados.append(E)

    def porcentajeAsistencia(self, month, year):
        a = 0
        for item in self.Lista_Empleados:
            a += item.porcentajeAsistencia(month, year)
        return a/len(self.Lista_Empleados)
