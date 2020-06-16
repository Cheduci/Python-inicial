from tkinter import *
from tkinter import filedialog


root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title = "Abrir",initialdir="D:\Mis cosas\Images", filetypes= (("Ficheros de excel","*.xlsx"),("Ficheros de texto","*.txt"))) # devuelve la ruta del archivo seleccionado, "filetypes" pide una tupla
    print(fichero)

Button(root, text = "Abrir fichero", command = abreFichero).pack()

root.mainloop()