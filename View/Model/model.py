from tkinter import messagebox
from datetime import *
	
class Usuario:
	def __init__(self, nome, senha):
		self.__nome = nome
		self.__senha = senha
		self.__lComprados = []
		self.__lRendas = []
		
		for i in range(10):
			if  str(i) in self.__nome:
				raise TypeError
		
	def getNome(self):
		return self.__nome
		
	def setNome(self, novoNome):
		self.__nome = novoNome
		
	def getSenha(self):
		return self.__senha
		
	def setSenha(self, novaSenha):
		self.__senha = novaSenha
		
	def getlComprados(self):
		return self.__lComprados
		
	def setlComprados(self, novolComprados):
		self.__lComprados = novolComprados
		
	def adCompra(self, novaCompra):
		self.__lComprados.append(novaCompra)
		return messagebox.showinfo("Sucesso!","Item registrado no\nseu controle de finanças.")
		
	def getlRendas(self):
		return self.__lRendas
		
	def setlRendas(self, novalRendas):
		self.__lRendas = novalRendas
		
	def adRenda(self, novaRenda):
		self.__lRendas.append(novaRenda)
		return messagebox.showinfo("Sucesso!","Renda registrada no\nseu controle de finanças.")
		
	def saldo(self):
		valorRenda = 0
		if len(self.__lRendas) > 0:
			for iV in range(len(self.__lRendas)):
				valorRenda += self.__lRendas[iV].getValor()
			
		precoCompra = 0
		if len(self.__lComprados) > 0:
			for iP in range(len(self.__lComprados)):
				precoCompra += self.__lComprados[iP].getPreco()
		return valorRenda - precoCompra
		
	def __str__(self):
		lNomesComprados = []
		for i in range(len(self.__lComprados)):
			lNomesComprados.append(self.__lComprados[i].getNome())
		strComprados = str.join(" e ", lNomesComprados).replace(" e ", ", ", len(lNomesComprados) - 2)
		
		lNomesRendas = []
		for i in range(len(self.__lRendas)):
			lNomesRendas.append(self.__lRendas[i].getNome())
		strRendas = str.join(" e ", lNomesRendas).replace(" e ", ", ", len(lNomesRendas) - 2)
		
		return "\nNome: {}\nSenha: {}\nLista de comprados: {}\nLista de rendas: {}".format(self.__nome, self.__senha, strComprados, strRendas)

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