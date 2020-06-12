#foods = ["apples","bread","cheese","milk","bananas"]

#for foo in foods: # Para recorrer listas/tuples
#    # Fundamental el espacio adelante
#    if foo == "cheese":
#        #break # Deja de contar
#        continue # continúa olvidando el valor del "if"
#    print(foo)
    
count = 4

while count <= 10:
    print(count)
    count = count + 1

import random
a = random.randint(1,101)
encontrado = False
intentos = 0

while not encontrado: 
    # while not condiciona según True o False de la variable analizada
    n = int(input("Ingrese número: "))
    if n < a:
        print("Su número es menor")
        intentos = intentos + 1
    elif n > a:
        print("Su número es mayor")
        intentos = intentos + 1
    else:
        encontrado = True
        print("Ud. acertó, el número es: {0}".format(a))
        print("Nro. de intentos: {0}".format(intentos))