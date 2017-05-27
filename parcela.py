#Tipos de terreo
class terreno():
	def dameResistencia():
		return

class terrenoRocoso(terreno):
	def dameResistencia():
		return 0.6

class terrenoArcilloso(terreno):
	def dameResistencia():
		return 0.7

#Clases de Parcela
class parcelaAbstracta():
	def __init__(self)
		return

class parcelaNull(parcelaAbstracta):
	def __init__(self)
		return

class parcelaConcreta(parcelaAbstracta):
	def __init__(self,yacimiento,presionInicial,tipoDeTerreno,profundidadAlReservorio):
		self.profundidadAlReservorio = profundidadAlReservorio
		self.yacimiento = yacimiento
		self.presion = presionInicial
		self.tipoDeTerreno = tipoDeTerreno
		self.pozo = pozoNull()

	def extraerProducto(volumen,cantidadDePozos):
		self.yacimiento.extraerProducto(volumen)
		self.presion = self.presion* math.e** BETA
		volRestanteDelYacimiento = self.yacimiento.volumenRestante()
		volInicialDelYacimiento = self.yacimiento.volumenInicial()
		BETA = (0.1 * (volRestanteDelYacimiento/volInicialDelYacimiento))/sqrtCUBO(cantidadDePozos^2)
	
	def perforar(poderDeExcavacion)
		perforarUnaDistanciaDe(self, poderDeExcavacion*tipoDeTerreno.resistencia())
		finalizarPozoSiProfundidadEsNecesaria(self)
	
	def perforarUnaDistanciaDe(self,unaDistancia)
		self.profundidadAlReservorio -= unaDistancia
	    
	def finalizarPozoSiProfundidadEsNecesaria(self)
		if self.profundidadAlReservorio < 0:
			self.pozo = pozoFinalizado(self)

	def listoParaExtraer()
		return self.pozo.listoParaExtraer()

	def volumen():
		return self.yacimiento.volumen()
