class Producto():
	def __init__(self):

class ProductoMezcla(producto):
	def __init__(self,volumen, porcentajeAgua,porcentajeGas,porcentajePetroleo):
		self.volumen = volumen
		self.porcentajeAgua = porcentajeAgua
		self.porcentajeGas = porcentajeGas
		self.porcentajePetroleo = porcentajePetroleo

	def refinar():
		return (ProductoRefinadoAgua(self.volumen*self.porcentajeAgua),ProductoRefinadoGas(self.volumen*self.porcentajeGas),ProductoRefinadoPetroleo(self.volumen*self.porcentajePetroleo))


class ProductoRefinadoAgua(producto):
	def __init__(self,volumen):
		self.volumen = volumen

class ProductoRefinadoPetroleo(producto):
	def __init__(self,volumen):
		self.volumen = volumen

class ProductoRefinadoGas(producto):
	def __init__(self,volumen):
		self.volumen = volumen