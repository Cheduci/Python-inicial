from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional(): # se debe definir cada función del menú
    messagebox.showinfo("JQZ playing menus","This is just a test, so I'm just playing")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia ZJQ, así que PAGUE! PAGUE! PAGUE! xD")

def salirApp():
#    valor = messagebox.askquestion("Quit","Do you really want to quit???") # devuelve "yes" o "no"
    valor = messagebox.askokcancel("Quit","Do you really want to quit???") # devuelve True o False
    if valor:
        root.destroy()

def cerrarDoc():
    valor = messagebox.askretrycancel("Reintentar","you can't just simply close") # devuelve True o False
    if not valor:
        root.destroy()


barraMenu = Menu(root)
root.config(menu = barraMenu, width = 800, height = 600)

archivoMenu = Menu(barraMenu, tearoff = 0) # tear es una barra separadora que viene por defecto, el valor 0 lo elimina
archivoMenu.add_command(label = "New")
archivoMenu.add_command(label = "Open")
archivoMenu.add_command(label = "Save")
archivoMenu.add_command(label = "Save as")
archivoMenu.add_separator() # separador
archivoMenu.add_command(label = "Close", command = cerrarDoc)
archivoMenu.add_command(label = "Quit", command = salirApp)

edicionMenu = Menu(barraMenu, tearoff = 0)
edicionMenu.add_command(label = "Undo")
edicionMenu.add_command(label = "Redo")
edicionMenu.add_separator()
edicionMenu.add_command(label = "Copy")
edicionMenu.add_command(label = "Cut")
edicionMenu.add_command(label = "Paste")

herramientasMenu = Menu(barraMenu, tearoff = 0)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "License", command = avisoLicencia)
ayudaMenu.add_command(label = "About", command = infoAdicional)

barraMenu.add_cascade(label = "File", menu = archivoMenu) # fundamental, pero va después de definir el nombre de solapa
barraMenu.add_cascade(label = "Edit", menu = edicionMenu)
barraMenu.add_cascade(label = "Tools", menu = herramientasMenu)
barraMenu.add_cascade(label = "Help", menu = ayudaMenu)



root.mainloop()