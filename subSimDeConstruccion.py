#Simulador de construccion
class SubSimDeConstruccion():
	def __init__(self,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDePlantas, constructorDeTanques):
		self.administradorDeTanques = administradorDeEstructuras(politicaDeConstruccionDeTanques,constructorDeTanques)
		self.administradorDePlantas = administradorDeEstructuras(politicaDeConstruccionDePlantas,constructorDePlantas)

	def simularConstruccion(self,dia):
		self.administradorDeTanques.simularConstruccion(dia)
		self.administradorDePlantas.simularConstruccion(dia)

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
		self.pasarDia(self.listaEstructurasConstruyendose)
		self.listaDeEstructurasListas = self.listaDeEstructurasListas + estructurasFinalizadas(self.listaEstructurasConstruyendose)
		self.listaEstructurasConstruyendose = estructurasNoFinalizadas(self.listaEstructurasConstruyendose)

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

class EstructuraEnConstruccion():
	def __init__(self,constructor):
		self.constructor
		self.diasConstruido = 0
		self.estructura = None
	def pasarDia(self):
		self.diasConstruido += 1
		return Evento(0,"Construccion Abanza un dia")
	def construccionFinalizada(self):
		return self.diasConstruido == self.constructor.tiempoDeConstruccion()
	def estructura(self):
		if self.construccionFinalizada():
			if self.estructura is None:
				self.estructura = self.constructor.construir()
		return self.estructura

class ConstructorDePlantasProcesadoras():
	def __init__(self, tiempoDeConstruccion, costo, capacidadMax):
		self.tiempoDeConstruccion = tiempoDeConstruccion
		self.costo = costo
		self.capacidadMax = capacidadMax
	def construir(self):
		return PlantaProcesadora(capacidadMax)
	def costo(self):
		return self.costo
	def tiempoDeConstruccion(self):
		return self.tiempoDeConstruccion

class ConstructorDeTanques():
	def __init__(self, tiempoDeConstruccion, costo, capacidadMax):
		self.tiempoDeConstruccion = tiempoDeConstruccion
		self.costo = costo
		self.capacidadMax = capacidadMax
	def construir(self):
		return Tanque(capacidadMax)
	def costo(self):
		return self.costo
	def tiempoDeConstruccion(self):
		return self.tiempoDeConstruccion