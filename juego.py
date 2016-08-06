import frase
import jugador
class Juego(frase.Frase):
	def __init__(self,fras, vidas, n1, n2):
		self.vidas=vidas
		self.j1=jugador.Jugador(n1)
		self.j2=jugador.Jugador(n2)
		self.ganar=False
		frase.Frase.__init__(self,fras)
	
	def comprobar(self,fras):
		if(self.sustituir(fras)==False):
			self.setVidas(self.getVidas()-1)

	def resolver(self,frase):
		if frase==self.getFrase():
			self.ganar=True

	def getVidas(self):
		return self.vidas
	
	def setVidas(self,v):
		self.vidas=v
	
	def Ganar(self,pal):
		if pal==self.getFrase():
			return True

		else:
			self.vidas=self.vidas-1
			return False

	def j1S(self):
		self.j1.sumaPuntos()

	def j2S(self):
		self.j2.sumaPuntos()
		#2857


