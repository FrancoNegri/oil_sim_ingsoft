from politicasEleccionDeRig import PoliticaEleccionRigRandom
from parcela import *
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
		
	def asignarParcela(parcela):
		self.parcela = parcela
		
	def excavarUnDia():
		self.costo += self.costoDiario
		self.parcela.perforar(self.poderDeExcavacion)
		return Evento(self.costoDiario, "Se Excava la parcela...")

	def dilucionDePetroleo():
		#que hace esto?
		return