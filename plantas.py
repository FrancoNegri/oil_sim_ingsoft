#tanques y plantas
from evento import *
class PlantaNula:
	def __init__(self):
		return
	def esValida(self):
		return False

class PlantaProcesadora:
	def __init__(self,capacidadMaxima):
		self.capacidadMaxima=capacidadMaxima
		self.capacidadUtilizadaDuranteElDia=0

	def esValida(self):
		return True
	def procesar(self,volumen,tanques):
		if volumen <= self.volumenDisponible(tanques): 
			self.capacidadUtilizadaDuranteElDia += volumen
			for tanque in tanques:
				volumenTanque = tanque.volumenDisponible()
				if volumenTanque > volumen:
					tanque.almacenar(volumenTanque)
					volumen = 0
				else:
					tanque.almacenar(volumenTanque)
					volumen -= volumenTanque
		else:
			raise Exception('Capacidad procesable excedida')
		return Evento(0,"Se procesaron: " + str(volumen) + "en planta procesadora")


	def volumenDisponible(self, tanques):
		volumenPotencialUtilizable = (self.capacidadMaxima-self.capacidadUtilizadaDuranteElDia)
		volumenDisponibleEnTanques = 0
		for tanque in tanques:
			volumenDisponibleEnTanques += tanque.volumenDisponible()
		if volumenDisponibleEnTanques > volumenPotencialUtilizable:
			volumenDisponible = volumenPotencialUtilizable
		else:
			volumenDisponible = volumenDisponibleEnTanques
		return volumenDisponible

	def finDelDia(self):
		self.capacidadUtilizadaDuranteElDia = 0

class Tanque:
	def __init__(self,capacidadMaxima):
		self.capacidadMaxima=capacidadMaxima
		self.capacidadUtilizada=0
	def esValida(self):
		return True
	def almacenar(self,volumen):
		volumenDisponible = self.volumenDisponible()
		if volumenDisponible >= volumen:
			self.capacidadUtilizada +=volumen
		else:
			raise Exception('Capacidad almacenable excedida')

	def volumenDisponible(self):
		volumenDisponible = (self.capacidadMaxima-self.capacidadUtilizada)
		return volumenDisponible

	def vender(self,volumen):
		self.capacidadUtilizada -= volumen
		#registrar evento

	#def estaLleno():
	#	return self.capacidadMaxima==self.capacidadUtilizada
