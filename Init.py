'''# Arquivo responsável por iniciar o Controle de FInanças (Trabalho de computação)

def executar():
# arquivo_principal.py

import sys
import os

# Adiciona o diretório do arquivo_a_executar.py ao sys.path
diretorio_do_arquivo_a_executar = os.path.abspath(os.path.dirname(__file__))
sys.path.append(diretorio_do_arquivo_a_executar)

# Importa e chama a função do arquivo_a_executar
from arquivo_a_executar import funcao_a_executar

executar()'''

'''import sys

#sys.path.append('C:/Users/diego/Área de Trabalho/Trabalho_Computa-o_2/View')
sys.path.append('/View')
print(sys.path)

python3'''

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
sys.path.append(os.path.join(current_dir, 'View'))
print(current_dir)


