#Clases de Pozos
class PozoAbstracto():
	def __init__(self):
		return
	def listoParaExtraer():
		return

class PozoNull(PozoAbstracto):
	def __init__(self):
		return
	def listoParaExtraer():
		return False
		
class PozoFinalizado(PozoAbstracto):
	def __init__(self, parcela):
		self.parcela = parcela
		return
	
	def listoParaExtraer(self):
		return True

	def abrirValvula(self,cantidadDePozosHabilitados,plantasProcesadoras):
		presion = self.parcela.presion()
		#falta decidir si alfa1 y alfa2 se pasan por parametro o de donde salen
		volumenPotencial = alfa1*(presion/cantidadDePozosHabilitados) + alfa2*(presion/cantidadDePozosHabilitados)^2
		volumenTotalDelYacimiento = self.parcela.volumen()
		#si el volumen 
		if volumenPotencial > volumenTotalDelYacimiento:
			volumenPotencial = volumenTotalDelYacimiento
		volumenTotalProcesado = 0
		for plantaProc in plantasProcesadoras:
			#en este caso ya procese todo el producto que tenia, listo
			if volumenProcesado == volumenPotencial:
				break
			else:
				#le pido a la planta que procese todo el volumen posible, me devuelve cuanto pudo procesar posta
				volumenProcesado = plantaProc.procesar(volumenPotencial - volumenProcesado)
				volumenTotalProcesado += volumenTotalProcesado
		self.parcela.extraerProducto(volumenProcesado,cantidadDePozosHabilitados)
		return Evento(0, "Al abrir la valvula del pozo se extrajo: " + str(volumenProcesado))