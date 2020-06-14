import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se registró una nueva persona cuyo nombre es",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno","ab+") # ab+ --> a=append, b=binary, +=reading and writing
        listaDePersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del listaDePersonas
            

    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del listaDePersonas

    def mostarInfoFicheroExterno(self):
        print("La info es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
p = Persona("Francisco","Masculino",38)
miLista.agregarPersonas(p)
miLista.mostarInfoFicheroExterno()