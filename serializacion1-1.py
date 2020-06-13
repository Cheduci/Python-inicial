import pickle

fichero = open("lista_nombres", "rb") # r de read, b de binary

lista = pickle.load(fichero)

print(lista)