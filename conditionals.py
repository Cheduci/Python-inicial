x = int(input("poné lo que quieras: "))
if x < 30: # No olvidar el ":"
    print("x is less than 30") # ell primer renglón es para True
    # es fundamental dejar el espacio adelante

# En python puede hacer una segunda condición con "elif"

elif x == 30: 
    print("x is equal to 30")

# En python hay que aclarar el incumplimiento de la condición

else: 
    print("x is greater than 30")

# Ejemplo de cadena de condiciones
name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter"
        print("you are John Carter")
    else:
        print("you are not John Carter")
else:
    print("you are not even John")

# Ejemplo de doble condición simultánea

y = 11

if y > 2 and y <=10:
    print("y está entre 2 y 10")
if (not(y == 10)):
    print("y no es igual a 10")