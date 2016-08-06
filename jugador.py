class Jugador:
	def __init__(self,nombre):
		self.nombre=nombre
		self.puntos=0

	def setNombre(self,nombre):
		self.nombre=nombre

	def setNombre(self,puntos):
		self.puntos=puntos
	
	def getNombre(self):
		return self.nombre

	def getPuntos(self):
		return self.puntos
	
	def sumaPuntos(self):
		self.puntos=self.puntos+1
