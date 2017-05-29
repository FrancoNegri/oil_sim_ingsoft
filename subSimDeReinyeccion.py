#Subsimulador de reinyeccion
class SubSimDeReinyeccion:
	def __init__(self, politicaDeReinyeccion):
		self.politicaDeQueParcelasReinyectar = politicaDeReinyeccion

	def simularReinyeccion(self,dia,parcelasConPozo, plantasProcesadoras, tanques):
		#	Elegimos las parcelas a ser utilizadas en base a la politica
		# elegir cuando producto se va a reinyectar en cada pozo, salksakdkask
		parcelasAReinyectar = self.politicaDeQueParcelasReinyectar.elegir(parcelasConPozo,dia)
		eventos = list(map(lambda parcela: parcela.reiyectar() ,parcelasAReinyectar))
		return
		