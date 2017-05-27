##SUbsistema de Excavacion
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
			parcelas.append(listaParcelasAPerforar[i])

		return parcelas

class SubSimDeExcavacion:
	def __init__(self,politicaDeSeleccionDeRig,politicaCuandoPerforarParcelas,rigs):
		self.administradorRIGS = AdministradorRIGS(politicaDeSeleccionDeRig,rigs)
		self.politicaCuandoPerforarParcelas = politicaCuandoPerforarParcelas

	def simularExcavacion(self,dia, parcelasParaPerforar):
		parcelasAPerforarHoy = self.politicaCuandoPerforarParcelas.parcelasAPerforarHoy(parcelasParaPerforar, self.administradorRIGS, dia)
		list(map(lambda parcela: self.administradorRIGS.asignarRig(parcela),parcelasAPerforarHoy))
		self.log.logear("Nada mas para excavar")
		self.administradorRIGS.progresar()
