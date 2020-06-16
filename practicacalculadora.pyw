from tkinter import *
from tkinter import messagebox

def infoAdicional(): # se debe definir cada función del menú
    messagebox.showinfo("JQZ playing menus","This is just a test, so I'm just playing")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia ZJQ, así que PAGUE! PAGUE! PAGUE! xD")

def salirApp():
#    valor = messagebox.askquestion("Quit","Do you really want to quit???") # devuelve "yes" o "no"
    valor = messagebox.askokcancel("Quit","Do you really want to quit???") # devuelve True o False
    if valor:
        raiz.destroy()

def numeros(a):
    if a == ".":
        return True
    else:
        try:
            float(a)
            return True
        except:
            return False

def operacion(o,a,b):
    if o == "suma":
        return a + b
    elif o == "resta":
        return a - b
    elif o == "mult":
        return a * b
    else:
        return a / b


raiz = Tk()
raiz.title("Calculadora de Zhang Jian Qiao")

miFrame = Frame(raiz)
miFrame.pack()

# ---------- Menus ---------- #

barraMenu = Menu(raiz)
raiz.config(menu = barraMenu)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Quit", command = salirApp)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "License", command = avisoLicencia)
ayudaMenu.add_command(label = "About", command = infoAdicional)

barraMenu.add_cascade(label = "File", menu = archivoMenu)
barraMenu.add_cascade(label = "Help", menu = ayudaMenu)

# ---------- Displays ---------- #

def ac():
    global resetDisplay
    global op
    global opPrev
    global resultado
    op = ""
    opPrev = ""
    resultado = ""
    resetDisplay = False
    display.set(resultado)

display = StringVar()

resetDisplay = False
opPrev = ""
op = ""
resultado = 0

botonOn = Button(miFrame, text = "Ac", font = 10, width = 9, height = 2, command = lambda:ac())
botonOn.grid(row = 1, column = 1)
botonOn.config(bg = "red", fg = "white", cursor = "hand1")


pantalla = Entry(miFrame, font = 8, width = 26, textvariable = display)
pantalla.grid(row = 1, column = 2, pady = 2, columnspan = 3)
pantalla.config(bg = "black", fg = "#00FF0F", justify = "right")

# ---------- pulsaciones ---------- #

def botoncoma():
    global resetDisplay
    global op
    global opPrev
    a = display.get()
    if a == "":
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


def suma(num):
    global op
    global opPrev
    global resultado
    global resetDisplay
    op = "suma"
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

def resta(num):
    global op
    global opPrev
    global resultado
    global resetDisplay
    op = "resta"
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

def mult(num):
    global op
    global opPrev
    global resultado
    global resetDisplay
    op = "mult"
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

def div(num):
    global op
    global opPrev
    global resultado
    global resetDisplay
    op = "div"
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

# ---------- segunda fila ---------- #

boton7 = Button(miFrame, text = "7", font = 10, width = 9, height = 2, command = lambda:botonPulsado("7"))
boton7.grid(row = 2, column = 1)
boton7.config(cursor = "hand2")

boton8 = Button(miFrame, text = "8", font = 10, width = 9, height = 2, command = lambda:botonPulsado("8"))
boton8.grid(row = 2, column = 2)
boton8.config(cursor = "hand2")

boton9 = Button(miFrame, text = "9", font = 10, width = 9, height = 2, command = lambda:botonPulsado("9"))
boton9.grid(row = 2, column = 3)
boton9.config(cursor = "hand2")

botonDiv = Button(miFrame, text = "/", font = 10, width = 9, height = 2, command = lambda:div(display.get()))
botonDiv.grid(row = 2, column = 4)
botonDiv.config(cursor = "hand2")

# ---------- tercera fila ---------- #

boton4 = Button(miFrame, text = "4", font = 10, width = 9, height = 2, command = lambda:botonPulsado("4"))
boton4.grid(row = 3, column = 1)
boton4.config(cursor = "hand2")

boton5 = Button(miFrame, text = "5", font = 10, width = 9, height = 2, command = lambda:botonPulsado("5"))
boton5.grid(row = 3, column = 2)
boton5.config(cursor = "hand2")

boton6 = Button(miFrame, text = "6", font = 10, width = 9, height = 2, command = lambda:botonPulsado("6"))
boton6.grid(row = 3, column = 3)
boton6.config(cursor = "hand2")

botonMult = Button(miFrame, text = "x", font = 10, width = 9, height = 2, command = lambda:mult(display.get()))
botonMult.grid(row = 3, column = 4)
botonMult.config(cursor = "hand2")

# ---------- cuarta fila ---------- #

boton1 = Button(miFrame, text = "1", font = 10, width = 9, height = 2, command = lambda:botonPulsado("1"))
boton1.grid(row = 4, column = 1)
boton1.config(cursor = "hand2")

boton2 = Button(miFrame, text = "2", font = 10, width = 9, height = 2, command = lambda:botonPulsado("2"))
boton2.grid(row = 4, column = 2)
boton2.config(cursor = "hand2")

boton3 = Button(miFrame, text = "3", font = 10, width = 9, height = 2, command = lambda:botonPulsado("3"))
boton3.grid(row = 4, column = 3)
boton3.config(cursor = "hand2")

botonRest = Button(miFrame, text = "-", font = 10, width = 9, height = 2, command = lambda:resta(display.get()))
botonRest.grid(row = 4, column = 4)
botonRest.config(cursor = "hand2")

# ---------- quinta fila ---------- #

boton0 = Button(miFrame, text = "0", font = 10, width = 9, height = 2, command = lambda:botonPulsado("0"))
boton0.grid(row = 5, column = 1)
boton0.config(cursor = "hand2")

botonComa = Button(miFrame, text = ".", font = 10, width = 9, height = 2, command = lambda:botoncoma())
botonComa.grid(row = 5, column = 2)
botonComa.config(cursor = "hand2")

botonIgual = Button(miFrame, text = "=", font = 10, width = 9, height = 2, command = lambda:igual(display.get()))
botonIgual.grid(row = 5, column = 3)
botonIgual.config(cursor = "hand2")

botonSuma = Button(miFrame, text = "+", font = 10, width = 9, height = 2, command = lambda:suma(display.get()))
botonSuma.grid(row = 5, column = 4)
botonSuma.config(cursor = "hand2")


raiz.mainloop()