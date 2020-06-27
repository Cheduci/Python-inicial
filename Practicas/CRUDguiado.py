from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# ------------ MENUS ------------ 

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

menuBBDD = Menu(barraMenu, tearoff = 0)
menuBBDD.add_command(label = "Conectar")
menuBBDD.add_command(label = "Salir")

menuBorrar = Menu(barraMenu, tearoff = 0)
menuBorrar.add_command(label = "Borrar todo")

menuCRUD = Menu(barraMenu, tearoff = 0)
menuCRUD.add_command(label = "Crear")
menuCRUD.add_command(label = "Leer")
menuCRUD.add_command(label = "Actualizar")
menuCRUD.add_command(label = "Borrar")

menuAyuda = Menu(barraMenu, tearoff = 0)
menuAyuda.add_command(label = "Licencia")
menuAyuda.add_command(label = "Acerca de")

barraMenu.add_cascade(label = "BBDD", menu = menuBBDD)
barraMenu.add_cascade(label = "Borrar", menu = menuBorrar)
barraMenu.add_cascade(label = "CRUD", menu = menuCRUD)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

# ------------ CAMPOS ------------ 

miFrame = Frame(root)
miFrame.pack()

cuadroID = Entry(miFrame)
cuadroID.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroNombre.config(fg = "red", justify = "right")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 4, column = 1, padx = 10, pady = 10)

textoComentario = Text(miFrame, width = 14, height = 5)
textoComentario.grid(row = 5, column = 1, sticky = "w", padx = 10, pady = 10)
scrollVert = Scrollbar(miFrame, command = textoComentario.yview)
scrollVert.grid(row = 5, column = 1, sticky = "nse")
textoComentario.config(yscrollcommand = scrollVert.set)

# ------------ Labels ------------ 

labelID = Label(miFrame, text = "ID: ")
labelID.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

labelNombre = Label(miFrame, text = "Nombre: ")
labelNombre.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

labelPass = Label(miFrame, text = "Password: ")
labelPass.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

labelApellido = Label(miFrame, text = "Apellido: ")
labelApellido.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)

labelDireccion = Label(miFrame, text = "Dirección: ")
labelDireccion.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10)

labelComentarios = Label(miFrame, text = "Comentarios: ")
labelComentarios.grid(row = 5, column = 0, sticky = "e", padx = 10, pady = 10)

# ------------ Frame 2 ------------ 





root.mainloop()