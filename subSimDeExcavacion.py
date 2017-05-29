from administradorRIGS import AdministradorRIGS
##SUbsistema de Excavacion
class SubSimDeExcavacion:
	def __init__(self,politicaEleccionRigs,politicaCualYCantidaddePozosParcela,politicaCuandoPerforar,rigs,parcelas):
		self.administradorRIGS = AdministradorRIGS(rigs,politicaEleccionRigs)
		self.politicaCuandoPerforarParcelas = politicaCuandoPerforar
		self.parcelasParaPerforar = politicaCualYCantidaddePozosParcela.elegir(parcelas)

	def simularExcavacion(self,dia):
		listaDeEventos = []
		parcelasAPerforarHoy = self.politicaCuandoPerforarParcelas.parcelasAPerforarHoy(self.parcelasParaPerforar, self.administradorRIGS, dia)
		eventosAsignar = list(map(lambda parcela: self.administradorRIGS.asignarRig(parcela),parcelasAPerforarHoy))
		if eventosAsignar:
			eventosFlat = reduce(lambda x,y: x+y,eventosAsignar)
			listaDeEventos = eventosFlat
		eventosProgresar = self.administradorRIGS.progresar()
		listaDeEventos = listaDeEventos + eventosProgresar
		self.quitarParcelasDeLaCola(parcelasAPerforarHoy)
		return listaDeEventos

	def quitarParcelasDeLaCola(self,parcelasAPerforarHoy):
		for parcela in parcelasAPerforarHoy:
			self.parcelasParaPerforar.remove(parcela)