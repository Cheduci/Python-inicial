from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ----------- Funciones ----------- #
def numero(a):
    try:
        float(a)
        return True
    except:
        return False


def conexionBBDD():
    miConexion = sqlite3.connect("Productosprueba") # Nombre de archivo
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSPRODUCTOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            PRECIO REAL)
            ''')
        messagebox.showinfo("BBDD","La BBDD fue creada exitósamente")
    
    except:
        messagebox.showwarning("¡Atención!","La BBDD ya existe")

def salirApp():
    valor = messagebox.askquestion("Salir","Jodeme que querés salir")
    if valor == "yes":
        raiz.destroy()

def crear():
    if elID.get() == "":
        miConexion = sqlite3.connect("Productosprueba")
        miCursor = miConexion.cursor()
        try:
            miCursor.execute('''
                CREATE TABLE DATOSPRODUCTOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PRECIO REAL)
                ''')
            messagebox.showinfo("BBDD","La BBDD fue creada exitósamente")
        except:
            pass
        finally:
            datosAlmacenar = (nombre.get(), precio.get())
            miCursor.execute("insert into DATOSPRODUCTOS VALUES (Null,?,?)", datosAlmacenar)
            miConexion.commit()

        messagebox.showinfo("BBDD","Registro ingresado exitosamente")
        get_prod()
    else:
        messagebox.showwarning("Cuidado","Debe dejar vacío el casillero ID")

def leer():
    try:
        idsel = str(arbol.item(arbol.selection())['text']) # cuidado con lo que devuelve el selection()

        miConexion = sqlite3.connect("Productosprueba")
        miCursor = miConexion.cursor()

        miCursor.execute("select * from DATOSPRODUCTOS where ID=" + idsel)
        elUsuario = miCursor.fetchall()
        elnombre.set("")
        elprecio.set("")
        for i in elUsuario:
            elID.set(i[0])
            elnombre.set(i[1])
            elprecio.set(i[2])
        miConexion.commit()
    except:
        messagebox.showwarning("Cuidado","Debe seleccionar un elemento de la tabla")

def actualizar():
    edit_wind = Toplevel()
    edit_wind.title("Actualizar")

    name = arbol.item(arbol.selection())['values'][0]
    old_price = arbol.item(arbol.selection())['values'][1]
    Label(edit_wind, text = "Nombre viejo: ").grid(row = 0, column = 0)
    Entry(edit_wind, textvariable = StringVar(edit_wind, value = name), state="readonly").grid(row = 0, column = 1)
    Label(edit_wind, text = "Precio viejo: ").grid(row = 1, column = 0)
    Entry(edit_wind, textvariable = StringVar(edit_wind, value = old_price), state="readonly").grid(row = 1, column = 1)
    
    nuevo_nombre = StringVar()
    nuevo_precio = StringVar()
    Label(edit_wind, text = "Nombre nuevo: ").grid(row = 0, column = 3)
    new_name = Entry(edit_wind, textvariable = nuevo_nombre)
    new_name.grid(row = 0, column = 4)
    Label(edit_wind, text = "Precio nuevo: ").grid(row = 1, column = 3)
    new_price = Entry(edit_wind, textvariable = nuevo_precio)
    new_price.grid(row = 1, column = 4)

    Button(edit_wind, text = "Modificar", command = lambda:modificar(nuevo_nombre.get(), nuevo_precio.get(), name, old_price)).grid(row = 0, column = 2, rowspan = 2, sticky = "ns")
    
    def modificar(new_name, new_price, name, old_price):
        if new_name != "" and numero(new_price) and new_price != "":

            miConexion = sqlite3.connect("Productosprueba")
            miCursor = miConexion.cursor()

            datosAlmacenar = (new_name, new_price, name, old_price)
            miCursor.execute("update DATOSPRODUCTOS set NOMBRE=?, PRECIO=? where NOMBRE=? and PRECIO=?", datosAlmacenar)
            miConexion.commit()
            messagebox.showinfo("BBDD","Registro actualizado exitosamente")
            edit_wind.destroy() # para que este destroy funcione, tiene que estar en tab con la función actualizar
        else:
            messagebox.showwarning("Cuidado","Debe ingresar valores correctamente")

        get_prod()

def eliminar():
    try:
        idsel = str(arbol.item(arbol.selection())['text'])

        miConexion = sqlite3.connect("Productosprueba")
        miCursor = miConexion.cursor()

        miCursor.execute("delete from DATOSPRODUCTOS where ID=" + idsel)
        miConexion.commit()

        messagebox.showinfo("BBDD","Registro eliminado exitosamente")
    except:
            messagebox.showwarning("Cuidado","Debe seleccionar un elemento de la tabla")
    get_prod()
    elID.set("")
    elnombre.set("")
    elprecio.set("")

def get_prod():
    records = arbol.get_children()
    for elem in records:
        arbol.delete(elem)
    
    miConexion = sqlite3.connect("Productosprueba")
    miCursor = miConexion.cursor()
   
    filasbd = miCursor.execute("select * from DATOSPRODUCTOS order by ID desc")
    miConexion.commit()
    for fila in filasbd:
        arbol.insert("", 0, text = fila[0], values = (fila[1], fila[2])) # al parecer "text" define el contenido de la primera columna

# ----------- Ventana ----------- #

raiz = Tk()
raiz.title('Products application')

# ----------- Menus ----------- #
barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300)

menuBBDD = Menu(barraMenu, tearoff = 0)
menuBBDD.add_command(label = "Conectar", command = conexionBBDD)
menuBBDD.add_command(label = "Salir", command = salirApp)

barraMenu.add_cascade(label = "BBDD", menu = menuBBDD)

# ----------- Frame 1 ----------- #

miFrame = Frame(raiz)
miFrame.pack()

algo1 = LabelFrame(miFrame, text = 'Register a new product')
algo1.grid(row = 0, column = 0, columnspan = 3)

elID = StringVar()

Label(algo1, text = 'ID: ').grid(row = 1, column = 0, sticky = "e")
miID = Entry(algo1, textvariable = elID)
miID.grid(row = 1, column = 1)

elnombre = StringVar()

Label(algo1, text = 'Nombre: ').grid(row = 2, column = 0, sticky = "e")
nombre = Entry(algo1, textvariable = elnombre)
nombre.focus()  # con esto enfocas el cursor en este entry al aprir la app
nombre.grid(row = 2, column = 1)

elprecio = StringVar()

Label(algo1, text = 'Precio: ').grid(row = 3, column = 0, sticky = "e")
precio = Entry(algo1, textvariable = elprecio)
precio.grid(row = 3, column = 1)

botonCrear = Button(algo1, text = 'Crear Producto', command = crear).grid(row = 4, columnspan = 2, sticky = "we")

# ----------- Botones (Frame 2) ----------- #

miFrame2 = Frame(raiz)
miFrame2.pack()

botonLeer = Button(miFrame2, text = "Leer", command = leer)
botonLeer.grid(row = 0, column = 0, padx = 10, pady = 10)
botonUpdate = Button(miFrame2, text = "Modificar", command = actualizar)
botonUpdate.grid(row = 0, column = 1, padx = 10, pady = 10)
botonDelete = Button(miFrame2, text = "Eliminar", command = eliminar)
botonDelete.grid(row = 0, column = 2, padx = 10, pady = 10)

# ----------- Tabla (Frame 3) ----------- #

miFrame3 = Frame(raiz)
miFrame3.pack(fill = "both", expand = 1)

arbol = ttk.Treeview(miFrame3)
arbol.pack(fill = "both", expand = 1)

arbol["columns"] = ("one", "two")
arbol.column("#0", width = 50, minwidth = 50)
arbol.heading("#0", text = "ID", anchor = CENTER)
arbol.column("one", width = 150, minwidth = 150)
arbol.heading("one", text = "Nombre", anchor = CENTER)
arbol.column("two", width = 75, minwidth = 75)
arbol.heading("two", text = "Precio", anchor = CENTER)

try:
    get_prod()
except:
    pass



raiz.mainloop()