from politicas import PoliticaEleccionRigRandom
from parcela import *
from evento import Evento
class Rig:
	contador = 0
	
	def __new__(cls,poderDeExcavacion,costoDiario,minimoDeDiasAPagar,consumoDeCombustible):
		contador += 1
		return super(Rig, cls).__new__(cls,contador,poderDeExcavacion,costoDiario,minimoDeDiasAPagar,consumoDeCombustible)
	
	#faltan algunas cosas como, que primero tenes que alquilarlo y despues lo podes desalquilar?
	def __init__(self,id,poderDeExcavacion,costoDiario,minimoDeDiasAPagar,consumoDeCombustible):
		self.poderDeExcavacion = poderDeExcavacion
		self.costoDiario = costoDiario
		self.minimoDeDiasAPagar = minimoDeDiasAPagar
		self.consumoDeCombustible = consumoDeCombustible
		self.costo = 0
		self.parcela = ParcelaNull()
		self.id = id
		
	def asignarParcela(self,parcela):
		self.parcela = parcela
		
	def excavarUnDia(self):
		self.costo += self.costoDiario
		self.parcela.perforar(self.poderDeExcavacion)
		return Evento(self.costoDiario, "Se Excava la parcela...")

	def finalizado(self):
		return self.parcela.listoParaExtraer()

	def dilucionDePetroleo(self):
		#que hace esto?
		return