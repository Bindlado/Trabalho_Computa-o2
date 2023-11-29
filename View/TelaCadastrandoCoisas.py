from tkinter import *
from pickle import *
from tkinter import messagebox

class TelaCadastrandoItem(Tk):
	def __init__(self):
		super(TelaCadastrandoItem, self).__init__()
		
		self.telaLogin = 2
		
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
		self.b1.bind('<Button-1>', self.salvar)
		self.b1.pack()
		
	def salvar(self):
		self.b1 = self.b1
		
j = TelaCadastrandoItem()
j.mainloop()