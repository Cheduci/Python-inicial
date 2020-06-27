class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre,self.cargo,self.salario)

listaEmpleados = [
    Empleado("Matías", "Director", 6700),
    Empleado("Ana", "Profesora", 7500),
    Empleado("Antonio", "Administrativo", 2100),
    Empleado("Sara", "Secretaria", 2150),
    Empleado("Mario", "Conserje", 1800
),
]

def calculo_comision(empleado):
    if empleado.salario <= 3000:
        empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for i in listaEmpleadosComision:
    print(i)