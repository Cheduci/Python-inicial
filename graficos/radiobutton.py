from tkinter import *

raiz = Tk()

varOpcion = IntVar()

def imprimir():
    # print(varOpcion.get())
    if varOpcion.get() == 1:
        etiqueta.config(text = "Eres hombre")
    else:
        etiqueta.config(text = "Eres mujer")

Label(raiz, text = "Género").pack()

Radiobutton(raiz, text = "Masculino", variable = varOpcion, value = 1, command = imprimir).pack()
Radiobutton(raiz, text = "Femenino", variable = varOpcion, value = 2, command = imprimir).pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()