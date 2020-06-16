from tkinter import *

root = Tk()
root.title("Whatever I want")

uno = IntVar()
dos = IntVar()
tres = IntVar()

def opciones():
    global muestra
    eleccion = ""
    if uno.get() == 1:
        eleccion += "uno "
    
    if dos.get() == 1:
        eleccion += "dos "

    if tres.get() == 1:
        eleccion += "tres "

    muestra.config(text = eleccion)

foto = PhotoImage(file = "graficos\jumbo.gif")
Label(root, image = foto).pack()

miFrame = Frame(root)
miFrame.pack()

Label(miFrame, text = "Elige lo que quieras").pack()

Checkbutton(miFrame, text = "uno", variable = uno, onvalue = 1, offvalue = 0, command = opciones).pack()
Checkbutton(miFrame, text = "dos", variable = dos, onvalue = 1, offvalue = 0, command = opciones).pack()
Checkbutton(miFrame, text = "tres", variable = tres, onvalue = 1, offvalue = 0, command = opciones).pack()

muestra = Label(miFrame)
muestra.pack()

root.mainloop()