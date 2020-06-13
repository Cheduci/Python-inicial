from io import open

archivo_texto = open("archivo.txt","r+") # open crea y abre a la vez, r+ significa lectura y escritura

lista_texto=archivo_texto.readlines()

lista_texto[1] = "jajaja, probé cambiar esto desde afuera \n"
archivo_texto.seek(0) # no olvidar esto, súmamente importante
archivo_texto.writelines(lista_texto)

archivo_texto.close()