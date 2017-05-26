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
	def __init__(self,profundidadAlReservorio,precionInicial,tipoDeTerreno):
		self.profundidadAlReservorio = profundidadAlReservorio
		self.precionInicial = precionInicial
		self.tipoDeTerreno = tipoDeTerreno
        self.pozo = pozoNull()
        self.profunididadRestanteAlReservorio = self.profundidadAlReservorio
	
	def perforar(poderDeExcavacion)
	    self.profunididadRestanteAlReservorio -= poderDeExcavacion*tipoDeTerreno.resistencia()
	    if profunididadRestanteAlReservorio < 0:
	        self.pozo = pozoFinalizado()
	
	def listoParaExtraer()
	    return self.pozo.listoParaExtraer()