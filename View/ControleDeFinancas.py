# Parte responsável pela importação dos módulos
from tkinter import *
from pickle import *
from tkinter import messagebox
import TelaCadastrandoItem as TCI

from matplotlib.pyplot import plot,show
from numpy import arange

class TelaControle(Tk):
    '''Classe que define a Janela de Finanças'''
    def __init__(self, telaLogin):
        '''Método construtor da classe TelaControle'''
        super(TelaControle, self).__init__()

        # Abertura do arquivo de texto no modo de leitura binária
        arq1 = open("UsuáriosCadastrados.txt", "rb")

        # Controle de erro para um erro de entrada e saída de dados
        try:
            self.listaUsers = load(arq1)  # Deserialização do texto UsuáriosCadastrados
        except IOError as e:
            print(e)  # Visualização do motivo do erro de entrada e saída
        finally:
            # Fechamento do arquivo de texto
            arq1.close()

        self.telaLogin = telaLogin # Fechamento do arquivo de texto

        # Configuração dos frames da janela de finanças
        self.title("Controle De Finanças")
        self.l0 = Label(self)
        self.l0.pack()
        self.f1 = Frame(self)
        self.f1.pack()
        self.f2 = Frame(self)
        self.f2.pack()

        # Configuração do Listbox e dos scrollbars
        self.scrollbarY = Scrollbar(self.f1, orient=VERTICAL)
        self.scrollbarY.pack(side=RIGHT, fill=Y)
        self.lb1 = Listbox(self.f1, yscrollcommand=self.scrollbarY.set,height=0, width=0)
        self.lb1.pack(side=RIGHT)
        self.scrollbarY.config(command=self.lb1.yview)

        # Inicialização da função escreverListBox
        self.escreverListBox()

        # Configuração dos botões da janela para limpar e cadastrar itens e gerar um relatório
        self.b1 = Button(self.f2, text='Cadastar Item')
        self.b2 = Button(self.f2, text='Limpar')
        self.b3 = Button(self.f2, text='Gerar Relatório')
        self.b1.pack(side=RIGHT)
        self.b2.pack(side=RIGHT)
        self.b3.pack(side=RIGHT)
        self.b1.bind("<ButtonRelease-1>", self.cadastrarItem)
        self.b2.bind("<ButtonRelease-1>", self.limpar)
        self.b3.bind("<ButtonRelease-1>", self.gerarRelatorio)

    def gerarRelatorio(self, event):
        '''Função utilizada para gerar um relatório em formato de gráfico'''
        user = self.listaUsers[self.telaLogin.iUser]
        
        # Parte relacionada aos itens comprados pelo usuário
        if len(user.getlComprados()) > 0:
            xComprados = arange(len(user.getlComprados()))
            yComprados = [item.getPreco() for item in user.getlComprados()]
            plot(xComprados, yComprados)
            
            meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
            123456789
        # Parte relacionada às rendas do usuário
        if len(user.getlRendas()) > 0:
            xComprados = arange(len(user.getlRendas()))
            yComprados = [item.getValor() for item in user.getlRendas()]
            plot(xComprados, yComprados)              
            show()

    def escreverListBox(self):
        '''Criação da função usada para inserir as informações sobre a renda e os itens comprados pelo usuário, além de mostrar o saldo'''
        self.l0.config(text='Total: R$ %.2f' % self.listaUsers[self.telaLogin.iUser].saldo())
        self.lb1.delete(0, END)
        for i in range(len(self.listaUsers[self.telaLogin.iUser].getlComprados())):
            self.lb1.insert(END, self.listaUsers[self.telaLogin.iUser].getlComprados()[i])

        for i in range(len(self.listaUsers[self.telaLogin.iUser].getlRendas())):
            self.lb1.insert(END, self.listaUsers[self.telaLogin.iUser].getlRendas()[i])


    def cadastrarItem(self, event):
        '''Criação do evento usado para ampliar a janela de cadastro de itens e decrescer a janela de finanças'''
        self.telaCI = TCI.TelaCadastrandoItem(self)
        self.telaCI.deiconify()
        self.withdraw()

    def limpar(self, event):
        '''Criação do evento usado para limpar todos os registros de renda e itens comprados pelo usuário'''
        r = messagebox.askyesno("ATENÇÃO!", "Deseja limpar todos os seus registros?")
        if r:
            self.listaUsers[self.telaLogin.iUser].setlRendas([])
            self.listaUsers[self.telaLogin.iUser].setlComprados([])
            self.escreverListBox()
            arq2 = open("UsuáriosCadastrados.txt", "wb")
            try:
                dump(self.listaUsers, arq2)
            except IOError as e:
                print(e)
            finally:
                arq2.close()