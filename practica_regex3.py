import re

#lista_nombres = ["Ana","Pedro","María",'Rosa','Sandra','Celia']
#
#for i in lista_nombres:
#    if re.findall('[o-t]',i):
#        print(i)

lista_ciudades = ["Ma1","Se1","Ma2","Ba1","Ma3","Va1","Va2","Ma4","MaA","Ma5","MaB","MaC"]

for i in lista_ciudades:
#    if re.findall("Ma[^0-3]", i): # el ^ en el rango hace que lo niegue, mostrando solo Ma4
    if re.findall("Ma[0-3A-B]",i): # ambos rangos se concatenan automáticamente 
        print(i)