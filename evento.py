class Evento():
	def __init__(self,costoDelEvento, mensaje):
		self.costoDelEvento = costoDelEvento
		self.mensaje = mensaje

	def getCostoDelEvento(self):
		return self.costoDelEvento

	def getMensaje(self):
		return self.mensaje