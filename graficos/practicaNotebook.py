from tkinter import *
from tkinter import ttk

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

page1 = ttk.Frame(nb)
nb.add(page1, text = "Tab 1")

page2 = ttk.Frame(nb)
nb.add(page2, text = "Tab 2")

page3 = ttk.Frame(nb)
nb.add(page3, text = "Tab 3")

raiz.mainloop()