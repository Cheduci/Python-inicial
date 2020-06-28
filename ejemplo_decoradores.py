def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs): # *args permite añadir los parámetros que quieras, "args" puede llamarse como quieras. **kwargs para keywords
        # Acciones adicionales que decoran
        print("Realizaremos un cálculo: ")

        funcion_parametro(*args, **kwargs)

        print("Se completó el cálculo.")
    
    return funcion_interior

@funcion_decoradora # el @ hace invocación de decoradora a la función suma
def suma(a,b,c):
    print(a+b+c)

@funcion_decoradora
def resta(a,b):
    print(a-b)

@funcion_decoradora
def potencia(n1,n2):
    print(n1**n2)

suma(3,5,8)

resta(8,3)

potencia(n1=2,n2=3) # los keywords tienen que coincidir con lo definido en la función