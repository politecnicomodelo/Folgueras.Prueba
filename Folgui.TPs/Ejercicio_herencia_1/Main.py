
from clases.Camionetas import Camioneta
from clases.Autos import Auto
from clases.Empresas import Empresa
from datetime import date

Ranger = Camioneta("54 THJ 60",date(2017,6,10))
Audi = Auto("64 TJF 84",date(2017,8,20))

Ford = Empresa()
Ford.agregarCamioneta(Ranger)
Ford.agregarAuto(Audi)

print(Ford.Lista_Autos)


