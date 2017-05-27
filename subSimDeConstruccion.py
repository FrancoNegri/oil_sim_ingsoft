class SubSimDeConstruccion():
	def __init__(self,logger,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas):
		self.listaTanquesListos = []
		self.listaTanquesConstruyendose = []
		self.listaPlantasProcesadorasListas = []
		self.listaPlantasProcesadorasConstruyendose = []
		self.politicaDeConstruccionDeTanques = politicaDeConstruccionDeTanques
		self.politicaDeConstruccionDePlantas = politicaDeConstruccionDePlantas

	def simularConstruccion(self,dia):
		#construyo tanques
		nuevosTanquesAConstruir = self.empezarConstruccionDeEstructuras(dia,self.politicaDeConstruccionDeTanques)
		self.listaTanquesConstruyendose = self.listaTanquesConstruyendose + nuevosTanquesAConstruir
		self.pasarDia(self.listaTanquesConstruyendose)
		self.listaTanquesListos = self.listaTanquesListos + estructurasFinalizadas(self.listaTanquesConstruyendose)
		self.listaTanquesConstruyendose = estructurasNoFinalizadas(self.listaTanquesConstruyendose)
		#construyo plantas
		nuevasPlantasAConstruir = self.empezarConstruccionDeEstructuras(dia,self.politicaDeConstruccionDePlantas)
		self.listaPlantasProcesadorasConstruyendose = self.listaPlantasProcesadorasConstruyendose + nuevasPlantasAConstruir
		self.pasarDia(self.listaPlantasProcesadorasConstruyendose)
		self.listaPlantasProcesadorasListas = self.listaTanquesListos + estructurasFinalizadas(self.listaPlantasProcesadorasConstruyendose)
		self.listaPlantasProcesadorasConstruyendose = estructurasNoFinalizadas(self.listaPlantasProcesadorasConstruyendose)

	def pasarDia(listaEstructuras):
		for estructura in listaEstructuras:
			estructura.pasarDia()		

	def empezarConstruccionDeEstructuras(self,dia,politicaDeConstruccion):
		estructurasAConstruir = []
		cantidadDeEstructurasAConstruirHoy = politicaDeConstruccion.elegir(dia)
		for i in range(0,cantidadDeEstructurasAConstruirHoy):
			estructurasAConstruir.append(EstructuraEnConstrucción())
		return estructurasAConstruir

	def estructurasFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: estructura.construccionFinalizada(),listaEstructurasConstruyendose))

	def estructurasNoFinalizadas(self, listaEstructurasConstruyendose):
		return list(filter(lambda estructura: not estructura.construccionFinalizada(),listaEstructurasConstruyendose))
		


class EstructuraEnConstrucción():
	def __init__(self,diasDeConstruccion,estructura):
		self.diasDeConstruccion = diasDeConstruccion
		self.estructura = estructura
		self.diasConstruido = 0

	def pasarDia():
		self.diasConstruido += 1

	def construccionFinalizada():
		return self.diasConstruido == self.diasDeConstruccion

	def estructura():
		return estructura