from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastro
import ControleDeFinancas as CF

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
		self.e2 = Entry(self.f2, show='*')
		self.e1.pack(side=RIGHT)
		self.e2.pack(side=RIGHT)
		
		self.l1 = Label(self.f1, text='Usuário: ')
		self.l2 = Label(self.f2, text='Senha: ')
		self.l1.pack()
		self.l2.pack()
		
		self.b1 = Button(self.f3, text='Cadastrar')
		self.b2 = Button(self.f3, text='Entrar')
		self.b1.bind("<ButtonRelease-1>", self.cadastrar)
		self.b2.bind("<ButtonRelease-1>", self.entrar)
		self.b1.pack(side=LEFT)
		self.b2.pack()
		
	def cadastrar(self, event):
		self.telaCadastro = TelaCadastro.TelaCadastro(self)
		self.telaCadastro.deiconify()
		self.withdraw()		
		
	def entrar(self, event):
		try:
			arq1 = open("UsuáriosCadastrados.txt", "rb")
			try:
				self.users = load(arq1)
			except IOError as e:
				print(e)
			finally:
				arq1.close()
		except:
			arq2 = open("UsuáriosCadastrados.txt", "wb")
			try:
				dump([], arq2)
			except IOError as e:
				print(e)
			finally:
				arq2.close()
				self.users = []
		varDeUser = 0
		varDeSenha = False
		if len(self.users) > 0:
			for i in range(len(self.users)):
				if self.e1.get() == self.users[i].getNome() and self.e2.get() == self.users[i].getSenha():
					
					self.iUser = i
					self.telaControle = CF.TelaControle(self)
					
					self.telaControle.deiconify()
					self.withdraw()

				elif self.e1.get() == self.users[i].getNome() and self.e2.get() != self.users[i].getSenha():
					varDeSenha = True
				else:
					varDeUser += 1
		try:
			if varDeSenha:
				raise ValueError
			elif varDeUser - len(self.users) == 0:
				raise IndexError
		except IndexError:
			r = messagebox.askyesno("ERRO!","O usuário ainda não foi cadastrado.\n\nQuer ir para o cadastro?")
			if r:
				self.cadastrar(event)
		except ValueError:
			messagebox.showerror("ERRO!","Por favor,\nVerifique se a senha está correta.")
			
if __name__ == '__main__':
	telaLogin = TelaLogin()
	telaLogin.mainloop()