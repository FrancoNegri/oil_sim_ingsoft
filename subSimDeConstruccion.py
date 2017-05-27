class SubSimDeConstruccion():
	def __init__(self,logger,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDePlantas, constructorDeTanques):
		self.listaTanquesListos = []
		self.listaTanquesConstruyendose = []
		self.listaPlantasProcesadorasListas = []
		self.listaPlantasProcesadorasConstruyendose = []
		self.constructorDePlantas = constructorDePlantas
		self.ConstructorDeTanques = constructorDeTanques
		self.politicaDeConstruccionDeTanques = politicaDeConstruccionDeTanques
		self.politicaDeConstruccionDePlantas = politicaDeConstruccionDePlantas

	def simularConstruccion(self,dia):
		#construyo tanques
		nuevosTanquesAConstruir = self.empezarConstruccionDeEstructuras(dia,self.politicaDeConstruccionDeTanques, self.constructorDeTanques)
		self.listaTanquesConstruyendose = self.listaTanquesConstruyendose + nuevosTanquesAConstruir
		self.pasarDia(self.listaTanquesConstruyendose)
		self.listaTanquesListos = self.listaTanquesListos + estructurasFinalizadas(self.listaTanquesConstruyendose)
		self.listaTanquesConstruyendose = estructurasNoFinalizadas(self.listaTanquesConstruyendose)
		#construyo plantas
		nuevasPlantasAConstruir = self.empezarConstruccionDeEstructuras(dia,self.politicaDeConstruccionDePlantas,self.constructorDePlantas)
		self.listaPlantasProcesadorasConstruyendose = self.listaPlantasProcesadorasConstruyendose + nuevasPlantasAConstruir
		self.pasarDia(self.listaPlantasProcesadorasConstruyendose)
		self.listaPlantasProcesadorasListas = self.listaTanquesListos + estructurasFinalizadas(self.listaPlantasProcesadorasConstruyendose)
		self.listaPlantasProcesadorasConstruyendose = estructurasNoFinalizadas(self.listaPlantasProcesadorasConstruyendose)

	def pasarDia(self,listaEstructuras):
		for estructura in listaEstructuras:
			estructura.pasarDia()		

	def empezarConstruccionDeEstructuras(self,dia,politicaDeConstruccion,constructor):
		estructurasAConstruir = []
		cantidadDeEstructurasAConstruirHoy = politicaDeConstruccion.elegir(dia)
		for i in range(0,cantidadDeEstructurasAConstruirHoy):
			estructurasAConstruir.append(EstructuraEnConstrucción(constructor))
		return estructurasAConstruir

	def estructurasFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: estructura.construccionFinalizada(),listaEstructurasConstruyendose))

	def estructurasNoFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: not estructura.construccionFinalizada(),listaEstructurasConstruyendose))
		


class EstructuraEnConstrucción():
	def __init__(self,constructor):
		self.constructor
		self.diasConstruido = 0
		self.estructura = None
	def pasarDia(self):
		self.diasConstruido += 1
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