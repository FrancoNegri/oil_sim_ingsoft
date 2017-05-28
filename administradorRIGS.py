from politicas import PoliticaEleccionRigRandom


class AdministradorRIGS:
	def __init__(self,rigs,politica):
		#los rigs tienen que tener id para identificarlos
		self.rigsDisponibles = rigs
		self.rigsUtilizados = []
		self.politicaDeAdministracion = politica

	def asignarRig(self,parcela):
		rigAUtilizar = self.dameRig()
		rigAUtilizar.asignarParcela(parcela)
		self.borrarRigDisponiblePorId(rigAUtilizar)
		self.rigsUtilizados.append(rigAUtilizar)

	#borra un rig usando un ID que deberia tener para identificarse
	def removeById(self,rig):
		for i, o in enumerate(self.rigsDisponibles):
			if o.dameId== rig.dameId():
				del self.rigsDisponibles[i]

	def cantidadRigsDisponibles(self):
		return len(self.rigsDisponibles)

	def dameRig(self):
		return self.politicaDeAdministracion.elegirRIG(self.rigsDisponibles)

	def borrarRigsFinalizados(self):
		rigsFinalizados =  list(filter(lambda rig: rig.finalizado(),self.rigsUtilizados))
		self.rigsUtilizados = list(filter(lambda rig: not rig.finalizado(),self.rigsUtilizados))
		self.rigsDisponibles = self.rigsDisponibles + rigsFinalizados

	def progresar(self):
		eventosDeExcavacion = list(map(lambda rig: rig.excavarUnDia(),self.rigsUtilizados))
		self.borrarRigsFinalizados()
		return eventosDeExcavacion