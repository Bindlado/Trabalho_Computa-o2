from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastrandoRenda as TCR
from Model import model

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
		self.f0.pack()
		self.f1.pack(side=RIGHT)
		self.f2.pack(side=LEFT)
		
		self.e1 = Entry(self.f1, textvariable='(ex: Sorvete)')
		self.e2 = Entry(self.f1, textvariable='(ex: 11.99)')
		self.e3 = Entry(self.f1, textvariable='(ex: Mercado)')
		self.e1.pack(anchor='w')
		self.e2.pack(anchor='w')
		self.e3.pack(anchor='w')
		
		self.f3 = Frame(self.f1)
		self.f3.pack(anchor='w')
		
		self.e31 = Entry(self.f3, width=0, textvariable='DD')
		self.e32 = Entry(self.f3, width=0, textvariable='MM')
		self.e33 = Entry(self.f3, width=0, textvariable='AAAA')
		self.e34 = Entry(self.f3, width=0, textvariable='hh')
		self.e35 = Entry(self.f3, width=0, textvariable='mm')
		
		self.l31 = Label(self.f3, text="/")
		self.l32 = Label(self.f3, text="/")
		self.l33 = Label(self.f3, text=" ")
		self.l34 = Label(self.f3, text=":")
		
		self.e31.pack(side=LEFT)
		self.l31.pack(side=LEFT)
		self.e32.pack(side=LEFT)
		self.l32.pack(side=LEFT)
		self.e33.pack(side=LEFT)
		self.l33.pack(side=LEFT)
		self.e34.pack(side=LEFT)
		self.l34.pack(side=LEFT)
		self.e35.pack(side=LEFT)
		
		self.defEntrada(self.e1)
		self.defEntrada(self.e2)
		self.defEntrada(self.e3)
		self.defEntrada(self.e31)
		self.defEntrada(self.e32)
		self.defEntrada(self.e33)
		self.defEntrada(self.e34)
		self.defEntrada(self.e35)
		
		self.e31.bind('<KeyRelease>', self.limitar)
		self.e32.bind('<KeyRelease>', self.limitar)
		self.e33.bind('<KeyRelease>', self.limitar)
		self.e34.bind('<KeyRelease>', self.limitar)
		self.e35.bind('<KeyRelease>', self.limitar)
		
		self.l1 = Label(self.f2, text='Nome da compra: ')
		self.l2 = Label(self.f2, text='Preço(R$): ')
		self.l3 = Label(self.f2, text='Local de compra: ')
		self.l4 = Label(self.f2, text='Data: ')
		self.l1.pack(anchor='e')
		self.l2.pack(anchor='e')
		self.l3.pack(anchor='e')
		self.l4.pack(anchor='e')
		
		self.f4 = Frame(self)
		self.f4.pack()
		
		self.b1 = Button(self.f4, text='Salvar')
		self.b1.bind('<ButtonRelease-1>', self.salvar)
		self.b1.pack(side=RIGHT)
		self.b2 = Button(self.f4, text='Voltar')
		self.b2.pack(side=LEFT)
		self.b2.bind('<ButtonRelease-1>', self.voltar)
		
		self.rb1 = Radiobutton(self, text="Compra", value=1)
		self.rb1.pack(anchor=W)
		self.rb1.bind("<Button-1>", self.mudarTela)
		self.rb1.select()
		
		self.rb2 = Radiobutton(self, text="Renda", value=2)
		self.rb2.pack(anchor=W)
		self.rb2.bind("<Button-1>", self.mudarTela)
		
	def voltar(self, event):
		self.telaControle.deiconify()
		self.withdraw()
		
	def defEntrada(self, entrada):
		entrada.delete(0, END)
		entrada.config(foreground='darkgray')
		entrada.insert(0, entrada.cget('textvariable'))
		entrada.bind('<FocusIn>', self.focado)
		entrada.bind('<FocusOut>', self.desfocado)
		
	def focado(self, event):
		if event.widget.get() == event.widget.cget('textvariable'):
			event.widget.delete(0, END)
			event.widget.config(foreground='black')		
		
	def limitar(self, event):
		if len(event.widget.get()) > len(event.widget.cget('textvariable')):
			event.widget.delete(event.widget.index(INSERT)-1, event.widget.index(INSERT))
		if len(event.widget.get()) > 0 and event.widget.get()[event.widget.index(INSERT)-1] not in '0123456789':
			event.widget.delete(event.widget.index(INSERT)-1, event.widget.index(INSERT))
		
	def desfocado(self, event):
		if event.widget.get() == '':
			event.widget.insert(0, event.widget.cget('textvariable'))
			event.widget.config(foreground='darkgray')
		
	def mudarTela(self, event):
		self.l1.focus()
		if event.widget.cget('value') == 2:
			self.l1.config(text='Nome da renda: ')
			self.l2.config(text='Valor(R$): ')
			self.l3.config(text='Local da renda: ')
			self.e1.config(textvariable='(ex: Conserto de PC)')
			self.e2.config(textvariable='(ex: 119.99)')
			self.e3.config(textvariable='(ex: Trabalho)')
			self.defEntrada(self.e1)
			self.defEntrada(self.e2)
			self.defEntrada(self.e3)
		
		if event.widget.cget('value') == 1:
			self.l1.config(text='Nome da compra: ')
			self.l2.config(text='Preço(R$): ')
			self.l3.config(text='Local da compra: ')
			self.e1.config(textvariable='(ex: Sorvete)')
			self.e2.config(textvariable='(ex: 19.99)')
			self.e3.config(textvariable='(ex: Mercado)')
			self.defEntrada(self.e1)
			self.defEntrada(self.e2)
			self.defEntrada(self.e3)
			
	def salvar(self, event):
		arq1 = open("UsuáriosCadastrados.txt", "rb")
		try:
			listaUsers = load(arq1)
		except IOError as e:
			print(e)
		finally:
			arq1.close()
		try:
			if self.e1.get() != self.e1.cget('textvariable') and self.e2.get() != self.e2.cget('textvariable') and self.e3.get() != self.e3.cget('textvariable'):
				if self.e1.cget('textvariable') == '(ex: Sorvete)':
					listaUsers[self.telaControle.telaLogin.iUser].adCompra(model.ItemDeCompra(self.e1.get(), self.e2.get(), self.e3.get(), '%s/%s/%s %s:%s'%(self.e31.get(), self.e32.get(), self.e33.get(), self.e34.get(), self.e35.get())))
				if self.e1.cget('textvariable') == '(ex: Conserto de PC)':
					listaUsers[self.telaControle.telaLogin.iUser].adRenda(model.Renda(self.e1.get(), self.e2.get(), self.e3.get(), '%s/%s/%s %s:%s'%(self.e31.get(), self.e32.get(), self.e33.get(), self.e34.get(), self.e35.get())))
					
				arq2 = open("UsuáriosCadastrados.txt", "wb")
				try:
					dump(listaUsers, arq2)
				except IOError as e:
					print(e)
				finally:
					arq2.close()
			
				self.telaControle.listaUsers = listaUsers
				self.telaControle.escreverListBox()
				self.telaControle.deiconify()
				self.withdraw()
			
		except TypeError:
			messagebox.showerror("ERRO!","Não pode números no nome.")
		except ValueError:
			try:
				float(self.e2.get())
			except:
				messagebox.showerror("ERRO!","Em %s só são válidos números."%self.l2.cget('text').replace('(R$):', ''))
			try:
				datetime.strptime('%s/%s/%s %s:%s'%(self.e31.get(), self.e32.get(), self.e33.get(), self.e34.get(), self.e35.get()), '%d/%m/%Y %H:%M')
			except:
				messagebox.showerror("ERRO!","Verifique se os valores para\ndata estão corretos.")