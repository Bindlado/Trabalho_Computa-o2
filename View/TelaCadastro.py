# Parte responsável pela importação dos módulos
from tkinter import *
from pickle import *
from tkinter import messagebox
from Model import Usuario as User

class TelaCadastro(Tk):
    '''Classe que define a janela de cadastro'''
    def __init__(self, telaLogin):
        '''Método construtor da classe TelaControle'''
        super(TelaCadastro, self).__init__()

        self.telaLogin = telaLogin  # Usado para não precisar importar o telaLogin

        # Configuração dos frames da janela de cadastro
        self.title("Cadastro de Usuário")
        self.l0 = Label(self, text='Cadastro de Usuário')
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
        self.f4.pack()

        # Configuração dos entries
        self.e1 = Entry(self.f1)
        self.e2 = Entry(self.f2, show='*')
        self.e3 = Entry(self.f3, show='*')
        self.e1.pack(side=RIGHT)
        self.e2.pack(side=RIGHT)
        self.e3.pack(side=RIGHT)

        # Configuração dos labels Usuário, Senha e Confirmar Senha para o e1, e2 e e3, respectivamente
        self.l1 = Label(self.f1, text='Usuário: ')
        self.l2 = Label(self.f2, text='Senha: ')
        self.l3 = Label(self.f3, text='Confirmar Senha: ')
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()

        # Configuração dos botões de salvar e voltar para janela inicial
        self.b1 = Button(self.f4, text='Salvar')
        self.b1.bind('<ButtonRelease-1>', self.salvar)
        self.b1.pack(side=RIGHT)
        self.b2 = Button(self.f4, text='Voltar')
        self.b2.pack(side=LEFT)
        self.b2.bind('<ButtonRelease-1>', self.voltar)

        arq1 = open("UsuáriosCadastrados.txt", "rb")  # Abertura do arquivo de texto no modo de leitura binária

        # Controle de erros para um erro de entrada e saída de dados
        try:
            self.listaUsers = load(arq1)  # Deserialização do texto UsuáriosCadastrados

        except IOError as e:
            print(e)  # Visualização do motivo do erro de entrada e saída

        finally:
            arq1.close()  # Fechamento do arquivo de texto

        if self.listaUsers != list(self.listaUsers):
            self.listaUsers = []

    def voltar(self, event):
        '''Evento usado para ampliar a tela inicial e decrescer a tela de cadastro'''
        self.telaLogin.deiconify()
        self.withdraw()

    def salvar(self, event):
        '''Evento usado para verificar a unicidade (ele é único) e veracidade (é verdadeiro) do usuário e senha e salva-los'''
        varDeNome = False
        for i in range(len(self.listaUsers)):
            if len(self.listaUsers) > 0 and self.listaUsers[i].getNome() == self.e1.get():
                varDeNome = True

        if self.e2.get() == self.e3.get() and varDeNome == False and len(self.e1.get().replace(' ', '')) > 2:
            try:
                self.listaUsers.append(User.Usuario(self.e1.get(), self.e3.get()))
                arq2 = open("UsuáriosCadastrados.txt", "wb")
                try:
                    dump(self.listaUsers, arq2)
                except IOError as e:
                    print(e)
                finally:
                    arq2.close()
                messagebox.showinfo("Sucesso!", "Usuário %s foi cadastrado." % self.e1.get())
                self.telaLogin.deiconify()
                self.withdraw()
            except:
                messagebox.showerror("ERRO!", "Não pode números no nome.")
        if self.e2.get() != self.e3.get():
            messagebox.showerror("ERRO!", "Por favor,\nVerifique se as senhas estão corretas.")
        if varDeNome:
            messagebox.showerror("ERRO!", "O nome de usuário já foi cadastrado\nPor favor, tente outro nome.")
