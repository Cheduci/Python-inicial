from tkinter import *

root = Tk()
root.title("Mi segunda ventana, Zhang Jian Qiao")

miFrame = Frame(root,width = 1400, height = 900)
miFrame.pack()

miImagen = PhotoImage(file = "graficos\jumbo.gif")
label1 = Label(miFrame, image = miImagen).place(x = 50, y = 80)

miLabel = Label(miFrame, text = "Mi primer texto en ventana. ZJQ", font = 18)
miLabel.place(x = 200, y = 10)

root.mainloop()