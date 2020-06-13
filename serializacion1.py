import pickle

lista_nombres = ["Jorge", "Christian", "Matías", "Diego"]
fichero_binario = open("lista_nombres","wb") # w para write, b para binary

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()
del fichero_binario