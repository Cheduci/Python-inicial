import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

n1 = "Python"

print(len(re.findall(n1,cadena)))