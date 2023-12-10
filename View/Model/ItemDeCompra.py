# Parte responsável pela importação dos módulos
from tkinter import messagebox
from datetime import *

class ItemDeCompra:
    """Classe que representa um item de compra"""

    def __init__(self, nome, preco, localCompra, dataCompra):
        """Inicializa uma instância da classe ItemDeCompra"""
        self.__nome = nome
        self.__preco = float(preco)
        self.localCompra = localCompra
        self.dataCompra = datetime.strptime(dataCompra, '%d/%m/%Y %H:%M')
        
        for i in range(10):
            if str(i) in self.__nome:
                raise TypeError
        
    def getNome(self):
        """Retorna o nome do item de compra"""
        return self.__nome
        
    def setNome(self, novoNome):
        """Atualiza o nome do item de compra"""
        self.__nome = novoNome
        
    def getPreco(self):
        """Retorna o preço do item de compra"""
        return self.__preco
        
    def setPreco(self, novoPreco):
        """Atualiza o preço do item de compra"""
        self.__preco = novoPreco
        
    def __str__(self):
        """Retorna uma representação em string da instância da classe"""
        return "{} - {} - {} - {}".format(self.dataCompra.strftime('%d/%m/%Y %H:%M'), self.__nome, self.localCompra, self.__preco)
