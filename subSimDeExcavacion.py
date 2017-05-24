from administradorRIGS import AdministradorRIGS

class SubSimDeExcavacion:
	def __init__(self, log):
		self.log = log
		self.administradorRIGS = AdministradorRIGS()
		#TODO: politicaDePlanificacion

	def simularExcavacion(self,dia):
		parcelasAPerforarHoy = politicaDePlanificacion.parcelasAPerforarHoy()
		while administradorRIGS.hayRigsDisponibles() and parcelasAPerforarHoy:
			administradorRIGS.excavar(self.parcelasAPerforarHoy.pop())
			#TODO: faltaria logear este evento
		else:
			self.log.loguear("Nada para excavar")
		self.administradorRigs.progresar()