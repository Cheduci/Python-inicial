from tkinter import *

raiz = Tk()
raiz.geometry("800x600")

miFrame = Frame(raiz, width = 1200, height = 900)
miFrame.pack()

labelNombre = Label(miFrame, text = "Nombre 名: ", font = 18)
labelNombre.grid(row = 0, column = 0, sticky = "w", padx = 2)

cuadroNombre = Entry(miFrame, font=1)
cuadroNombre.grid(row = 0, column = 1, padx = 4, pady = 2)

labelApellido = Label(miFrame, text = "Apellido 姓: ", font = 18)
labelApellido.grid(row = 1, column = 0, sticky = "w", padx = 2)

cuadroApellido = Entry(miFrame, font=1)
cuadroApellido.grid(row = 1, column = 1)

labelDomicilio = Label(miFrame, text = "Domicilio 住址: ", font = 18)
labelDomicilio.grid(row = 2, column = 0, sticky = "w", padx = 2)

cuadroDomicilio = Entry(miFrame, font=1)
cuadroDomicilio.grid(row = 2, column = 1)

labelPass = Label(miFrame, text = "Password 密码: ", font = 18)
labelPass.grid(row = 3, column = 0, sticky = "w", padx = 2)

cuadroPass = Entry(miFrame, font=1)
cuadroPass.grid(row = 3, column = 1)
cuadroPass.config(show = "*")

raiz.mainloop()