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
		self.logger.logear("Dia: " + str(self.dia))
		self.unSubSimDeExcavacion.simularExcavacion(self.dia)
		self.unSubSimDeExtraccion.simularExtraccion(self.dia)
		self.unSubSimDeReinyeccion.simularReinyeccion(self.dia)
		self.unSubSimDeConstruccion.simularConstruccion(self.dia)
		self.logger.logear("Fin del dia")

	def comenzarDia(self):
		self.dia += 1

sim = Simulador()
sim.pasarDeDia()