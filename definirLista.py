from pickle import *
listaUsers = []

arq2 = open("UsuáriosCadastrados.txt", "wb")
try:
	dump(listaUsers, arq2)
except IOError as e:
	print(e)
finally:
	arq2.close()
print("Lista vazia criada")