from evento import Evento
#Clases de Pozos
class PozoAbstracto():
	def __init__(self):
		return
	def listoParaExtraer():
		return

class PozoNull(PozoAbstracto):
	def __init__(self):
		return
	def listoParaExtraer(self):
		return False

class PozoFinalizado(PozoAbstracto):
	def __init__(self, parcela):
		self.parcela = parcela
		self.alfa1 = 0.4
		self.alfa2 = 0.3
		return

	def listoParaExtraer(self):
		return True
    def getVolumenPotencial(self,presion,cantidadDePozosHabilitados):
        return self.alfa1*(presion/cantidadDePozosHabilitados) + self.alfa2*(presion/cantidadDePozosHabilitados)**2

	def abrirValvula(self,cantidadDePozosHabilitados,plantasProcesadoras,tanques):
		presion = self.parcela.getPresion()
		#falta decidir si alfa1 y alfa2 se pasan por parametro o de donde salen
        volumenPotencial = self.getVolumenPotencial(presion,cantidadDePozosHabilitados)
		volumenTotalDelYacimiento = self.parcela.getVolumenRestante()
		#si el volumen
		if volumenPotencial > volumenTotalDelYacimiento:
			volumenPotencial = volumenTotalDelYacimiento
		volumenTotalProcesado = 0
		for plantaProc in plantasProcesadoras:
			#en este caso ya procese todo el producto que tenia, listo
			if volumenTotalProcesado == volumenPotencial:
				break
			else:
				#le pido a la planta que procese todo el volumen posible, me devuelve cuanto pudo procesar posta
				volumenProcesado = plantaProc.procesar(volumenPotencial - volumenTotalProcesado,tanques)
				volumenTotalProcesado += volumenProcesado
		self.parcela.extraerProducto(volumenTotalProcesado,cantidadDePozosHabilitados)
		return Evento(0, "Al abrir la valvula del pozo se extrajo: " + str(volumenTotalProcesado))