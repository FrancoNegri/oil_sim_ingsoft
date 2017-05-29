from pozo import *
import math
#Tipos de terreo
class Terreno():
	def dameResistencia(self):
		return

class TerrenoRocoso(Terreno):
	def dameResistencia(self):
		return 0.6

class TerrenoArcilloso(Terreno):
	def dameResistencia(self):
		return 0.7

#Clases de Parcela
class ParcelaAbstracta():
	def __init__(self):
		return

class ParcelaNull(ParcelaAbstracta):
	def __init__(self):
		return

class ParcelaConcreta(ParcelaAbstracta):
	contador =1;

	def __init__(self,yacimiento,presionInicial,tipoDeTerreno,profundidadAlReservorio):
		self.profundidadAlReservorio = profundidadAlReservorio
		self.yacimiento = yacimiento
		self.id= ParcelaConcreta.contador
		ParcelaConcreta.contador+=1
		self.presion = presionInicial
		self.presionInicial = presionInicial
		self.tipoDeTerreno = tipoDeTerreno
		self.pozo = PozoNull()

	def dameId(self):
		return self.id

	def extraerProducto(self,volumen,cantidadDePozos):
		volRestanteDelYacimiento = self.yacimiento.getVolumenRestante()
		volInicialDelYacimiento = self.yacimiento.getVolumenInicial()
		BETA = (0.1 * (volRestanteDelYacimiento/volInicialDelYacimiento))/(((cantidadDePozos*1.0)**2)**(1./3))
		self.presion = self.presion* math.exp(BETA)
		self.yacimiento.extraerProducto(volumen)

	def perforar(self,poderDeExcavacion):
		self.perforarUnaDistanciaDe(poderDeExcavacion*self.tipoDeTerreno.dameResistencia())
		self.finalizarPozoSiProfundidadEsNecesaria()

	def perforarUnaDistanciaDe(self,unaDistancia):
		self.profundidadAlReservorio -= unaDistancia

	def finalizarPozoSiProfundidadEsNecesaria(self):
		if self.profundidadAlReservorio < 0:
			self.pozo = PozoFinalizado(self)

	def listoParaExtraer(self):
		return self.pozo.listoParaExtraer()

	def getVolumenRestante(self):
		return self.yacimiento.getVolumenRestante()

	def reinyectar(self,volumenAgua,volumenGas):
		#falta hacer el chequeo de reinyeccion sarasa, posiblemente en la politica? ya no tengo idea
		presionDespuesDeReinyeccion = self.presionInicial *( self.yacimiento.getVolumenInicial() - self.yacimiento.getVolumenExtraido() + self.yacimiento.getVolumenReinyectado())/ self.yacimiento.getVolumenInicial()
		self.yacimiento.reinyectar(volumenAgua,volumenGas)
		return Evento(-100, "Reinyeccion Finalizada, Reinyectado Agua: " + str(volumenAgua) + " Gas" + str(volumenGas))

	def profundidad(self):
		return self.profundidadAlReservorio

	def getPresion(self):
		return self.presion

	def dilucionDePetroleo(self):
		return self.yacimiento.getProporcionDePetroleo()