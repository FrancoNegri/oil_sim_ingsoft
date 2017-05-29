from politicas import PoliticaEleccionRigRandom
from evento import Evento

class AdministradorRIGS:
	def __init__(self,rigs,politica):
		#los rigs tienen que tener id para identificarlos
		self.rigsDisponibles = rigs
		self.rigsUtilizados = []
		self.politicaDeAdministracion = politica

	def asignarRig(self,parcela):
		rigAUtilizar = self.dameRig()
		eventoAsignarParsela = rigAUtilizar.asignarParcela(parcela)
		self.rigsUtilizados.append(rigAUtilizar)
		self.rigsDisponibles.remove(rigAUtilizar)
		evento = Evento(0,"rig " + str(rigAUtilizar.dameId()) + " paso a ser un rig utilizado")
		return [eventoAsignarParsela, evento]



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