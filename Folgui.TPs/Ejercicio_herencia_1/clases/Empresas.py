
class Empresa(object):

    def __init__(self):
        self.Lista_Camionetas = []
        self.Lista_Autos = []

    def agregarCamioneta(self, C):
        self.Lista_Camionetas.append(C)

    def agregarAuto(self, A):
        self.Lista_Autos.append(A)