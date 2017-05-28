from politicasEleccionDeRig import PoliticaEleccionRigRandom


class AdministradorRIGS:
	def __init__(self,rigs,Politca):
		#los rigs tienen que tener id para identificarlos
		self.rigsDisponibles = rigs
		self.rigsUtilizados = []
		politicaDeAdministracion = Politica
		
	def asignarRig(self,parcela):
		rigAUtilizar = self.dameRig()
		rigAUtilizar.asignarParcela(parcela)
		self.removeById(rigAUtilizar)
		self.rigsUtilizados.append(rigAUtilizar)
	
	#borra un rig usando un ID que deberia tener para identificarse
	def removeById(self,rig):	
		 sorted(parcelas, key=lambda parcela: parcela.profundidad())
		
	def cantidadRigsDisponibles(self):
		return len(self.rigsDisponibles)
		
	def dameRig(self):
		return politicaDeAdministracion.elegirRIG(self.rigsDisponibles)
		
	def borrarRigsFinalizados(self):
		rigsFinalizados =  list(filter(lambda rig: rig.parcela().listoParaExtraer(),self.rigsUtilizados))
		self.rigsUtilizados = list(filter(lambda rig: not rig.parcela().listoParaExtraer(),self.rigsUtilizados))
		self.rigsDisponibles = self.rigsDisponibles + rigsFinalizados
		
	def progresar(self):
		eventosDeExcavacion = list(map(lambda rig: rig.excavarUnDia(),self.rigsUtilizados))
		self.borrarRigsFinalizados()
		return eventosDeExcavacion