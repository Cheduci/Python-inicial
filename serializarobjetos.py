import pickle

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
        print("\n", self.__class__,"\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1 = Vehiculos("Honda","Corolla")
coche2 = Vehiculos("Wolksvagen","Fox")
coche3 = Vehiculos("Fiat","Uno")

coches = [coche1, coche2, coche3]
fichero = open("losCoches","wb")
pickle.dump(coches, fichero)
fichero.close()
del fichero

ficheroApertura = open("losCoches","rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for i in misCoches:
    print(i.estado())