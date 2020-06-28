import re

cadena1 = "Jara López"
cadena2 = "Antonio Gómez"
cadena3 = "Lara López"

codigo1 = "aewrhoijireohnjaoerñ71aohbjnew4org"
codigo2 = "apehgaioh71arenwjohgar"
codigo3 = "aophnwgongiuheo5nrhygñnh"


#if re.match(".ara", cadena2,re.IGNORECASE): # el . es caracter comodin, el ignorecase evita case sensitive
#if re.match("\d", cadena2): # esto busca si la cadena empieza con número
#if re.search("López", cadena3): # SEARCH busca en TODA la cadena
if re.search("71", codigo3):
    print("Se encontró")
else:
    print("No se encontró")