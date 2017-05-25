from administradorRIGS import AdministradorRIGS

class politicaDeSeleccionMenorProfundidad:
	def __init__(self, cantidadDePozos):
		self.cantidadDePozos = cantidadDePozos
	def elegir(self, parcelas):
		parcelas_elegidas = sorted(parcelas, key=lambda parcela: parcela.profundidad())
		return parcelas_elegidas[:self.cantidadDePozos]

class politicaCuandoPerforarParcelasTodasAlPrincipio:
	def __init__(self):
		return
	def parcelasAPerforarHoy(self,listaParcelasAPerforar,administradorRIGS, dia):
		parcelas = []
		for i in range(0,administradorRIGS.cantidadRigsDisponibles()):
			parcelas.append(listaParcelasAPerforar.pop())
		return parcelas

class SubSimDeExcavacion:
	def __init__(self,log,politicaDeSeleccion,politicaCuandoPerforarParcelas,parcelas):
		self.log = log
		self.listaParcelasAPerforar = politicaDeSeleccion.elegir(parcelas)
		self.administradorRIGS = AdministradorRIGS()
		self.politicaCuandoPerforarParcelas = politicaCuandoPerforarParcelas
	def simularExcavacion(self,dia):
		parcelasAPerforarHoy = self.politicaCuandoPerforarParcelas.parcelasAPerforarHoy(self.listaParcelasAPerforar, self.administradorRIGS, dia)
		while parcelasAPerforarHoy:
			self.administradorRIGS.excavar(self.parcelasAPerforarHoy.pop())
			#TODO: faltaria logear este evento
		else:
			self.log.logear("Nada para excavar")
		self.administradorRIGS.progresar()