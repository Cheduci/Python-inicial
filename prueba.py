from tkinter import *
from tkinter import ttk
from tkinter import messagebox

raiz = Tk()
tree=ttk.Treeview(raiz)

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270)
tree.column("one", width=150, minwidth=150)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50)

tree.heading("#0",text="Name",anchor=CENTER)
tree.heading("one", text="Date modified",anchor=CENTER)
tree.heading("two", text="Type",anchor=CENTER)
tree.heading("three", text="Size",anchor=CENTER)

tree.pack()


raiz.mainloop()