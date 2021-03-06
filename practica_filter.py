class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self): # esto define el speech cuando se llama a un empleado
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre,self.cargo,self.salario)

listaEmpleados = [
    Empleado("Matías", "Director", 80000),
    Empleado("Ana", "Profesora", 70000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Conserje", 21000),
]

salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados) # esta es la linea donde se construye la lista filtrada

for empleadoSalario in salarios_altos:
    print(empleadoSalario)
