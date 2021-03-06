from tkinter import *
from tkinter import messagebox

# ---------- Mensajes menus ---------- #

def infoAdicional(): # se debe definir cada función del menú
    messagebox.showinfo("JQZ playing menus","This is just a test, so I'm just playing")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia ZJQ, así que PAGUE! PAGUE! PAGUE! xD")

def salirApp():
#    valor = messagebox.askquestion("Quit","Do you really want to quit???") # devuelve "yes" o "no"
    valor = messagebox.askokcancel("Quit","Do you really want to quit???") # devuelve True o False
    if valor:
        raiz.destroy()

# ---------- Operador universal ---------- #

def operacion(o,a,b):
    """
    Este es el operador que hace todas las operaciones, si en un futuro se quiere agregar más funciones a la calculadora, se puede agregar desde acá.
    El parámetro 'o' es la operación que analiza, se ingresa un string y hay que hacer un "elif" que lo sepa distinguir, tal como "suma", "resta", etc.
    """
    if o == "suma":
        return a + b
    elif o == "resta":
        return a - b
    elif o == "mult":
        return a * b
    elif o == "div":
        return a / b

# ---------- Pulsaciones ---------- #

def ac():
    global resetDisplay
    global op
    global opPrev
    global resultado
    op = ""
    opPrev = ""
    resultado = ""
    resetDisplay = True
    display.set(resultado)

def botoncoma():
    global resetDisplay
    global op
    global opPrev
    a = display.get()
    if resetDisplay:
        display.set("0.")
        resetDisplay = False
    elif a.count(".") == 0:
        display.set(display.get() + ".")

def botonPulsado(num):
    global resetDisplay
    if resetDisplay != False:
        display.set(num)
        resetDisplay = False
    else:
        display.set(display.get() + num)

def botonOperacion(num,oper):
    """
    Convocar esta función en todos los botones de operación.
    Se recomienda usar "display.get()" en el parámetro 'num' y en el parámetro 'oper' usar el string que la función "operacion" sepa disginguir.
    La función "operacion(o,a,b)" está descrita más arriba.
    """
    global op
    global opPrev
    global resultado
    global resetDisplay
    op = oper
    if opPrev == "":
        resultado = float(num)
        opPrev = op
        resetDisplay = True
        display.set(resultado)
    else:
        resultado = operacion(opPrev,resultado,float(num))
        opPrev = op
        resetDisplay = True
        display.set(resultado)

def igual(num):
    global opPrev
    global resultado
    global resetDisplay
    resultado = operacion(opPrev,resultado,float(num))
    opPrev = ""
    resetDisplay = True
    display.set(resultado)
    resultado = 0

# ---------- Inicio de calculadora ---------- #

raiz = Tk()
raiz.title("Calculadora de Zhang Jian Qiao")
raiz.resizable(False,False)

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg = "black")

# ---------- Menus ---------- #

barraMenu = Menu(raiz)
raiz.config(menu = barraMenu)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Quit", command = salirApp)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "License", command = avisoLicencia)
ayudaMenu.add_command(label = "About", command = infoAdicional)

barraMenu.add_cascade(label = "App", menu = archivoMenu)
barraMenu.add_cascade(label = "Help", menu = ayudaMenu)

# ---------- Display ---------- #

display = StringVar()

resetDisplay = True
opPrev = ""
op = ""
resultado = 0

botonOn = Button(miFrame, text = "Ac", font = 10, width = 9, height = 2, command = ac)
botonOn.grid(row = 1, column = 1)
botonOn.config(bg = "red", fg = "white", cursor = "hand1")

pantalla = Entry(miFrame, font = "Calibri 20", textvariable = display, state = "readonly")
pantalla.grid(row = 1, column = 2, columnspan = 3, sticky = "we")
pantalla.config(bg = "black", fg = "black", justify = "right")

# ---------- Segunda fila ---------- #

boton7 = Button(miFrame, text = "7", font = 10, width = 9, height = 2, command = lambda:botonPulsado("7"))
boton7.grid(row = 2, column = 1, padx = 2, pady = 2)
boton7.config(cursor = "hand2")

boton8 = Button(miFrame, text = "8", font = 10, width = 9, height = 2, command = lambda:botonPulsado("8"))
boton8.grid(row = 2, column = 2, padx = 2, pady = 2)
boton8.config(cursor = "hand2")

boton9 = Button(miFrame, text = "9", font = 10, width = 9, height = 2, command = lambda:botonPulsado("9"))
boton9.grid(row = 2, column = 3, padx = 2, pady = 2)
boton9.config(cursor = "hand2")

botonDiv = Button(miFrame, text = "/", font = 10, width = 9, height = 2, command = lambda:botonOperacion(display.get(),"div"))
botonDiv.grid(row = 2, column = 4, padx = 2, pady = 2)
botonDiv.config(cursor = "hand2")

# ---------- Tercera fila ---------- #

boton4 = Button(miFrame, text = "4", font = 10, width = 9, height = 2, command = lambda:botonPulsado("4"))
boton4.grid(row = 3, column = 1, padx = 2, pady = 2)
boton4.config(cursor = "hand2")

boton5 = Button(miFrame, text = "5", font = 10, width = 9, height = 2, command = lambda:botonPulsado("5"))
boton5.grid(row = 3, column = 2, padx = 2, pady = 2)
boton5.config(cursor = "hand2")

boton6 = Button(miFrame, text = "6", font = 10, width = 9, height = 2, command = lambda:botonPulsado("6"))
boton6.grid(row = 3, column = 3, padx = 2, pady = 2)
boton6.config(cursor = "hand2")

botonMult = Button(miFrame, text = "x", font = 10, width = 9, height = 2, command = lambda:botonOperacion(display.get(),"mult"))
botonMult.grid(row = 3, column = 4, padx = 2, pady = 2)
botonMult.config(cursor = "hand2")

# ---------- Cuarta fila ---------- #

boton1 = Button(miFrame, text = "1", font = 10, width = 9, height = 2, command = lambda:botonPulsado("1"))
boton1.grid(row = 4, column = 1, padx = 2, pady = 2)
boton1.config(cursor = "hand2")

boton2 = Button(miFrame, text = "2", font = 10, width = 9, height = 2, command = lambda:botonPulsado("2"))
boton2.grid(row = 4, column = 2, padx = 2, pady = 2)
boton2.config(cursor = "hand2")

boton3 = Button(miFrame, text = "3", font = 10, width = 9, height = 2, command = lambda:botonPulsado("3"))
boton3.grid(row = 4, column = 3, padx = 2, pady = 2)
boton3.config(cursor = "hand2")

botonRest = Button(miFrame, text = "-", font = 10, width = 9, height = 2, command = lambda:botonOperacion(display.get(),"resta"))
botonRest.grid(row = 4, column = 4, padx = 2, pady = 2)
botonRest.config(cursor = "hand2")

# ---------- Quinta fila ---------- #

boton0 = Button(miFrame, text = "0", font = 10, width = 9, height = 2, command = lambda:botonPulsado("0"))
boton0.grid(row = 5, column = 1, padx = 2, pady = 2)
boton0.config(cursor = "hand2")

botonComa = Button(miFrame, text = ".", font = 10, width = 9, height = 2, command = botoncoma)
botonComa.grid(row = 5, column = 2, padx = 2, pady = 2)
botonComa.config(cursor = "hand2")

botonIgual = Button(miFrame, text = "=", font = 10, width = 9, height = 2, command = lambda:igual(display.get()))
botonIgual.grid(row = 5, column = 3, padx = 2, pady = 2)
botonIgual.config(cursor = "hand2")

botonSuma = Button(miFrame, text = "+", font = 10, width = 9, height = 2, command = lambda:botonOperacion(display.get(),"suma"))
botonSuma.grid(row = 5, column = 4, padx = 2, pady = 2)
botonSuma.config(cursor = "hand2")

# ---------- Fin del programa ---------- #
raiz.mainloop()