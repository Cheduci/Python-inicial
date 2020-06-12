class Vehiculos():
    def __init__(self,marca,modelo): # constructor de propiedades iniciales
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        if self.enmarcha:
            self.frena = True
        else:
            print("El vehículo está detenido, no es necesario frenar.")    
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): # hereda las funciones y las propiedades
    hcaballito = ""
    def caballito(self):
        hcaballito = "Voy haciendo el caballito"

miMoto = Moto("Honda","CBR")

miMoto.estado()