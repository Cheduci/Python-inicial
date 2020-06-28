def areaTrian(base,altura):

    """
    Calcula al área de un triángulo
    >>> areaTrian(3,6)
    9.0
    """

    return (base*altura)/2

def areaCuad(lado):

    """
    Calcula al área de un triángulo
    >>> areaCuad(2)
    4
    """

    return lado**2

import doctest 
doctest.testmod() # esto testea TODAS las funciones según la documentación a partir de >>>