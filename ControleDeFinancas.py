from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastrandoItem as TCI

class TelaControle(Tk):
	def __init__(self, telaLogin):
		super(TelaControle, self).__init__()
		
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			self.listaUsers = load(arq1)
		except IOError as e:
			print(e)
		finally:
			arq1.close()
		
		self.telaLogin = telaLogin
		
		self.title("Controle De Finanças")
		self.l0 = Label(self, text='Total: R$ %.2f'%self.listaUsers[self.telaLogin.iUser].saldo())
		self.l0.pack()
		self.f1 = Frame(self)
		self.f1.pack()
		self.f2 = Frame(self)
		self.f2.pack()
		
		self.scrollbarY = Scrollbar(self.f1, orient = VERTICAL)
		self.scrollbarY.pack(side=RIGHT, fill=Y)
		self.lb1 = Listbox(self.f1, yscrollcommand=self.scrollbarY.set,)
		self.lb1.pack(side=RIGHT)
		self.scrollbarY.config(command=self.lb1.yview)
		
		for i in range(len(self.listaUsers[self.telaLogin.iUser].getlComprados())):
			self.lb1.insert(END, self.listaUsers[self.telaLogin.iUser].getlComprados()[i])
			
		for i in range(len(self.listaUsers[self.telaLogin.iUser].getlRendas())):
			self.lb1.insert(END, self.listaUsers[self.telaLogin.iUser].getlRendas()[i])
		
		self.b1 = Button(self.f2, text='Cadastar Item')
		self.b2 = Button(self.f2, text='Limpar')
		self.b3 = Button(self.f2, text='Gerar Relatório')
		self.b1.pack(side=RIGHT)
		self.b2.pack(side=RIGHT)
		self.b3.pack(side=RIGHT)
		self.b1.bind("<ButtonRelease-1>", self.cadastrarItem)
		self.b2.bind("<Button-1>", )
		self.b3.bind("<Button-1>", )
		
	def cadastrarItem(self, event):
		self.telaCI = TCI.TelaCadastrandoItem(self)
		self.telaCI.deiconify()
		self.withdraw()