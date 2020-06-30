from tkinter import *
from tkinter import messagebox

def primerboton():
    messagebox.showinfo("Primer botón","El primer botón funciona")

def segundoboton():
    messagebox.showinfo("Segundo botón botón","El segundo botón funciona")

def tercerboton():
    cliente.set(""); apellido.set(""); nombre.set(""); snombre.set(""); rua.set(""); area.set(""); codpostal.set(""); ncnh.set(""); dataa.set(""); localidad.set(""); matricula.set(""); diastotales.set("") 
    tipomotor.set(""); estilo.set(""); agnoauto.set(""); claseauto.set(""); descauto.set(""); kmanterior.set(""); kmentrega.set(""); fabauto.set(""); modeloauto.set(""); fabmotor.set(""); corauto.set(""); seguroauto.set("")
    idCliente.set(""); totaldias.set(""); diasalqui.set(""); factura.set(""); descuento.set(""); totalfinal.set("")

def cuartoboton():
    salir = messagebox.askyesno("Salir","¿Seguro que desea salir?")
    if salir:
        raiz.destroy()

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
framesupizq.pack(side = TOP, anchor = CENTER)

primeroselem = Frame(framesupizq, bd = 5, relief = "raise", bg = "gold")
primeroselem.grid(row = 0, column = 0, pady = 50)

segundoselem = Frame(framesupizq)
segundoselem.grid(row = 1, column = 0, pady = 10)

tercerelem = Frame(framesupizq)
tercerelem.grid(row = 2, column = 0, pady = 10)

cuartoelem = Frame(framesupizq)
cuartoelem.grid(row = 3, column = 0, pady = 5, padx = 10)

quintoelem = Frame(framesupizq)
quintoelem.grid(row = 4, column = 0, pady = 30)

    # ------------ Título  ------------ #

Label(primeroselem, text = "Autos Rent Zhang", font = "Cambria 40 bold", bg = "gold").pack(padx = 100, pady = 20)

    # ------------ Datos cliente  ------------ #

grillacliente = LabelFrame(segundoselem, text = "Datos de cliente", font = "Cambria 15", labelanchor = "n")
grillacliente.pack(pady = 10)

cliente = StringVar()
etiq111 = Label(grillacliente, text = "Cliente: ", font = "15")
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
etiq122 = Label(grillacliente, text = "Rua: ", font = "15")
etiq122.grid(row = 1, column = 2, sticky = "e")
camp122 = Entry(grillacliente, textvariable = rua, font = "15")
camp122.grid(row = 1, column = 3)

area = StringVar()
etiq123 = Label(grillacliente, text = "Area: ", font = "15")
etiq123.grid(row = 1, column = 4, sticky = "e")
camp123 = Entry(grillacliente, textvariable = area, font = "15")
camp123.grid(row = 1, column = 5)

codpostal = StringVar()
etiq131 = Label(grillacliente, text = "Cod. Postal: ", font = "15")
etiq131.grid(row = 2, column = 0, sticky = "e")
camp131 = Entry(grillacliente, textvariable = codpostal, font = "15")
camp131.grid(row = 2, column = 1)

ncnh = StringVar()
etiq132 = Label(grillacliente, text = "N-CNH: ", font = "15")
etiq132.grid(row = 2, column = 2, sticky = "e")
camp132 = Entry(grillacliente, textvariable = ncnh, font = "15")
camp132.grid(row = 2, column = 3)

dataa = StringVar()
etiq133 = Label(grillacliente, text = "Data: ", font = "15")
etiq133.grid(row = 2, column = 4, sticky = "e")
camp133 = Entry(grillacliente, textvariable = dataa, font = "15")
camp133.grid(row = 2, column = 5)

localidad = StringVar()
etiq141 = Label(grillacliente, text = "Localidad: ", font = "15")
etiq141.grid(row = 3, column = 0, sticky = "e")
camp141 = Entry(grillacliente, textvariable = localidad, font = "15")
camp141.grid(row = 3, column = 1)

matricula = StringVar()
etiq142 = Label(grillacliente, text = "Matrícula: ", font = "15")
etiq142.grid(row = 3, column = 2, sticky = "e")
camp142 = Entry(grillacliente, textvariable = matricula, font = "15")
camp142.grid(row = 3, column = 3)

diastotales = StringVar()
etiq143 = Label(grillacliente, text = "Total días: ", font = "15")
etiq143.grid(row = 3, column = 4, sticky = "e")
camp143 = Entry(grillacliente, textvariable = diastotales, font = "15")
camp143.grid(row = 3, column = 5)

    # ------------ Datos auto  ------------ #

grillaauto = LabelFrame(tercerelem, text = "Datos de auto", font = "Cambria 15", labelanchor = "n")
grillaauto.pack(pady = 10)

tipomotor = StringVar()
etiq211 = Label(grillaauto, text = "Tipo motor: ", font = "15")
etiq211.grid(row = 0, column = 0, sticky = "e")
camp211 = Entry(grillaauto, textvariable = tipomotor, font = "15")
camp211.grid(row = 0, column = 1)

estilo = StringVar()
etiq212 = Label(grillaauto, text = "Estilo: ", font = "15")
etiq212.grid(row = 0, column = 2, sticky = "e")
camp212 = Entry(grillaauto, textvariable = estilo, font = "15")
camp212.grid(row = 0, column = 3)

agnoauto = StringVar()
etiq213 = Label(grillaauto, text = "Año auto: ", font = "15")
etiq213.grid(row = 0, column = 4, sticky = "e")
camp213 = Entry(grillaauto, textvariable = agnoauto, font = "15")
camp213.grid(row = 0, column = 5)

claseauto = StringVar()
etiq221 = Label(grillaauto, text = "Clase auto: ", font = "15")
etiq221.grid(row = 1, column = 0, sticky = "e")
camp221 = Entry(grillaauto, textvariable = claseauto, font = "15")
camp221.grid(row = 1, column = 1)

descauto = StringVar()
etiq222 = Label(grillaauto, text = "Desc-auto: ", font = "15")
etiq222.grid(row = 1, column = 2, sticky = "e")
camp222 = Entry(grillaauto, textvariable = descauto, font = "15")
camp222.grid(row = 1, column = 3)

kmanterior = StringVar()
etiq223 = Label(grillaauto, text = "Km-anterior: ", font = "15")
etiq223.grid(row = 1, column = 4, sticky = "e")
camp223 = Entry(grillaauto, textvariable = kmanterior, font = "15")
camp223.grid(row = 1, column = 5)

kmentrega = StringVar()
etiq231 = Label(grillaauto, text = "Km-entrega: ", font = "15")
etiq231.grid(row = 2, column = 0, sticky = "e")
camp231 = Entry(grillaauto, textvariable = kmentrega, font = "15")
camp231.grid(row = 2, column = 1)

fabauto = StringVar()
etiq232 = Label(grillaauto, text = "Fab-auto: ", font = "15")
etiq232.grid(row = 2, column = 2, sticky = "e")
camp232 = Entry(grillaauto, textvariable = fabauto, font = "15")
camp232.grid(row = 2, column = 3)

modeloauto = StringVar()
etiq233 = Label(grillaauto, text = "Modelo: ", font = "15")
etiq233.grid(row = 2, column = 4, sticky = "e")
camp233 = Entry(grillaauto, textvariable = modeloauto, font = "15")
camp233.grid(row = 2, column = 5)

fabmotor = StringVar()
etiq241 = Label(grillaauto, text = "Fab-motor: ", font = "15")
etiq241.grid(row = 3, column = 0, sticky = "e")
camp241 = Entry(grillaauto, textvariable = fabmotor, font = "15")
camp241.grid(row = 3, column = 1)

corauto = StringVar()
etiq242 = Label(grillaauto, text = "Cor-auto: ", font = "15")
etiq242.grid(row = 3, column = 2, sticky = "e")
camp242 = Entry(grillaauto, textvariable = corauto, font = "15")
camp242.grid(row = 3, column = 3)

seguroauto = StringVar()
etiq243 = Label(grillaauto, text = "Seguro auto: ", font = "15")
etiq243.grid(row = 3, column = 4, sticky = "e")
camp243 = Entry(grillaauto, textvariable = seguroauto, font = "15")
camp243.grid(row = 3, column = 5)

    # ------------ Info renta ------------ #

grillarenta = LabelFrame(cuartoelem, text = "Info de la renta", font = "Cambria 15", labelanchor = "n")
grillarenta.pack(pady = 10)

idCliente = StringVar()
totaldias = StringVar()
diasalqui = StringVar()
factura = StringVar()
descuento = StringVar()
totalfinal = StringVar()

etiquetacliente = Label(grillarenta, text = "ID cliente: ", font = "15")
etiquetacliente.grid(row = 0, column = 0, padx = 3, sticky = "e")
campocliente = Entry(grillarenta, textvariable = idCliente, font = "15")
campocliente.grid(row = 0, column = 1, padx = 3)

etiqtotaldias = Label(grillarenta, text = "Total días: ", font = "15")
etiqtotaldias.grid(row = 1, column = 0, padx = 3, sticky = "e")
campototaldias = Entry(grillarenta, textvariable = totaldias, font = "15")
campototaldias.grid(row = 1, column = 1, padx = 3)

etiqdiasalqui = Label(grillarenta, text = "D. Alquilado: ", font = "15")
etiqdiasalqui.grid(row = 0, column = 2, padx = 3, sticky = "e")
campodiasalqui = Entry(grillarenta, textvariable = diasalqui, font = "15")
campodiasalqui.grid(row = 0, column = 3, padx = 3)

etiqfactura = Label(grillarenta, text = "Factura: ", font = "15")
etiqfactura.grid(row = 1, column = 2, padx = 3, sticky = "e")
campofactura = Entry(grillarenta, textvariable = factura, font = "15")
campofactura.grid(row = 1, column = 3, padx = 3)

etiqdesc = Label(grillarenta, text = "Descuento: ", font = "15")
etiqdesc.grid(row = 0, column = 4, padx = 3, sticky = "e")
campodesc = Entry(grillarenta, textvariable = descuento, font = "15")
campodesc.grid(row = 0, column = 5, padx = 3)

etiqtotal = Label(grillarenta, text = "Total: ", font = "15")
etiqtotal.grid(row = 1, column = 4, padx = 3, sticky = "e")
campototal = Entry(grillarenta, textvariable = totalfinal, font = "15")
campototal.grid(row = 1, column = 5, padx = 3)
    
    # ------------ Botones ------------ #

#etiqueta1 = Label(frameIzq, text = "Etiqueta 1:", font = "Calibri 20 bold italic")
#etiqueta1.grid(row = 0, column = 0)
boton1 = Button(quintoelem, text = "Total", font = "Arial 15 bold", command = primerboton, width = 10)
boton1.grid(row = 1, column = 0, padx = 15, sticky = "n")

#etiqueta2 = Label(frameIzq, text = "Etiqueta 2:", font = "Calibri 20 bold italic")
#etiqueta2.grid(row = 1, column = 0)
boton2 = Button(quintoelem, text = "Recibo", font = "Arial 15 bold", command = segundoboton, width = 10)
boton2.grid(row = 1, column = 1, padx = 15, sticky = "n")

#etiqueta3 = Label(frameIzq, text = "Etiqueta 3:", font = "Calibri 20 bold italic")
#etiqueta3.grid(row = 2, column = 0)
boton3 = Button(quintoelem, text = "Limpiar", font = "Arial 15 bold", command = tercerboton, width = 10)
boton3.grid(row = 1, column = 2, padx = 15, sticky = "n")

#etiqueta4 = Label(frameIzq, text = "Etiqueta 4:", font = "Calibri 20 bold italic")
#etiqueta4.grid(row = 3, column = 0)
boton4 = Button(quintoelem, text = "Salir", font = "Arial 15 bold", command = cuartoboton, width = 10)
boton4.grid(row = 1, column = 3, padx = 15, sticky = "n")


# ------------ Fin del programa ------------ #
raiz.mainloop()