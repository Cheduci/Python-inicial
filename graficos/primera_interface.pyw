from tkinter import * # la extensión .pyw permite abrir desde windows sin consola

raiz = Tk()

raiz.title("Mi primera ventana, Zhang Jian Qiao")
#raiz.geometry("800x600")
raiz.config(bg = "green") # bg = background
raiz.config(bd=32)
raiz.config(relief = "groove")
raiz.resizable(False,True) # el primer argumento es para el eje X y el segundo para el eje Y

miFrame = Frame()
#miFrame.pack(side="left",anchor="s") # side funca con direcciones, anchor funciona con puntos cardinales
miFrame.pack(fill = "both", expand = "True") # para rellenar en la dirección Y, necesita expand = "True"
miFrame.config(bg = "black")
miFrame.config(width = "800", height = "600")
miFrame.config(cursor = "hand2")

raiz.mainloop()