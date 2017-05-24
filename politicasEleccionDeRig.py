import random

class PoliticaEleccionRigRandom:
	def __init__(self):
		return

	def elegirRIG(self,listaRigs):
		return listaRigs.pop(random.randrange(len(listaRigs)))