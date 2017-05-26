
#clase que loguea todos los eventos del simulador
class Logger:
	def __init__(self, file_name):
		self.log = open(file_name, mode='w')

	def logearEventos(self,eventos):
		for evento in eventos:
			self.log.write(evento.mensaje() + "\n")