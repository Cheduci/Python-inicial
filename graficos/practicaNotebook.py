from tkinter import *
from tkinter import ttk

def ocultar2():
    nb.hide(1)

def mostrar2():
    nb.add(page2, text = "Tab 2")

def ira2():
    nb.select(1)

raiz = Tk()
raiz.title("Notebook")
raiz.geometry("800x600")

rows = 0
while rows < 50:
    raiz.rowconfigure(rows, weight = 1)
    raiz.columnconfigure(rows, weight = 1)
    rows += 1

nb = ttk.Notebook(raiz)
nb.grid(row = 0, column = 0, columnspan = 50, rowspan = 50, sticky = "nswe", padx = 5, pady = 5)

page1 = Frame(nb, bg = "red")
nb.add(page1, text = "Tab 1")
page2 = Frame(nb, bg = "black")
nb.add(page2, text = "Tab 2")
page3 = Frame(nb)
nb.add(page3, text = "Tab 3")

boton1 = Button(page1, text = "Ocultar Tab 2", command = ocultar2).pack(pady = 5)
boton2 = Button(page1, text = "Mostrar Tab 2", command = mostrar2).pack(pady = 5)
boton3 = Button(page1, text = "Ir a Tab 2", command = ira2).pack(pady = 5)

raiz.mainloop()