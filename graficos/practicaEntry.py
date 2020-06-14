from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 1200, height = 900)
miFrame.pack()

minombre = StringVar()

labelNombre = Label(miFrame, text = "Nombre 名: ", font = 18)
labelNombre.grid(row = 0, column = 0, sticky = "e", padx = 2)
cuadroNombre = Entry(miFrame, font=1, textvariable = minombre)
cuadroNombre.grid(row = 0, column = 1, sticky = "w")

labelApellido = Label(miFrame, text = "Apellido 姓: ", font = 18)
labelApellido.grid(row = 1, column = 0, sticky = "e", padx = 2)
cuadroApellido = Entry(miFrame, font=1)
cuadroApellido.grid(row = 1, column = 1, sticky = "w")

labelDomicilio = Label(miFrame, text = "Domicilio 住址: ", font = 18)
labelDomicilio.grid(row = 2, column = 0, sticky = "e", padx = 2)
cuadroDomicilio = Entry(miFrame, font=1)
cuadroDomicilio.grid(row = 2, column = 1, sticky = "w")

labelPass = Label(miFrame, text = "Password 密码: ", font = 18)
labelPass.grid(row = 3, column = 0, sticky = "e", padx = 2)
cuadroPass = Entry(miFrame, font=1)
cuadroPass.grid(row = 3, column = 1, sticky = "w")
cuadroPass.config(show = "*")

labelComent = Label(miFrame, text = "Comentarios 评论: ", font = 18)
labelComent.grid(row = 4, column = 0, sticky = "ne", padx = 2)
cuadroComent = Text(miFrame, width = 20, height = 10)
cuadroComent.grid(row = 4, column = 1, sticky = "w")
scrollVert = Scrollbar(miFrame, command = cuadroComent.yview) # el scrollbar se construye a parte, luego se coloca donde se necesita
scrollVert.grid(row = 4, column = 1, sticky = "nse") # para dejar el scrollbar dentro del cuadro, se lo superpone con este y solo se stickea arriba-abajo-derecha
cuadroComent.config(yscrollcommand = scrollVert.set) # muestra la posición actual del scroll, pero esto debe hacerse después de crear el scroll

def codigoBoton():
    minombre.set("Matías")

botonEnvio = Button(raiz, text = "Enviar", command = codigoBoton)
botonEnvio.pack()

raiz.mainloop()