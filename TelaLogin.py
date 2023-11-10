from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastro

class Usuario:
	def __init__(self, nome, senha):
		self.__nome = nome
		self.__senha = senha
		self.__lComprados = []
		self.__lRendas = []
		
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
		
	def adComprados(self, novaCompra):
		self.__lComprados.append(novaCompra)
		
	def getlRendas(self):
		return self.__lRendas
		
	def adRendas(self, novaRenda):
		self.__lRendas.append(novaRenda)
		
	def __str__(self):
		lNomesComprados = []
		for i in range(len(self.__lComprados)):
			lNomes.append(self.__lComprados[i].getNome())
		strComprados = str.join(" e ", lNomesComprados).replace(" e ", ", ", len(lNomesComprados) - 2)
		
		lNomesRendas = []
		for i in range(len(self.__lRendas)):
			lNomesRendas.append(self.__lRendas[i].getNome())
		strRendas = str.join(" e ", lNomesRendas).replace(" e ", ", ", len(lNomesRendas) - 2)
		
		return "\nNome: {}\nSenha: {}\nLista de comprados: {}\nLista de rendas: {}".format(self.__nome, self.__senha, strComprados, strRendas)

class ItemDeCompra:
	def __init__(self, nome, preco, dataCompra, localCompra):
		self.__nome = nome
		self.__preco = preco
		self.dataCompra = dataCompra
		self.localCompra = localCompra
		
	def getNome(self):
		return self.__nome
		
	def setNome(self, novoNome):
		self.__nome = novoNome
		
	def getPreco(self):
		return self.__preco
		
	def setPreco(self, novoPreco):
		self.__preco = novoPreco

class Renda:
	def __init__(self, nome, valor, dataRecebimento, fonte):
		self.__nome = nome
		self.__valor = valor
		self.dataRecebimento = dataRecebimento
		self.fonte = fonte
		
	def getNome(self):
		return self.__nome
		
	def setNome(self, novoNome):
		self.__nome = novoNome
		
	def getValor(self):
		return self.__valor
		
	def setValor(self, novoValor):
		self.__valor = novoValor

class TelaLogin(Tk, object):
	def __init__(self):
		super(TelaLogin, self).__init__()
		
		self.title("Controle de Finanças")
		self.l0 = Label(self, text='Controle de Finanças')
		self.l0.pack()
		
		self.f0 = Frame(self)
		self.f1 = Frame(self.f0)
		self.f2 = Frame(self.f0)
		self.f3 = Frame(self)
		self.f0.pack()
		self.f1.pack(anchor='e')
		self.f2.pack(anchor='e')
		self.f3.pack()
		
		self.e1 = Entry(self.f1)
		self.e2 = Entry(self.f2)
		self.e1.pack(side=RIGHT)
		self.e2.pack(side=RIGHT)
		
		self.l1 = Label(self.f1, text='Usuário: ')
		self.l2 = Label(self.f2, text='Senha: ')
		self.l1.pack()
		self.l2.pack()
		
		self.b1 = Button(self.f3, text='Cadastrar')
		self.b2 = Button(self.f3, text='Entrar')
		self.b1.bind('<Button-1>', self.cadastrar)
		self.b2.bind('<Button-1>', self.entrar)
		self.b1.pack(side=LEFT)
		self.b2.pack()
		
	def cadastrar(self, event):
		self.telaCadastro = TelaCadastro.TelaCadastro(self)
		self.telaCadastro.deiconify()
		self.withdraw()		
		
	def entrar(self, event):
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			self.users = load(arq1)
		except IOError as e:
			print(e)
		finally:
			arq1.close()
		if self.users == list(self.users):
			for i in range(len(self.users)):
				if self.e1.get() == self.users[i].getNome() and self.e2.get() == self.users[i].getSenha():
					self.l4 = Label(self, text=str(self.users))
					self.l4.pack()
		
if __name__ == '__main__':
	telaLogin = TelaLogin()
	telaLogin.mainloop()