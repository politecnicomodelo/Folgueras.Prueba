
class Pedido(object):

    def __init__(self, F, H, E, Plato):
        self.Fecha_Creacion = F
        self.Hora_Entrega = H
        self.Entregado = E
        self.Plato = Plato

    def Mod_Pedidos(self, F = None, H = None, E = None):
        if F:
            self.Fecha_Creacion = F
        if H:
            self.Hora_Entrega = H
        if E:
            self.Entregado = E

    def CalcularPrecio(self):
        return (100-(self.Persona.getDescuento()))/100*self.Platillos.Precio



