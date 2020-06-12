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
        print("\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): # hereda las funciones y las propiedades
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
    
    def estado(self): # sobreescritura de métodos, el hijo sobreescribe al padre
        print("\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class Furgoneta(Vehiculos):

    def carga(self,cargar): # función exclusiva de furgoneta
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo) # Hereda las propiedades iniciales del padre
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

class BiciElectrica(VElectricos,Vehiculos): # herencia doble, hereda con prioridad la primera clase
    pass

miMoto = Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BiciElectrica("Shimano","T-1100")
miBici.estado()