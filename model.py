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
		
	def adCompra(self, novaCompra):
		self.__lComprados.append(novaCompra)
		return messagebox.showinfo("Sucesso!","Item cadastrado no\nseu controle de finanças.")
		
	def getlRendas(self):
		return self.__lRendas
		
	def adRenda(self, novaRenda):
		self.__lRendas.append(novaRenda)
		showinfo("Sucesso!","Renda cadastrada no\nseu controle de finanças.")
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
	def __init__(self, nome, preco, dataCompra, localCompra):
		self.__nome = nome
		self.__preco = float(preco)
		self.dataCompra = dataCompra
		self.localCompra = localCompra
		
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
		return "Nome: {} - Preço: {} - Data da compra: {} - Local da compra: {}".format(self.__nome, self.__preco, self.dataCompra, self.localCompra)


class Renda:
	def __init__(self, nome, valor, dataRecebimento, fonte):
		self.__nome = nome
		self.__valor = float(valor)
		self.dataRecebimento = dataRecebimento
		self.fonte = fonte
		
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
		return "Nome: {} - Valor: {} - Data: {} - Fonte: {}".format(self.__nome, self.__valor, self.__dataRecebimento, self.fonte)