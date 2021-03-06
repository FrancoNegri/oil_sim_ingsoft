import functools
class CalculadorDeGanancia():
	def calcular(self,eventos):
		listaGanancias = list(map(lambda evento: evento.getGanancia(),eventos))
		if listaGanancias:
			gananciaTotal = functools.reduce(lambda x,y: x+y,listaGanancias)
		return gananciaTotal