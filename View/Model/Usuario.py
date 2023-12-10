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
