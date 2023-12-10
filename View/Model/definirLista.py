# Parte responsável pela importação dos módulos
from pickle import *

# Criação de uma variável tipo lista inicialmente vazia
listaUsers = []

# Abertura do arquivo de texto no modo de escrita binária
arq2 = open("UsuáriosCadastrados.txt", "wb")

# Controle de error para um erro de entrada e saída de dados
try:
        dump(listaUsers, arq2) # Deserialização do texto UsuáriosCadastrados
	
except IOError as e:
        print(e) # Visualização do motivo do erro de entrada e saída
	
finally:
        arq2.close() # Fechamento do arquivo de texto

# Aviso que a lista foi criada
print("Lista vazia criada")