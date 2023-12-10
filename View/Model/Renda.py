# Parte responsável pela importação dos módulos
from tkinter import messagebox
from datetime import *

class Renda:
    """Classe que representa uma entrada de renda"""

    def __init__(self, nome, valor, fonte, dataRecebimento):
        """Inicializa uma instância da classe Renda"""
        
        self.__nome = nome
        self.__valor = float(valor)
        self.fonte = fonte
        self.dataRecebimento = datetime.strptime(dataRecebimento, '%d/%m/%Y %H:%M')
        
        for i in range(10):
            if str(i) in self.__nome:
                raise TypeError
        
    def getNome(self):
        """Retorna o nome da renda"""
        return self.__nome
        
    def setNome(self, novoNome):
        """Atualiza o nome da renda"""
        self.__nome = novoNome
        
    def getValor(self):
        """Retorna o valor da renda"""
        return self.__valor
        
    def setValor(self, novoValor):
        """Atualiza o valor da renda"""
        self.__valor = novoValor
        
    def __str__(self):
        """Retorna uma representação em string da instância da classe"""
        return "{} - {} - {} - {} - Renda".format(self.dataRecebimento.strftime('%d/%m/%Y %H:%M'), self.__nome, self.fonte, self.__valor)

