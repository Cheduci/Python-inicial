from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sqlite3 import *

def jajaja(a):
    try:
        float(a)
        return True
    except:
        return False

def primerboton():
    messagebox.showinfo("Primer botón","El primer botón funciona")

def segundoboton():
    messagebox.showinfo("Segundo botón","El segundo botón funciona")

def tercerboton():
    cliente.set(""); apellido.set(""); nombre.set(""); snombre.set(""); rua.set(""); area.set(""); codpostal.set(""); ncnh.set(""); dataa.set(""); localidad.set(""); matricula.set(""); diastotales.set("") 
    tipomotor.set(""); estilo.set(""); agnoauto.set(""); claseauto.set(""); descauto.set(""); kmanterior.set(""); kmentrega.set(""); fabauto.set(""); modeloauto.set(""); fabmotor.set(""); corauto.set(""); seguroauto.set("")
    idCliente.set(""); totaldias.set(""); diasalqui.set(""); factura.set(""); descuento.set(""); totalfinal.set("")

def cuartoboton():
    salir = messagebox.askyesno("Salir","¿Seguro que desea salir?")
    if salir:
        raiz.destroy()

def quintoboton():
    messagebox.showinfo("Quinto botón","{}".format(muestra))

def opciones():
    global muestra
    eleccion = {"estilo":"Económico", "claseid":"Cliente estándar", "facturaid":"Pagado en ARS", "diaria":"No", "automatico":"No", "aircond":"No", "segurinc":"No", "detallecliente":"No"}
    if checkuno.get() == 1:
        eleccion["estilo"] = "Clásico"
    if checkdos.get() == 1:
        eleccion["claseid"] = "Cliente VIP"
    if checktres.get() == 1:
        eleccion["facturaid"] = "Pagado en USD"
    if checkcuatro.get() == 1:
        eleccion["diaria"] = "Sí"
    if checkcinco.get() == 1:
        eleccion["automatico"] = "Sí"
    if checkseis.get() == 1:
        eleccion["aircond"] = "Sí"
    if checksiete.get() == 1:
        eleccion["segurinc"] = "Sí"
    if checkocho.get() == 1:
        eleccion["detallecliente"] = "Sí"
    muestra = eleccion

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_CLIENTE VARCHAR(20),
            APELLIDO_CLIENTE VARCHAR(20),
            NOMBRE_CLIENTE VARCHAR(20),
            S_NOMBRE VARCHAR(20),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD","La BBDD fue creada exitósamente")
    
    except:
        messagebox.showwarning("¡Atención!","La BBDD ya existe")

def get_prod():
    records = arbol.get_children()
    for elem in records:
        arbol.delete(elem)
    
    miConexion = sqlite3.connect("AlquilerDeAutos")
    miCursor = miConexion.cursor()
   
    filasbd = miCursor.execute("select * from ALQUILER order by ID desc")
    miConexion.commit()
    for fila in filasbd:
        arbol.insert("", 0, text = fila[0], values = (fila[1], fila[2]))

# ------------ Definiendo estructura ventana ------------ #

raiz = Tk()
raiz.title("No sé qué estoy haciendo")

rows = 0
while rows < 2:
    raiz.rowconfigure(rows, weight = 1)
    raiz.columnconfigure(rows, weight = 1)
    rows += 1

# ------------ Frames principales ------------ #

frameIzq = Frame(raiz, width = 400, height = 600, bd=4, relief = "raise")
frameIzq.grid(row = 0, column = 0, rowspan = 2, sticky ="news")
frameDer = Frame(raiz, width = 600, height = 600, bd=4, relief = "raise")
frameDer.grid(row = 0, column = 1, rowspan = 2, sticky ="news")

# ------------ Estructura Frame izquierdo ------------ #

framesupizq = Frame(frameIzq)
framesupizq.pack(side = TOP, anchor = CENTER, pady = 20)

primeroselem = Frame(framesupizq, bd = 5, relief = "raise", bg = "gold")
primeroselem.grid(row = 0, column = 0, pady = 20)

segundoselem = Frame(framesupizq)
segundoselem.grid(row = 1, column = 0, pady = 10)

tercerelem = Frame(framesupizq)
tercerelem.grid(row = 2, column = 0, pady = 10)

cuartoelem = Frame(framesupizq)
cuartoelem.grid(row = 3, column = 0, pady = 5, padx = 10)

quintoelem = Frame(framesupizq)
quintoelem.grid(row = 4, column = 0, pady = 30)

    # ------------ Título  ------------ #

Label(primeroselem, text = "Autos Rent Chuang", font = "Cambria 40 bold", bg = "gold").pack(padx = 100, pady = 20)

    # ------------ Datos cliente  ------------ #

grillacliente = LabelFrame(segundoselem, text = "Datos de cliente", font = "Cambria 15", labelanchor = "n")
grillacliente.pack(pady = 10)

cliente = StringVar()
etiq111 = Label(grillacliente, text = "Documento: ", font = "15")
etiq111.grid(row = 0, column = 0, sticky = "e")
camp111 = Entry(grillacliente, textvariable = cliente, font = "15")
camp111.grid(row = 0, column = 1)

apellido = StringVar()
etiq112 = Label(grillacliente, text = "Apellido: ", font = "15")
etiq112.grid(row = 0, column = 2, sticky = "e")
camp112 = Entry(grillacliente, textvariable = apellido, font = "15")
camp112.grid(row = 0, column = 3)

nombre = StringVar()
etiq113 = Label(grillacliente, text = "Nombre: ", font = "15")
etiq113.grid(row = 0, column = 4, sticky = "e")
camp113 = Entry(grillacliente, textvariable = nombre, font = "15")
camp113.grid(row = 0, column = 5)

snombre = StringVar()
etiq121 = Label(grillacliente, text = "S-Nombre: ", font = "15")
etiq121.grid(row = 1, column = 0, sticky = "e")
camp121 = Entry(grillacliente, textvariable = snombre, font = "15")
camp121.grid(row = 1, column = 1)

rua = StringVar()
etiq122 = Label(grillacliente, text = "Licencia: ", font = "15")
etiq122.grid(row = 1, column = 2, sticky = "e")
camp122 = Entry(grillacliente, textvariable = rua, font = "15")
camp122.grid(row = 1, column = 3)

area = StringVar()
etiq123 = Label(grillacliente, text = "Teléfono: ", font = "15")
etiq123.grid(row = 1, column = 4, sticky = "e")
camp123 = Entry(grillacliente, textvariable = area, font = "15")
camp123.grid(row = 1, column = 5)

codpostal = StringVar()
etiq131 = Label(grillacliente, text = "Domicilio: ", font = "15")
etiq131.grid(row = 2, column = 0, sticky = "e")
camp131 = Entry(grillacliente, textvariable = codpostal, font = "15")
camp131.grid(row = 2, column = 1)

ncnh = StringVar()
etiq132 = Label(grillacliente, text = "XXXX: ", font = "15")
etiq132.grid(row = 2, column = 2, sticky = "e")
camp132 = Entry(grillacliente, textvariable = ncnh, font = "15")
camp132.grid(row = 2, column = 3)

dataa = StringVar()
etiq133 = Label(grillacliente, text = "XXXX: ", font = "15")
etiq133.grid(row = 2, column = 4, sticky = "e")
camp133 = Entry(grillacliente, textvariable = dataa, font = "15")
camp133.grid(row = 2, column = 5)

    # ------------ Datos auto  ------------ #

grillaauto = LabelFrame(tercerelem, text = "Datos de auto", font = "Cambria 15", labelanchor = "n")
grillaauto.pack(pady = 10)

tipomotor = StringVar()
etiq211 = Label(grillaauto, text = "Tipo vehículo: ", font = "15")
etiq211.grid(row = 0, column = 0, sticky = "e")
camp211 = Entry(grillaauto, textvariable = tipomotor, font = "15")
camp211.grid(row = 0, column = 1)

estilo = StringVar()
etiq212 = Label(grillaauto, text = "Marca: ", font = "15")
etiq212.grid(row = 0, column = 2, sticky = "e")
camp212 = Entry(grillaauto, textvariable = estilo, font = "15")
camp212.grid(row = 0, column = 3)

agnoauto = StringVar()
etiq213 = Label(grillaauto, text = "Modelo: ", font = "15")
etiq213.grid(row = 0, column = 4, sticky = "e")
camp213 = Entry(grillaauto, textvariable = agnoauto, font = "15")
camp213.grid(row = 0, column = 5)

claseauto = StringVar()
etiq221 = Label(grillaauto, text = "Año auto: ", font = "15")
etiq221.grid(row = 1, column = 0, sticky = "e")
camp221 = Entry(grillaauto, textvariable = claseauto, font = "15")
camp221.grid(row = 1, column = 1)

descauto = StringVar()
etiq222 = Label(grillaauto, text = "Nombre motor: ", font = "15")
etiq222.grid(row = 1, column = 2, sticky = "e")
camp222 = Entry(grillaauto, textvariable = descauto, font = "15")
camp222.grid(row = 1, column = 3)

kmanterior = StringVar()
etiq223 = Label(grillaauto, text = "Año motor: ", font = "15")
etiq223.grid(row = 1, column = 4, sticky = "e")
camp223 = Entry(grillaauto, textvariable = kmanterior, font = "15")
camp223.grid(row = 1, column = 5)

kmentrega = StringVar()
etiq231 = Label(grillaauto, text = "Combustible: ", font = "15")
etiq231.grid(row = 2, column = 0, sticky = "e")
camp231 = Entry(grillaauto, textvariable = kmentrega, font = "15")
camp231.grid(row = 2, column = 1)

fabauto = StringVar()
etiq232 = Label(grillaauto, text = "Km. acumulados: ", font = "15")
etiq232.grid(row = 2, column = 2, sticky = "e")
camp232 = Entry(grillaauto, textvariable = fabauto, font = "15")
camp232.grid(row = 2, column = 3)

modeloauto = StringVar()
etiq233 = Label(grillaauto, text = "Seguro: ", font = "15")
etiq233.grid(row = 2, column = 4, sticky = "e")
camp233 = Entry(grillaauto, textvariable = modeloauto, font = "15")
camp233.grid(row = 2, column = 5)

    # ------------ Info renta ------------ #

grillarenta = LabelFrame(cuartoelem, text = "Info de la renta", font = "Cambria 15", labelanchor = "n")
grillarenta.pack(pady = 10)

idCliente = StringVar()
totaldias = StringVar()
diasalqui = StringVar()
factura = StringVar()
descuento = StringVar()
totalfinal = StringVar()

etiquetacliente = Label(grillarenta, text = "ID Factura: ", font = "15")
etiquetacliente.grid(row = 0, column = 0, padx = 3, sticky = "e")
campocliente = Entry(grillarenta, textvariable = idCliente, font = "15", state = "readonly")
campocliente.grid(row = 0, column = 1, padx = 3)

etiqtotaldias = Label(grillarenta, text = "Total días: ", font = "15")
etiqtotaldias.grid(row = 1, column = 0, padx = 3, sticky = "e")
campototaldias = Entry(grillarenta, textvariable = totaldias, font = "15")
campototaldias.grid(row = 1, column = 1, padx = 3)

etiqdiasalqui = Label(grillarenta, text = "Fecha alquiler: ", font = "15")
etiqdiasalqui.grid(row = 0, column = 2, padx = 3, sticky = "e")
campodiasalqui = Entry(grillarenta, textvariable = diasalqui, font = "15")
campodiasalqui.grid(row = 0, column = 3, padx = 3)

etiqfactura = Label(grillarenta, text = "Costo diario: ", font = "15")
etiqfactura.grid(row = 1, column = 2, padx = 3, sticky = "e")
campofactura = Entry(grillarenta, textvariable = factura, font = "15")
campofactura.grid(row = 1, column = 3, padx = 3)

etiqdesc = Label(grillarenta, text = "Descuento: ", font = "15")
etiqdesc.grid(row = 0, column = 4, padx = 3, sticky = "e")
campodesc = Entry(grillarenta, textvariable = descuento, font = "15")
campodesc.grid(row = 0, column = 5, padx = 3)

etiqtotal = Label(grillarenta, text = "Total: ", font = "15")
etiqtotal.grid(row = 1, column = 4, padx = 3, sticky = "e")
campototal = Entry(grillarenta, textvariable = totalfinal, font = "15", state = "readonly")
campototal.grid(row = 1, column = 5, padx = 3)
    
    # ------------ Botones ------------ #

boton1 = Button(quintoelem, text = "Vehículo", font = "Arial 15 bold", command = primerboton, width = 10)
boton1.grid(row = 1, column = 0, padx = 15)

boton2 = Button(quintoelem, text = "Total", font = "Arial 15 bold", command = segundoboton, width = 10)
boton2.grid(row = 1, column = 1, padx = 15)

boton3 = Button(quintoelem, text = "Limpiar", font = "Arial 15 bold", command = tercerboton, width = 10)
boton3.grid(row = 1, column = 2, padx = 15)

boton4 = Button(quintoelem, text = "Salir", font = "Arial 15 bold", command = cuartoboton, width = 10, bg = "red")
boton4.grid(row = 1, column = 3, padx = 15)

boton5 = Button(quintoelem, text = "Imprimir", font = "Arial 15 bold", command = quintoboton, width = 10)
boton5.grid(row = 1, column = 4, padx = 15)

# ------------ Estructura Frame derecho ------------ #

framesupder = Frame(frameDer, width = 500)
framesupder.pack(side = TOP, anchor = CENTER)

elemuno = Frame(framesupder)
elemuno.grid(row = 0, column = 0, pady = 10)

elemdos = Frame(framesupder, width = 500)
elemdos.grid(row = 1, column = 0, pady = 10)

elemtres = Frame(framesupder, width = 500)
elemtres.grid(row = 2, column = 0, pady = 10)

    # ------------ Settings de alquiler ------------ #

muestra = dict()

grillaopciones = Frame(elemuno)
grillaopciones.pack()

checkuno = IntVar()
check1 = Checkbutton(grillaopciones, text = "Estilo", variable = checkuno, onvalue = 1, offvalue = 0, command = opciones)
check1.grid(row = 0)
checkdos = IntVar()
check2 = Checkbutton(grillaopciones, text = "Clase ID", variable = checkdos, onvalue = 1, offvalue = 0, command = opciones)
check2.grid(row = 1)
checktres = IntVar()
check3 = Checkbutton(grillaopciones, text = "Factura ID", variable = checktres, onvalue = 1, offvalue = 0, command = opciones)
check3.grid(row = 2)
checkcuatro = IntVar()
check4 = Checkbutton(grillaopciones, text = "Diaria", variable = checkcuatro, onvalue = 1, offvalue = 0, command = opciones)
check4.grid(row = 3)
checkcinco = IntVar()
check5 = Checkbutton(grillaopciones, text = "Automático", variable = checkcinco, onvalue = 1, offvalue = 0, command = opciones)
check5.grid(row = 4)
checkseis = IntVar()
check6 = Checkbutton(grillaopciones, text = "A/C", variable = checkseis, onvalue = 1, offvalue = 0, command = opciones)
check6.grid(row = 5)
checksiete = IntVar()
check7 = Checkbutton(grillaopciones, text = "Seguro incluido", variable = checksiete, onvalue = 1, offvalue = 0, command = opciones)
check7.grid(row = 6)
checkocho = IntVar()
check8 = Checkbutton(grillaopciones, text = "Detalles del cliente", variable = checkocho, onvalue = 1, offvalue = 0, command = opciones)
check8.grid(row = 7)
    # ------------ Botones ------------ #

grillabotones = Frame(elemdos)
grillabotones.pack()

botonuno = Button(grillabotones, text = "Boton uno", font = "Calibri 15")
botonuno.grid(row = 0, column = 0, padx = 10)

botondos = Button(grillabotones, text = "Boton dos", font = "Calibri 15")
botondos.grid(row = 0, column = 1, padx = 10)

botontres = Button(grillabotones, text = "Boton tres", font = "Calibri 15")
botontres.grid(row = 0, column = 2, padx = 10)

botoncuatro = Button(grillabotones, text = "Boton cuatro", font = "Calibri 15")
botoncuatro.grid(row = 0, column = 3, padx = 10)


    # ------------ Tabla ------------ #

grillatabla = Frame(elemtres, width = 500)
grillatabla.pack(fill = "both", expand = 1, padx = 10, pady = 10)

arbol = ttk.Treeview(grillatabla, height = 22)
arbol.pack(fill = "both", expand = 1)

arbol["columns"] = ("one", "two", "three")
arbol.column("#0", width = 150, minwidth = 50)
arbol.heading("#0", text = "Num factura", anchor = CENTER)
arbol.column("one", width = 150, minwidth = 150)
arbol.heading("one", text = "ID Auto", anchor = CENTER)
arbol.column("two", width = 150, minwidth = 75)
arbol.heading("two", text = "Nombre cliente", anchor = CENTER)
arbol.column("three", width = 150, minwidth = 75)
arbol.heading("three", text = "Fecha expiracion", anchor = CENTER)

scrollHor = Scrollbar(grillatabla, command = arbol.xview, orient=HORIZONTAL)
scrollHor.pack(fill = "x")
arbol.config(xscrollcommand = scrollHor.set)

try:
    get_prod()
except:
    pass



# ------------ Fin del programa ------------ #
raiz.mainloop()