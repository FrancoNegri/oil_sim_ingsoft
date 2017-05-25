
#clase que loguea todos los eventos del simulador
class Logger:
	def __init__(self, file_name):
		self.log = open(file_name, mode='w')

	def logear(self,log_info):
		self.log.write(log_info + "\n")