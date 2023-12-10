from matplotlib.pyplot import *
from numpy import *
from tkinter import *

def mostrarGrafico(user):
	if len(user.getlComprados()) > 0:
		xComprados = arange(len(user.getlComprados))
		yComprados = user.getlComprados[xComprados].getPreco()
		plot(xComprados, yComprados)
		show()

# Gera um gráfico que compõe o fluxo de caixa do usuário
    def gerarRelatorio(event, self):
        user = self.listaUsers(self.telaLogin.IUser)
        if len(user.getlComprados()) > 0:
            xComprados = arange(len(user.getlComprados))
            yComprados = user.getlComprados[xComprados].getPreco()
            plot(xComprados, yComprados)
            show()