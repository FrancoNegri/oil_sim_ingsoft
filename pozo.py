#Clases de Pozos
class pozoAbstracto():
	def __init__(self):
		return
	def listoParaExtraer():
		return

class pozoNull(PozoAbstracto):
	def __init__(self)
		return
	def listoParaExtraer():
		return False
		
class pozoFinalizado(PozoAbstracto):
	def __init__(self, parcela)
		self.parcela = parcela
		return
	
	def listoParaExtraer(self):
		return True

	def abrirValvula(self,cantidadDePozosHabilitados,plantasProcesadoras):
		presion = self.parcela.presion()
		volumenPotencial = alfa1*(presion/cantidadDePozosHabilitados) + alfa2*(presion/cantidadDePozosHabilitados)^2
		volumenTotalDelYacimiento = self.parcela.volumen()
		#si el volumen 
		if volumenPotencial > volumenTotalDelYacimiento:
			volumenPotencial = volumenTotalDelYacimiento
		volumenTotalProcesado = 0
		for plantaProc in plantasProcesadoras:
			#en este caso ya procese todo el producto que tenía, listo
			if volumenProcesado == volumenPotencial:
				break
			else:
				#le pido a la planta que procese todo el volumen posible, me devuelve cuanto pudo procesar posta
				volumenProcesado = plantaProc.procesar(volumenPotencial - volumenProcesado)
				volumenTotalProcesado += volumenTotalProcesado
				
		self.parcela.extraerProducto(volumenProcesado,cantidadDePozosHabilitados)
		#despues habría que notificar al yacimiento que acabo de extraer una cantidad de producto x de el