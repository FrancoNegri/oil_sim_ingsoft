from pozo import *
#Tipos de terreo
class Terreno():
	def dameResistencia():
		return

class TerrenoRocoso(Terreno):
	def dameResistencia():
		return 0.6

class TerrenoArcilloso(Terreno):
	def dameResistencia():
		return 0.7

#Clases de Parcela
class ParcelaAbstracta():
	def __init__(self):
		return

class ParcelaNull(ParcelaAbstracta):
	def __init__(self):
		return

class ParcelaConcreta(ParcelaAbstracta):
	def __init__(self,yacimiento,presionInicial,tipoDeTerreno,profundidadAlReservorio):
		self.profundidadAlReservorio = profundidadAlReservorio
		self.yacimiento = yacimiento
		self.presion = presionInicial
		self.presionInicial = presionInicial
		self.tipoDeTerreno = tipoDeTerreno
		self.pozo = PozoNull()

	def extraerProducto(volumen,cantidadDePozos):
		self.yacimiento.extraerProducto(volumen)
		self.presion = self.presion* math.e** BETA
		volRestanteDelYacimiento = self.yacimiento.volumenRestante()
		volInicialDelYacimiento = self.yacimiento.volumenInicial()
		BETA = (0.1 * (volRestanteDelYacimiento/volInicialDelYacimiento))/sqrtCUBO(cantidadDePozos^2)

	def perforar(poderDeExcavacion):
		perforarUnaDistanciaDe(self, poderDeExcavacion*tipoDeTerreno.resistencia())
		finalizarPozoSiProfundidadEsNecesaria(self)

	def perforarUnaDistanciaDe(self,unaDistancia):
		self.profundidadAlReservorio -= unaDistancia

	def finalizarPozoSiProfundidadEsNecesaria(self):
		if self.profundidadAlReservorio < 0:
			self.pozo = pozoFinalizado(self)

	def listoParaExtraer():
		return self.pozo.listoParaExtraer()

	def volumen():
		return self.yacimiento.volumen()

	def reinyectar(volumenAgua,volumenGas):
		#falta hacer el chequeo de reinyeccion sarasa, posiblemente en la politica? ya no tengo idea
		presionDespuesDeReinyeccion = self.presionInicial *( self.yacimiento.volumenInicial() - self.yacimiento.volumenExtraido() + self.yacimiento.volumenReinyectado())/ self.yacimiento.volumenInicial()
		self.yacimiento.reinyectar(volumenAgua,volumenGas)
