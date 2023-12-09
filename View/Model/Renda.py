from tkinter import messagebox
from datetime import *

class Renda:
	def __init__(self, nome, valor, fonte, dataRecebimento):
		self.__nome = nome
		self.__valor = float(valor)
		self.fonte = fonte
		self.dataRecebimento = datetime.strptime(dataRecebimento, '%d/%m/%Y %H:%M')
		
		for i in range(10):
			if  str(i) in self.__nome:
				raise TypeError
		
	def getNome(self):
		return self.__nome
		
	def setNome(self, novoNome):
		self.__nome = novoNome
		
	def getValor(self):
		return self.__valor
		
	def setValor(self, novoValor):
		self.__valor = novoValor
		
	def __str__(self):
		return "{} - {} - {} - {}".format(self.dataRecebimento.strftime('%d/%m/%Y %H:%M'), self.__nome, self.fonte, self.__valor)