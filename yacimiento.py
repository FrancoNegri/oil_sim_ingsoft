class Yacimiento:
	def __init__(self,volumenInicial,proporcionGas,proporcionAgua,proporcionPetroleo):
		self.volumen=float(volumenInicial)
		self.volumenInicial = float(volumenInicial)
		self.volumenRestante=float(volumenInicial)
		self.proporcionGas = float(proporcionGas)
		self.proporcionAgua=float(proporcionAgua)
		self.proporcionPetroleo=float(proporcionPetroleo)
		self.volumenReinyectado = float(0)
	def getProporcionDePetroleo(self):
		return self.proporcionPetroleo
	def extraerProducto(self,volumen):
		self.volumenRestante-=volumen
	def getVolumenRestante(self):
		return self.volumenRestante
	def getVolumenInicial(self):
		return self.volumenInicial
	def getVolumenExtraido(self):
		return self.volumenInicial - self.volumenRestante
	def reinyectar(volumenAgua,volumenGas):
		self.volumenReinyectado += volumenAgua + volumenGas
		self.proporcionAgua = (self.proporcionAgua * ((self.volumenInicial() - self.volumenExtraido) + 100* self.volumenReinyectado()))/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
		self.proporcionGas = (self.proporcionGas * (self.volumenInicial() - self.volumenExtraido) )/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
		self.proporcionPetroleo = (self.proporcionPetroleo * (self.volumenInicial() - self.volumenExtraido))/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
