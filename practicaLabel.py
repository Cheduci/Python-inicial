from tkinter import *

root = Tk()
root.title("Mi segunda ventana, Zhang Jian Qiao")

miFrame = Frame(root,width = 1400, height = 900)
miFrame.pack()

miImagen = PhotoImage(file="jumbo.gif")

Label(miFrame, image = miImagen).place(x = 50, y = 80)

root.mainloop()