from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastrandoRenda as TCR
import model

class TelaCadastrandoItem(Tk):
	def __init__(self, telaControle):
		super(TelaCadastrandoItem, self).__init__()
		
		self.telaControle = telaControle
		
		self.title("Cadastro de Item")
		self.l0 = Label(self, text='Cadastro de Item')
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
		
		self.l1 = Label(self.f1, text='Nome do item: ')
		self.l2 = Label(self.f2, text='Preço: ')
		self.l3 = Label(self.f3, text='Local de compra: ')
		self.l4 = Label(self.f4, text='Data: ')
		self.l1.pack()
		self.l2.pack()
		self.l3.pack()
		self.l4.pack()
		
		self.b1 = Button(self, text='Salvar')
		self.b1.bind("<ButtonRelease-1>", self.salvar)
		self.b1.pack()
		
		self.v = StringVar()
		self.v.set(1)
		
		self.rb1 = Radiobutton(self, text="Um", variable=self.v, value=1)
		self.rb1.pack(anchor=W)
		self.rb1.bind("<ButtonRelease-1>", self.mudarTela)
		
		self.rb2 = Radiobutton(self, text="Dois", variable=self.v, value=2)
		self.rb2.pack(anchor=W)
		self.rb2.bind("<ButtonRelease-1>", self.mudarTela)
		
	def mudarTela(self, event):
		TCI.TelaCadastrandoRenda(self).deiconify()
		self.withdraw()
		
	def salvar(self, event):
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			listaUsers = load(arq1)
		except IOError as e:
			print(e)
		finally:
			arq1.close()
		try:
			listaUsers[self.telaControle.telaLogin.iUser].adCompra(model.ItemDeCompra(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()))
			
			arq2 = open("UsuáriosCadastrados.txt", "wb")
			try:
				dump(listaUsers, arq2)
			except IOError as e:
				print(e)
			finally:
				arq2.close()
			
			self.telaControle.l0.config(text='Total: R$ %f'%listaUsers[self.telaControle.telaLogin.iUser].saldo())
			self.telaControle.deiconify()
			self.withdraw()
		except TypeError:
			messagebox.showerror("ERRO!","Não pode números no nome.")
		except ValueError:
			messagebox.showerror("ERRO!","Em preço só são válidos números.")
