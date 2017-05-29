from evento import Evento

from plantas import *
#Simulador de construccion
class SubSimDeConstruccion():
	def __init__(self,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDePlantas, constructorDeTanques):
		self.administradorDeTanques = administradorDeEstructuras(politicaDeConstruccionDeTanques,constructorDeTanques)
		self.administradorDePlantas = administradorDeEstructuras(politicaDeConstruccionDePlantas,constructorDePlantas)

	def simularConstruccion(self,dia):
		eventosConstruccionTanques = self.administradorDeTanques.simularConstruccion(dia)
		eventosConstruccionPlantas = self.administradorDePlantas.simularConstruccion(dia)
		return eventosConstruccionTanques+eventosConstruccionPlantas

	def tanques(self):
		return self.administradorDeTanques.estructurasParaUtilizar()

	def plantasProcesadoras(self):
		return self.administradorDePlantas.estructurasParaUtilizar()

#Administrador de tanques o administrador de plantas procesadoras
class administradorDeEstructuras():
	def __init__(self,politicaDeConstruccionDeEstructuras,constructorDeEstrcturas):
		self.politicaDeConstruccionDeEstructuras = politicaDeConstruccionDeEstructuras
		self.constructorDeEstrcturas = constructorDeEstrcturas
		self.listaEstructurasConstruyendose = []
		self.listaDeEstructurasListas = []

	def simularConstruccion(self,dia):
		nuevasEstructurasAConstruir = self.empezarConstruccionDeEstructuras(dia,self.politicaDeConstruccionDeEstructuras, self.constructorDeEstrcturas)
		self.listaEstructurasConstruyendose = self.listaEstructurasConstruyendose + nuevasEstructurasAConstruir
		eventosNuevos = list(map(lambda ne : Evento(0,"agrego nueva estructura a construir " + ne.dameNombre()),nuevasEstructurasAConstruir))
		eventosPasarDia = self.pasarDia(self.listaEstructurasConstruyendose)
		self.listaDeEstructurasListas = self.listaDeEstructurasListas + self.estructurasFinalizadas(self.listaEstructurasConstruyendose)
		self.listaEstructurasConstruyendose = self.estructurasNoFinalizadas(self.listaEstructurasConstruyendose)
		return eventosNuevos+eventosPasarDia

	def pasarDia(self,listaEstructuras):
		eventos = []
		for estructura in listaEstructuras:
			evento = estructura.pasarDia()
			eventos.append(evento)
		return eventos

	def empezarConstruccionDeEstructuras(self,dia,politicaDeConstruccion,constructor):
		estructurasAConstruir = []
		cantidadDeEstructurasAConstruirHoy = politicaDeConstruccion.elegir(dia)
		for i in range(0,cantidadDeEstructurasAConstruirHoy):
			estructurasAConstruir.append(EstructuraEnConstruccion(constructor))
		return estructurasAConstruir

	def estructurasFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: estructura.construccionFinalizada(),listaEstructurasConstruyendose))

	def estructurasNoFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: not estructura.construccionFinalizada(),listaEstructurasConstruyendose))

	def estructurasParaUtilizar(self):
		return list(map(lambda estructura: estructura.getEstructura(),self.listaDeEstructurasListas))

class EstructuraEnConstruccion():
	contadorTanques=0
	contadorPlantas=0

	def __init__(self,constructor):
		self.diasConstruido = 0
		self.constructor = constructor
		if constructor.dameNombre()=='planta':
			self.id=EstructuraEnConstruccion.contadorPlantas
			EstructuraEnConstruccion.contadorPlantas+=1
		else:
			self.id=EstructuraEnConstruccion.contadorTanques
			EstructuraEnConstruccion.contadorTanques+=1

		self.estructura = ConstructorNulo()
	def pasarDia(self):
		self.diasConstruido += 1
		return Evento(0,"Construccion Abanza un dia "+self.constructor.dameNombre() + " " +str(self.id) +" quedan "+str(self.constructor.getTiempoDeConstruccion()-self.diasConstruido)+" dias para que termine su construccion")
	def dameNombre(self):
		return self.constructor.dameNombre()
	def construccionFinalizada(self):
		return self.diasConstruido == self.constructor.getTiempoDeConstruccion()
	def getEstructura(self):
		if self.construccionFinalizada():
			if not self.estructura.esValida():
				self.estructura = self.constructor.construir()
		return self.estructura

class ConstructorNulo():
	def __init__(self):
		return
	def esValida(self):
		return False

class ConstructorDePlantasProcesadoras():
	def __init__(self, tiempoDeConstruccion, costo, capacidadMax):
		self.tiempoDeConstruccion = tiempoDeConstruccion
		self.costo = costo
		self.capacidadMax = capacidadMax
		self.name='planta'
	def esValida(self):
		return True
	def dameNombre(self):
		return self.name
	def construir(self):
		return PlantaProcesadora(self.capacidadMax)
	def getCosto(self):
		return self.costo
	def getTiempoDeConstruccion(self):
		return self.tiempoDeConstruccion

class ConstructorDeTanques():
	def __init__(self, tiempoDeConstruccion, costo, capacidadMax):
		self.name='tanque'
		self.tiempoDeConstruccion = tiempoDeConstruccion
		self.costo = costo
		self.capacidadMax = capacidadMax
	def esValida(self):
		return True
	def dameNombre(self):
		return self.name
	def construir(self):
		return Tanque(self.capacidadMax)
	def getCosto(self):
		return self.costo
	def getTiempoDeConstruccion(self):
		return self.tiempoDeConstruccion