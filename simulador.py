from subSimDeExcavacion import *
from subSimDeExtraccion import *
from subSimDeConstruccion import *
from subSimDeReinyeccion import *
from logger import Logger

class Simulador:
	def __init__(self):
		parcelas = []
		self.logger = Logger("log.txt")
		self.dia = 0
		self.unSubSimDeExcavacion = SubSimDeExcavacion(self.logger, politicaDeSeleccionMenorProfundidad(3),politicaCuandoPerforarParcelasTodasAlPrincipio(), parcelas)
		self.unSubSimDeExtraccion = SubSimDeExtraccion(self.logger)
		self.unSubSimDeReinyeccion = SubSimDeReinyeccion(self.logger)
		self.unSubSimDeConstruccion = SubSimDeConstruccion(self.logger)

	def pasarDeDia(self):
		self.comenzarDia()
		eventos = []
		eventoComienzoDelDia = Evento(0,"Comienzo del dia " + str(self.dia))
		eventos.append(eventoComienzoDelDia)
		eventosDeExcavacion = self.unSubSimDeExcavacion.simularExcavacion(self.dia)
		eventosDeExtraccion = self.unSubSimDeExtraccion.simularExtraccion(self.dia)
		eventosDeReinyeccion = self.unSubSimDeReinyeccion.simularReinyeccion(self.dia)
		eventosDeConstruccion = self.unSubSimDeConstruccion.simularConstruccion(self.dia)
		eventos = eventos + eventosDeExcavacion + eventosDeExtraccion + eventosDeReinyeccion + eventosDeConstruccion
		eventoFinDelDia = Evento(0,"Fin del dia " + str(self.dia))
		eventos.append(eventoFinDelDia)
		self.logger.logearEventos(eventos)

	def comenzarDia(self):
		self.dia += 1

sim = Simulador()
sim.pasarDeDia()