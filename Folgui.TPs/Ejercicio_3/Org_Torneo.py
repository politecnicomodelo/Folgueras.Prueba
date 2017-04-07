from datetime import date
from Clases.Equipos import Equipo
from Clases.jugadores import jugador
from Clases.Partido import Partido
from Clases.Torneo import Torneo

Jugador1 = jugador()
Jugador2 = jugador()
Jugador3 = jugador()
Jugador4 = jugador()
Jugador5 = jugador()
Jugador6 = jugador()


Equipo1 = Equipo()
Equipo2 = Equipo()

Torneo = Torneo()

Partidos = Partido()

#--------------------------------------------------------------- EQUIPO 1


Jugador1.setNombre("Roberto")
Jugador1.setFecha_Nac(date(1992,7,12))
Jugador1.NroCamiseta("11")

Jugador2.setNombre("Rodrigo")
Jugador2.setFecha_Nac(date(1991,7,23))
Jugador2.NroCamiseta("1")

Jugador3.setNombre("Federico")
Jugador3.setFecha_Nac(date(1996,7,13))
Jugador3.NroCamiseta("9")

Equipo1.setNombre("Los Negroh")
Equipo1.setBarrio("Floresta")
Equipo1.agregarJugador(Jugador1)
Equipo1.agregarJugador(Jugador2)
Equipo1.agregarJugador(Jugador3)
Equipo1.Capitan_E(Jugador3)
Equipo1.setTurno(2,1,True)
Equipo1.setTurno(1,1,True)
Equipo1.setTurno(0,1,True)

#--------------------------------------------------------------- EQUIPO 2

Jugador4.setNombre("Rodriguez")
Jugador4.setFecha_Nac(date(1996,7,10))
Jugador4.NroCamiseta("11")

Jugador5.setNombre("Ricardo")
Jugador5.setFecha_Nac(date(1997,7,9))
Jugador5.NroCamiseta("3")

Jugador6.setNombre("Ruben")
Jugador6.setFecha_Nac(date(1993,7,8))
Jugador6.NroCamiseta("2")

Equipo2.setNombre("Gran R")
Equipo2.setBarrio("Floresta")
Equipo2.agregarJugador(Jugador4)
Equipo2.agregarJugador(Jugador5)
Equipo2.agregarJugador(Jugador6)
Equipo2.Capitan_E(Jugador6)
Equipo2.setTurno(5,1,True)
Equipo2.setTurno(0,1,True)
Equipo2.setTurno(3,1,True)

#----------------------------------------------------------------- GRAN TORNEO


Torneo.Nombre_Torneo("ElGranTorneo")
Torneo.agregarEquipo(Equipo1)
Torneo.agregarEquipo(Equipo2)

#----------------------------------------------------------------- PARTIDO

Partidos.Dia_P(date(2017,8,10))
Partidos.setTurno(0,1,True)
Partidos.Equipo1 = Equipo1
Partidos.Equipo2 = Equipo2

#----------------------------------------------------------------- MOSTRAR

print(Torneo.Nombre)
print("Equipos: ")
print(Equipo1.Nombre,"y",Equipo2.Nombre)
print("Del Barrio:")
print(Equipo1.Barrio)
print("Horario:")
print(Partidos.Turno)