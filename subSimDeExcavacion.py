from administradorRIGS import AdministradorRIGS
##SUbsistema de Excavacion
class SubSimDeExcavacion:
	def __init__(self,politicaEleccionRigs,politicaCualYCantidaddePozosParcela,politicaCuandoPerforar,rigs,parcelas):
		self.administradorRIGS = AdministradorRIGS(rigs,politicaEleccionRigs)
		self.politicaCuandoPerforarParcelas = politicaCuandoPerforar
		self.parcelasParaPerforar = politicaCualYCantidaddePozosParcela.elegir(parcelas)

	def simularExcavacion(self,dia):
		#TODO: falta quitar las parcelas de la lista a perforar
		parcelasAPerforarHoy = self.politicaCuandoPerforarParcelas.parcelasAPerforarHoy(self.parcelasParaPerforar, self.administradorRIGS, dia)
		eventosAsignar = list(map(lambda parcela: self.administradorRIGS.asignarRig(parcela),parcelasAPerforarHoy))
		eventosFlat = reduce(lambda x,y: x+y,eventosAsignar)
		eventosProgresar = self.administradorRIGS.progresar()
		return eventosFlat