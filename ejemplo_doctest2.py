import math

def raizCuad(listaNum):
    """
    La función defuelve una lista con la raiz cuadrada de los
    elementos de la lista ingresada
    >>> lista = []
    >>> for i in [4,9,16]:
    ...     lista.append(i)  # los tres puntos sirven para avisar que esta instrucción está anidada en el for anterior
    >>> raizCuad(lista)
    [2.0, 3.0, 4.0]
    
    >>> lista = []
    >>> for i in [-4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuad(lista)
    Traceback (most recent call last):
        ...   # cuando se espera un error, pero solo importa la primera y última línea, las del medio no son importantes
    ValueError: math domain error
    
    """

    return [math.sqrt(n) for n in listaNum]

#print(raizCuad([9,-16,25,36,49,64]))

import doctest
doctest.testmod()