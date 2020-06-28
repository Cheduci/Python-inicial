class Areas:
    """Esta clase permite calcular áreas de figuras geométricas"""
    def areaCuad(lado):
        """acá yo podría ingresar lo que yo quiera
        verdad?""" # documentación del programa
        return "El área del cuadrado es: " + str(lado**2)

    def areaTria(base, altura):
        return "El área del triángulo es: " + str(base*altura/2)



#print(areaTria(3,5))
print(areaCuad.__doc__) # imprime la documentación
help(areaCuad) # imprime la forma en que está definida la función y la documentación