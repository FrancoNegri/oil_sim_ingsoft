from politicas import PoliticaEleccionRigRandom
from parcela import *
from evento import Evento
class Rig:
	contador = 1

	#faltan algunas cosas como, que primero tenes que alquilarlo y despues lo podes desalquilar?
	def __init__(self,poderDeExcavacion,costoDiario,minimoDeDiasAPagar,consumoDeCombustible):
		self.poderDeExcavacion = poderDeExcavacion
		self.costoDiario = costoDiario
		self.minimoDeDiasAPagar = minimoDeDiasAPagar
		self.consumoDeCombustible = consumoDeCombustible
		self.costo = 0
		self.parcela = ParcelaNull()
		self.id = Rig.contador
		Rig.contador+=1

	def dameId(self):
		return self.id

	def asignarParcela(self,parcela):
		self.parcela = parcela
		return Evento(0,"se asigna la parcela "+str(parcela.dameId())+ " al rig " + str(self.dameId()) )

	def excavarUnDia(self):
		self.costo += self.costoDiario
		self.parcela.perforar(self.poderDeExcavacion)
		return Evento(self.costoDiario, "Se Excava la parcela...")

	def finalizado(self):
		return self.parcela.listoParaExtraer()

	def dilucionDePetroleo(self):
		#que hace esto?
		return