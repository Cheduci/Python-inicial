def hello(name="idiot"):
    print("{0} jelou {0}".format(name))
    # .format() reemplaza todos los {0} por el argumento del format


add = lambda n1, n2: print(n1 + n2)
add(1,3)