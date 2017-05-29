from subSimDeExcavacion import *
from subSimDeExtraccion import *
from subSimDeConstruccion import *
from subSimDeReinyeccion import *
from logger import Logger
from evento import *
from calculadorDeGanancia import *

class Simulador:
	def __init__(self,rigs,parcelas,politicaDeEleccionDePozos,politicaCuandoPerforar,politicaCualYCantidaddePozosParcela,politicaEleccionRigs,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDeTanques, constructorDePlantas,politicaDeFinalizacion,politicaDeReinyeccion):
		# yacimiento = (
		# parcelas = [Listdo de Parcelas] [ [Arcilloso, 20, 20], [Roca, 10, 15], [Roca, 1, 10] ]
		# politicaCuandoPerforar: Todas al Principio
		# politicaCualYCantidadDePozosParcela: De Menor Profundidad: cantidadDePozos (int)
		# politicaEleccionRigs: Random
		# politicaDeConsutrccionTanques: Todas al Principio parametro: cantidad a construir (int)
		# politicaDeConstruccionDePlantas : Todas al principio: cantidad a construir (int)

		self.parcelas = parcelas
		self.logger = Logger("log.txt")
		self.dia = 0
		self.unSubSimDeExcavacion = SubSimDeExcavacion(politicaEleccionRigs,politicaCualYCantidaddePozosParcela,politicaCuandoPerforar,rigs,parcelas)
		self.unSubSimDeExtraccion = SubSimDeExtraccion(parcelas,politicaDeEleccionDePozos)
		self.unSubSimDeReinyeccion = SubSimDeReinyeccion(politicaDeReinyeccion)
		self.unSubSimDeConstruccion = SubSimDeConstruccion(politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDePlantas, constructorDeTanques)
		self.politicaDeFinalizacion = politicaDeFinalizacion
		self.politicaDeReinyeccion = politicaDeReinyeccion
		self.eventos = []
		self.calculador = CalculadorDeGanancia()

	def start(self):
		while not self.politicaDeFinalizacion.finalizo(self.dia):
			self.pasarDeDia()
		return self.calculador.calcular(self.eventos)

	def filtrarConPozo(self,parcela):
		return parcela.listoParaExtraer()

	def filtrarParcelas(self,funcionParaFiltrar):
		return list(filter(funcionParaFiltrar,self.parcelas))

	def pasarDeDia(self):
		self.comenzarDia()
		eventoComienzoDelDia = [Evento(0,"Comienzo del dia "+ str(self.dia))]
		self.logger.logearEventos(eventoComienzoDelDia)
		self.eventos += eventoComienzoDelDia
		tanques =  self.unSubSimDeConstruccion.tanques()
		plantasProcesadoras =  self.unSubSimDeConstruccion.plantasProcesadoras()
		#me quedon con las parcelas que puedo extraer o reinyectar
		parcelasConPozo = self.filtrarParcelas(self.filtrarConPozo)
		if self.politicaDeReinyeccion.elijoReinyectar(parcelasConPozo,self.dia):
			eventosDeReinyeccion = self.unSubSimDeReinyeccion.simularReinyeccion(self.dia, parcelasConPozo, plantasProcesadoras, tanques)
			self.logger.logearEventos(eventosDeReinyeccion)
			self.eventos += eventoComienzoDelDia
		else:
			eventosDeExtraccion = self.unSubSimDeExtraccion.simularExtraccion(self.dia, parcelasConPozo, plantasProcesadoras, tanques)
			self.logger.logearEventos(eventosDeExtraccion)
			self.eventos += eventosDeExtraccion
		eventosDeExcavacion = self.unSubSimDeExcavacion.simularExcavacion(self.dia)
		self.logger.logearEventos(eventosDeExcavacion)
		eventosDeConstruccion = self.unSubSimDeConstruccion.simularConstruccion(self.dia)
		self.logger.logearEventos(eventosDeConstruccion)
		eventoFinDelDia = [Evento(0,"Fin del dia " + str(self.dia))]
		self.logger.logearEventos(eventoFinDelDia)
		self.eventos +=  eventosDeExcavacion + eventosDeConstruccion + eventoFinDelDia
	def comenzarDia(self):
		self.dia += 1