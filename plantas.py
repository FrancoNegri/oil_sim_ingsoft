#tanques y plantas
class PlantaProcesadora:
	def __init__(self,capacidadMaxima):
		self.capacidadMaxima=capacidadMaxima
		self.capacidadUtilizadaDuranteElDia=0
	def procesar(self,volumen,tanques):
		volumenPotencialDisponible = (self.capacidadMaxima-self.capacidadUtilizadaDuranteElDia)
		
		if volumenPotencialDisponible>volumen:
			volumenPotencialProcesado = volumen
		else:
			volumenPotencialProcesado = volumenPotencialDisponible
		
		volumenTotalProcesado = 0
		for tanque in tanques:
			#en este caso ya procese todo el producto que tenia, listo
			if volumenTotalProcesado == volumenPotencialProcesado:
				break
			else:
				#le pido a la planta que procese todo el volumen posible, me devuelve cuanto pudo procesar posta
				volumenProcesado = tanque.almacenar(volumenPotencialProcesado - volumenTotalProcesado)
				volumenTotalProcesado += volumenProcesado

		self.capacidadUtilizadaDuranteElDia +=volumenTotalProcesado
		return volumenTotalProcesado

	def finDelDia(self):
		self.capacidadUtilizadaDuranteElDia = 0

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
