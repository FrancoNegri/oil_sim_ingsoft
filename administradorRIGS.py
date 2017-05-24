from politicasEleccionDeRig import PoliticaEleccionRigRandom

class AdministradorRIGS:
	def __init__(self):
		self.rigsDisponibles = []
		self.rigsUtilizados = []
		#falta asignar politca
		politicaDeAdministracion = PoliticaEleccionRigRandom()

	def excavar(self,parcela):
		rigAUtilizar = self.dameRig()
		response = this.asignarRig(rigAUtilizar, parcela)
		self.rigsUtilizados.append(rigAUtilizar)

	def hayRigsDisponibles(self):
		return len(self.rigsDisponibles) != 0

	def asignarRig(self,rig, parcela):
		rig.asignarParcela(parcela)

	def dameRig(self):
		return politicaDeAdministracion.elegirRIG(self.rigsDisponibles)

	def progresar(self):
		for rig in self.rigsUtilizados:
			rig.bajarDia() # verificar esto, por el tema de la responsabilidad
			