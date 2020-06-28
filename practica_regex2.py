import re
#lista_nombres = ['Ana Gómez','María Martín','Sandra López','Santiago Martín','Sandra Pérez']

lista_nombres = ["hombres","mujeres","mascotas",'niños','niñas','camion','camión']
for i in lista_nombres:
#    if re.findall('^Sandra',i): # buscará los elementos de la lista en busca del que empiece con Sandra
#    if re.findall('Martín$',i): # buscará los que terminen en Martín
#    if re.findall('niñ[oa]s',i): # busca los elementos con opciones multiples de busqueda
#    if re.findall("cami[oó]n",i):
    if re.findall('[o-t]',i): # busca resultados en rango
        print(i)