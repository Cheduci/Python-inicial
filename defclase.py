class Coche(): # definición de una clase
    
    def __init__(self): # constructor de estado inicial (2 guiones bajos adelante y atrás)
        self.largoChasis=250 # definición de propiedades
        self.anchoChasis=120
        self.__ruedas=4 # encapsulado, con 2 guiones bajos evita que después se pueda modificar, además no se puede llamar
        self.enmarcha=False # 4 propiedades, no llevan paréntesis

  # definición de métodos
  # def function(self): "function" es lo que puede hacer, "self" se refiere al objeto perteneciente a la clase
  #     pass

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if self.enmarcha:
            chequeo = self.__chequeo_interno()
        if self.enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.enmarcha and chequeo == False:
            return "Algo salió mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"

    def estado(self): # 2 comportamientos
        print("Cant. de ruedas: ", self.__ruedas, '''
Long. de coche: ''', self.largoChasis, '''
Ancho de coche: ''', self.anchoChasis, '''
''')

    def __chequeo_interno(self): # encapsulado de método, solo se puede modificar desde otro método
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "no ok"
        self.puertas = "cerradas"
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

print('''
------Creación del 1er objeto------
''')

miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print('''
------Creación del 2do objeto------
''')

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()