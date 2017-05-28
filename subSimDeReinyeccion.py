#Politicas de cuando reinyectar
class PoliticaDeReinyeccionReinyectoEnPuntoCritico():
	def __init__(self, presionCritica,dilucionCritica):
		self.presionCritica = presionCritica
		self.dilucionCritica = dilucionCritica
	
	def elijoReinyectar(parcelas,dia):
		for parcela in parcelasConPozo:
			if parcela.presion() < self.presionCritica and parcela.dilucionDePetroleo() > self.dilucionCritica:
				return True
		return False

#Subsimulador de reinyeccion
class SubSimDeReinyeccion:
	def __init__(self):
		return

	def simularReinyeccion(self,dia):
		#	Elegimos las parcelas a ser utilizadas en base a la politica
		# elegir cuando producto se va a reinyectar en cada pozo, salksakdkask
		parcelasAReinyectar = politicaDeQueParcelasReinyectar.elegir(parcelasConPozo,dia)
		eventos = list(map(lambda parcela: parcela.reiyectar() ,parcelasAReinyectar))
		return
		