# clase de polimorfismo

class Coche():

    def desplazamiento(self):
        print("Se desplaza con cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Se desplaza con dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Se desplaza con seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion() # aquí puede ir Moto, Coche o Camión
desplazamientoVehiculo(miVehiculo) # se reemplaza automáticamente aquí

