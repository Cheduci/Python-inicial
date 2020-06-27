from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# ------------ FUNCIONES ------------ 

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD","La BBDD fue creada exitósamente")
    
    except:
        messagebox.showwarning("¡Atención!","La BBDD ya existe")

def salirApp():
    valor = messagebox.askquestion("Salir","Jodeme que querés salir")
    if valor == "yes":
        root.destroy()

def clearCampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPassword.set("")
    textoComentario.delete(1.0, END)

def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datosAlmacenar = (miNombre.get(), miPassword.get(), miApellido.get(), miDireccion.get(), textoComentario.get(1.0,END))
    miCursor.execute("insert into DATOSUSUARIOS VALUES (Null,?,?,?,?,?)", datosAlmacenar)
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro ingresado exitosamente")

def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    
    miCursor.execute("select * from DATOSUSUARIOS where ID=" + miID.get())
    elUsuario = miCursor.fetchall()
    clearCampos()
    for i in elUsuario:
        miID.set(i[0])
        miNombre.set(i[1])
        miPassword.set(i[2])
        miApellido.set(i[3])
        miDireccion.set(i[4])
        textoComentario.insert(1.0, i[5])

    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    
    #miCursor.execute("update DATOSUSUARIOS set NOMBRE_USUARIO='" + miNombre.get() + "', PASSWORD='" + miPassword.get()+ "', APELLIDO='"+ miApellido.get() + "', DIRECCION='"+miDireccion.get() + "',COMENTARIOS='"+ textoComentario.get("1.0",END)+"' WHERE ID=" + miID.get())
    datosAlmacenar = (miNombre.get(), miPassword.get(), miApellido.get(), miDireccion.get(), textoComentario.get(1.0,END))
    miCursor.execute("update DATOSUSUARIOS set NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?" + "where ID=" + miID.get(), datosAlmacenar)
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro actualizado exitosamente")

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("delete from DATOSUSUARIOS where ID=" + miID.get())
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro eliminado exitosamente")

# ------------ MENUS ------------ 

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

menuBBDD = Menu(barraMenu, tearoff = 0)
menuBBDD.add_command(label = "Conectar", command = conexionBBDD)
menuBBDD.add_command(label = "Salir", command = salirApp)

menuBorrar = Menu(barraMenu, tearoff = 0)
menuBorrar.add_command(label = "Borrar todo", command = clearCampos)

menuCRUD = Menu(barraMenu, tearoff = 0)
menuCRUD.add_command(label = "Crear", command = crear)
menuCRUD.add_command(label = "Leer", command = leer)
menuCRUD.add_command(label = "Actualizar", command = actualizar)
menuCRUD.add_command(label = "Borrar", command = eliminar)

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

miID = StringVar()

cuadroID = Entry(miFrame, textvariable = miID)
cuadroID.grid(row = 0, column = 1, padx = 10, pady = 10)

miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable = miNombre)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroNombre.config(fg = "red", justify = "right")

miPassword = StringVar()

cuadroPass = Entry(miFrame, textvariable = miPassword)
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*")

miApellido = StringVar()

cuadroApellido = Entry(miFrame, textvariable = miApellido)
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

miDireccion = StringVar()

cuadroDireccion = Entry(miFrame, textvariable = miDireccion)
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

frame2 = Frame(root)
frame2.pack()

botonCrear = Button(frame2, text = "Create", command = crear)
botonCrear.grid(row = 0, column = 0, padx = 10, pady = 10)
botonLeer = Button(frame2, text = "Read", command = leer)
botonLeer.grid(row = 0, column = 1, padx = 10, pady = 10)
botonUpdate = Button(frame2, text = "Update", command = actualizar)
botonUpdate.grid(row = 0, column = 2, padx = 10, pady = 10)
botonDelete = Button(frame2, text = "Delete", command = eliminar)
botonDelete.grid(row = 0, column = 3, padx = 10, pady = 10)



root.mainloop()