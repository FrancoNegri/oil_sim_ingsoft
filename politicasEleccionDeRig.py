import random

#Politicas de eleccion de rig
class PoliticaDeEleccionAbstracta():
	def __init__(self):
		return 

class PoliticaEleccionRigRandom(PoliticaDeEleccionAbstracta):
	def __init__(self):
		return
	def elegirRIG(self,listaRigs):
		return listaRigs[random.randrange(len(listaRigs))]
		
#Politica de donde hacer pozos
class politicaDeSeleccionMenorProfundidad:
	def __init__(self, cantidadDePozos):
		self.cantidadDePozos = cantidadDePozos
	def elegir(self, parcelas):
		parcelas_elegidas = sorted(parcelas, key=lambda parcela: parcela.profundidad())
		return parcelas_elegidas[:self.cantidadDePozos]

#Politica de cuando hacer pozos
class politicaCuandoPerforarParcelasTodasAlPrincipio:
	def __init__(self):
		return
	def parcelasAPerforarHoy(self,listaParcelasAPerforar,administradorRIGS, dia):
		parcelas = []
		for i in range(0,administradorRIGS.cantidadRigsDisponibles()):
			parcelas.append(listaParcelasAPerforar[i])
		return parcelas
#politica de construccion de estructuras

class politicaDeConstruccionDeEstructurasAlPrincipio():
	def __init__(self,cantidad):
		self.cantidad = cantidad

	def elegir(self,dia):
		if dia == 0:
			return cantidad
#Politica de eleccion de parcelas
class politicaDeEleccionDeParcelasParaExtraccion():
	def elegir(parcelasListasParaExtraer):
		return parcelasListasParaExtraer

class politicaDeFinalizacionVencimientoDeContrato():
	def __init__(self,dias):
		self.dias = dias
	def finalizo(dia):
		if dia == self.dias:
			return True
		else:
			return False