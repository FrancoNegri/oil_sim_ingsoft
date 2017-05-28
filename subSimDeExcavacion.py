from administradorRIGS import AdministradorRIGS
##SUbsistema de Excavacion
class SubSimDeExcavacion:
	def __init__(self,politicaDeSeleccionDeRig,politicaCuandoPerforarParcelas,rigs):
		self.administradorRIGS = AdministradorRIGS(politicaDeSeleccionDeRig,rigs)
		self.politicaCuandoPerforarParcelas = politicaCuandoPerforarParcelas

	def simularExcavacion(self,dia, parcelasParaPerforar):
		parcelasAPerforarHoy = self.politicaCuandoPerforarParcelas.parcelasAPerforarHoy(parcelasParaPerforar, self.administradorRIGS, dia)
		list(map(lambda parcela: self.administradorRIGS.asignarRig(parcela),parcelasAPerforarHoy))
		self.log.logear("Nada mas para excavar")
		self.administradorRIGS.progresar()
