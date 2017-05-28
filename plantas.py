#tanques y plantas
class PlantaProcesadora:
	def __init__(self,capacidadMaxima):
		self.capacidadMaxima=capacidadMaxima
		self.capacidadUtilizada=0
	def procesar(self,volumen):
		volumenDisponible = (self.capacidadMaxima-self.capacidadUtilizada)
		if volumenDisponible>volumen:
			procesado = volumen
		else:
			procesado = volumenDisponible
		self.capacidadUtilizada +=procesado
		return procesado

class Tanque:
	def __init__(self,capacidadMaxima):
		self.capacidadMaxima=capacidadMaxima
		self.capacidadUtilizada=0
		
	def almacenar(self,volumen):
		volumenDisponible = (self.capacidadMaxima-self.capacidadUtilizada)
		if volumenDisponible>volumen:
			almacenado = volumen
		else:
			almacenado = volumenDisponible
		self.capacidadUtilizada +=almacenado
		# registrar evento
		return almacenado

	def vender(self,volumen):
		self.capacidadUtilizada -= volumen
		#registrar evento
		
	#def estaLleno():
	#	return self.capacidadMaxima==self.capacidadUtilizada
