class SubSimDeExtraccion:
	def __init__(self,parcelas,politicaDeExtraccion):
		self.parcelas = parcelas
		self.politicaDeExtraccion=politicaDeExtraccion

	def simularExtraccion(self,dia,parcelasListasParaExtraer,plantasProcesdoras,tanques):
		#	obtenemos las parcelas que tienen el pozo terminado
		#  parcelasListasParaExtraer = list(filter(lambda parcela: parcela.listoParaExtraer()),self.parcelas))
		#	Elegimos las parcelas a ser utilizadas en base a la politica
		parcelasElegidas = self.politicaDeExtraccion.elegir(parcelasListasParaExtraer)
		#	abrimos la valvula y procesamos la materia prima
		ListaEventosDeAperturaDeValvulas =  list(map(lambda parcela: parcela.pozo.abrirValvula(len(parcelasElegidas), plantasProcesdoras,tanques),parcelasElegidas))
		list(map(lambda plantasProcesdora: plantasProcesdora.finDelDia(),plantasProcesdoras))
		return ListaEventosDeAperturaDeValvulas