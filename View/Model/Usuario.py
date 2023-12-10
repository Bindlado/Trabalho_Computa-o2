# Parte responsável pelo importe dos módulos
from tkinter import messagebox
from datetime import *

class Usuario:
    """Classe que representa o usuário responsável por manipular o fluxo de caixa"""

    def __init__(self, nome, senha):
        """Método construtor que inicializa um objeto de usuário com um nome, senha e listas vazias para compras e rendas"""
        self.__nome = nome
        self.__senha = senha
        self.__lComprados = []
        self.__lRendas = []

        for i in range(10):
            if str(i) in self.__nome:
                raise TypeError

    def getNome(self):
        """Retorna o nome do usuário"""
        return self.__nome

    def setNome(self, novoNome):
        """Define um novo nome para o usuário"""
        self.__nome = novoNome

    def getSenha(self):
        """Retorna a senha do usuário"""
        return self.__senha

    def setSenha(self, novaSenha):
        """Define uma nova senha para o usuário"""
        self.__senha = novaSenha

    def getlComprados(self):
        """Retorna a lista de compras do usuário"""
        return self.__lComprados

    def setlComprados(self, novolComprados):
        """Define uma nova lista de compras para o usuário"""
        self.__lComprados = novolComprados

    def adCompra(self, novaCompra):
        """Adiciona uma nova compra à lista de compras do usuário"""
        self.__lComprados.append(novaCompra)
        return messagebox.showinfo("Sucesso!", "Item registrado no\nseu controle de finanças.")

    def getlRendas(self):
        """Retorna a lista de rendas do usuário"""
        return self.__lRendas

    def setlRendas(self, novalRendas):
        """Define uma nova lista de rendas para o usuário"""
        self.__lRendas = novalRendas

    def adRenda(self, novaRenda):
        """Adiciona uma nova renda à lista de rendas do usuário"""
        self.__lRendas.append(novaRenda)
        return messagebox.showinfo("Sucesso!", "Renda registrada no\nseu controle de finanças.")

    def saldo(self):
        """Calcula o saldo do usuário, subtraindo o total de compras do total de rendas"""
        valorRenda = 0
        if len(self.__lRendas) > 0:
            for iV in range(len(self.__lRendas)):
                valorRenda += self.__lRendas[iV].getValor()

        precoCompra = 0
        if len(self.__lComprados) > 0:
            for iP in range(len(self.__lComprados)):
                precoCompra += self.__lComprados[iP].getPreco()
        return valorRenda - precoCompra

    def __str__(self):
        """Retorna uma representação em string do objeto usuário"""
        lNomesComprados = []
        for i in range(len(self.__lComprados)):
            lNomesComprados.append(self.__lComprados[i].getNome())
        strComprados = str.join(" e ", lNomesComprados).replace(" e ", ", ", len(lNomesComprados) - 2)

        lNomesRendas = []
        for i in range(len(self.__lRendas)):
            lNomesRendas.append(self.__lRendas[i].getNome())
        strRendas = str.join(" e ", lNomesRendas).replace(" e ", ", ", len(lNomesRendas) - 2)

        return "\nNome: {}\nSenha: {}\nLista de comprados: {}\nLista de rendas: {}".format(self.__nome, self.__senha, strComprados, strRendas)
