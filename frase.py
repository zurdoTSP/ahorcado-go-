class Frase():
	def __init__(self,frase):
		self.frase=frase
		self.incognita=self.convertir()

	def convertir(self):
		cad="-"
		cad=cad*len(self.frase)
		return list(cad)

	def getFrase(self):
		return self.frase
	
	def getIncognita(self):
		return self.incognita

	def setNueva(self,frase):
		self.frase=frase
		self.incognita=self.convertir()

	def sustituir(self,x):
		resultado=False
		
		t=0
		for y in self.frase:
			if x==y:
				self.incognita[t]=x
				resultado=True
			t=t+1
		return resultado


