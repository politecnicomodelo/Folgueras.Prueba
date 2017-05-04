class Familia(object):

    def __init__(self):
        self.ListaPersonas = []
        self.Calorias = []

    def Agregar_P(self, P):
        self.ListaPersonas.append(P)

    def Promedio_Familia(self, Persona):
        c = 0
        Total = 0
        for item2 in self.ListaPersonas:
            if item2 == Persona:
                for item in item2.Lista_Platos:
                    c += item.Cant_Calorias
                    self.Calorias.append(c)
                for item3 in self.Calorias:
                    Total += item3
        return Total

    def Consumio_Mas(self, Persona):
        Calorias = 0
        Mayor = 0
        for item2 in self.ListaPersonas:
            if item2 == Persona:
                for item in item2.Lista_Platos:
                    Calorias += item.Cant_Calorias
                if Calorias > Mayor:
                    Mayor = Calorias
        return Mayor

    def Consumio_Menos(self, Persona):
        Calorias = 0
        Menor = 0
        for item2 in self.ListaPersonas:
            if item2 == Persona:
                for item in item2.Lista_Platos:
                    Calorias += item.Cant_Calorias
                Calorias = Menor
                if Calorias < Menor:
                    Menor = Calorias
        return Menor