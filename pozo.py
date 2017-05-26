#Clases de Pozos
class pozoAbstracto():
	def __init__(self):
		return
	def listoParaExtraer(self):
		return
class pozoNull(PozoAbstracto):
	def __init__(self)
		return
	def listoParaExtraer(self):
		return False  
class pozoEnProceso(PozoAbstracto):
	def __init__(self)
		return
	def listoParaExtraer(self):
		return False

class pozoFinalizado(PozoAbstracto):
	def __init__(self)
		return
	
	def listoParaExtraer(self):
		return True

	def abrirValvula(self,pozo,cantidadDePozosHabilitados,plantasProcesadoras):
		presion = pozo.presion()
		volumenPotencial = alfa1*(presion/cantidadDePozosHabilitados) + alfa2*(presion/cantidadDePozosHabilitados)^2
		volumenProcesado = 0
		for plantaProc in plantasProcesadoras:
			#en este caso ya procese todo el producto que tenía, listo
			if volumenProcesado == volumenPotencial:
				break
			else:
				#le pido a la planta que procese todo el volumen posible, me devuelve cuanto pudo procesar posta
				volumenProcesado = plantaProc.procesar(volumenPotencial - volumenProcesado)
				volumenTotalProcesado += volumenProcesado
		#despues habría que notificar al yacimiento que acabo de extraer una cantidad de producto x de el