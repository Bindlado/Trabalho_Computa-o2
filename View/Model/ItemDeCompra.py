from tkinter import messagebox
from datetime import *
	
class ItemDeCompra:
	def __init__(self, nome, preco, localCompra, dataCompra):
		self.__nome = nome
		self.__preco = float(preco)
		self.localCompra = localCompra
		self.dataCompra = datetime.strptime(dataCompra, '%d/%m/%Y %H:%M')
		
		for i in range(10):
			if  str(i) in self.__nome:
				raise TypeError
		
	def getNome(self):
		return self.__nome
		
	def setNome(self, novoNome):
		self.__nome = novoNome
		
	def getPreco(self):
		return self.__preco
		
	def setPreco(self, novoPreco):
		self.__preco = novoPreco
		
	def __str__(self):
		return "{} - {} - {} - {}".format(self.dataCompra.strftime('%d/%m/%Y %H:%M'), self.__nome, self.localCompra, self.__preco)