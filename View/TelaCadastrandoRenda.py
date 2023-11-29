from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaLogin as TL
import TelaCadastrandoItem as TCI
import model

class TelaCadastrandoRenda(Tk):
	def __init__(self, telaItem):
		super(TelaCadastrandoRenda, self).__init__()
		
		self.telaItem = telaItem
		self.telaControle = self.telaItem.telaControle
		
		self.title("Cadastro de Renda")
		self.l0 = Label(self, text='Cadastro de Renda')
		self.l0.pack()
		
		self.f0 = Frame(self)
		self.f1 = Frame(self.f0)
		self.f2 = Frame(self.f0)
		self.f3 = Frame(self.f0)
		self.f4 = Frame(self.f0)
		self.f0.pack()
		self.f1.pack(anchor='e')
		self.f2.pack(anchor='e')
		self.f3.pack(anchor='e')
		self.f4.pack(anchor='e')
		
		self.e1 = Entry(self.f1)
		self.e2 = Entry(self.f2)
		self.e3 = Entry(self.f3)
		self.e4 = Entry(self.f4)
		self.e1.pack(side=RIGHT)
		self.e2.pack(side=RIGHT)
		self.e3.pack(side=RIGHT)
		self.e4.pack(side=RIGHT)
		
		self.l1 = Label(self.f1, text='Nome da renda: ')
		self.l2 = Label(self.f2, text='Valor: ')
		self.l3 = Label(self.f3, text='Fonte: ')
		self.l4 = Label(self.f4, text='Data: ')
		self.l1.pack()
		self.l2.pack()
		self.l3.pack()
		self.l4.pack()
		
		self.b1 = Button(self, text='Salvar')
		self.b1.bind('<Button-1>', self.salvar)
		self.b1.pack()
		
		self.v = StringVar()
		
		self.rb1 = Radiobutton(self, text="Um", variable=self.v, value=1)
		self.rb1.pack(anchor=W)
		self.rb1.bind("<Button-1>", self.mudarTela)
		
		self.rb2 = Radiobutton(self, text="Dois", variable=self.v, value=2)
		self.rb2.pack(anchor=W)
		self.rb2.bind("<ButtonRelease-1>", self.mudarTela)
		
	def mudarTela(self, event):
		TCI.TelaCadastrandoItem(self.telaControle).deiconify()
		self.withdraw()
		
	def salvar(self, event):
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			listaUsers = load(arq1)
		except IOError as e:
			print(e)
		finally:
			arq1.close()
		listaUsers[TelaLogin.TelaLogin.iUser].adRenda(TelaLogin.ItemDeCompra(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()))
		
		arq2 = open("UsuáriosCadastrados.txt", "wb")
		try:
			dump(listaUsers, arq2)
		except IOError as e:
			print(e)
		finally:
			arq2.close()
		
		self.telaItem.telaControle.deiconify()
		self.withdraw()