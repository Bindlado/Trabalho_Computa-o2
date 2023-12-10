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