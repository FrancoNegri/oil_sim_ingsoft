class Yacimiento:
	def __init__(self,volumenInicial,proporcionGas,proporcionAgua,proporcionPetroleo):
		self.volumen=volumenInicial
		self.volumenRestante=volumenInicial
		self.proporcionGas = proporcionGas
		self.proporcionAgua=proporcionAgua
		self.proporcionPetroleo=proporcionPetroleo
		self.volumenReinyectado = 0
	def extreaerProducto(volumen):
		self.volumenRestante-=volumen
	def volumenRestante():
		return self.volumenRestante
	def volumenInicial():
		return self.volumenInicial
	def volumenExtraido():
		return self.volumenInicial - self.volumenRestante
	def reinyectar(volumenAgua,volumenGas):
		self.volumenReinyectado += volumenAgua + volumenGas
		self.proporcionAgua = (self.proporcionAgua * ((self.volumenInicial() - self.volumenExtraido) + 100* self.volumenReinyectado()))/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
		self.proporcionGas = (self.proporcionGas * (self.volumenInicial() - self.volumenExtraido) )/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
		self.proporcionPetroleo = (self.proporcionPetroleo * (self.volumenInicial() - self.volumenExtraido))/(self.volumenInicial() - self.volumenExtraido() + self.volumenReinyectado)
