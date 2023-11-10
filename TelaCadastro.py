from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaLogin

class TelaCadastro(Tk):
	def __init__(self, telaLogin):
		super(TelaCadastro, self).__init__()
		
		self.telaLogin = telaLogin
		
		self.title("Cadastro de Usuário")
		self.l0 = Label(self, text='Cadastro de Usuário')
		self.l0.pack()
		
		self.f0 = Frame(self)
		self.f1 = Frame(self.f0)
		self.f2 = Frame(self.f0)
		self.f3 = Frame(self.f0)
		self.f0.pack()
		self.f1.pack(anchor='e')
		self.f2.pack(anchor='e')
		self.f3.pack(anchor='e')
		
		self.e1 = Entry(self.f1)
		self.e2 = Entry(self.f2)
		self.e3 = Entry(self.f3)
		self.e1.pack(side=RIGHT)
		self.e2.pack(side=RIGHT)
		self.e3.pack(side=RIGHT)
		
		self.l1 = Label(self.f1, text='Usuário: ')
		self.l2 = Label(self.f2, text='Senha: ')
		self.l3 = Label(self.f3, text='Confirmar Senha: ')
		self.l1.pack()
		self.l2.pack()
		self.l3.pack()
		
		self.b1 = Button(self, text='Salvar')
		self.b1.bind('<Button-1>', self.salvar)
		self.b1.pack()
		
	def salvar(self, event):
		
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			listaUsers = load(arq1)
		except IOEroor as e:
			print(e)
		finally:
			arq1.close()
		if listaUsers != list(listaUsers):
			listaUsers = []
		listaUsers.append(TelaLogin.Usuario(self.e1.get(), self.e3.get()))
		
		arq2 = open("UsuáriosCadastrados.txt", "wb")
		try:
			dump(listaUsers, arq2)
		except IOEroor as e:
			print(e)
		finally:
			arq1.close()
			messagebox.showinfo("Sucesso!","Funcionário %s com matrícula %s registrado." % (self.e1.get(), self.e3.get()))	      
			self.telaLogin.deiconify()
			self.withdraw()