from tkinter import *
from tkinter import ttk
import sqlite3

class Product:
    db_name = "Productosprueba"
    def __init__(self, window):
        self.wind = window
        self.wind.title("Products application")

        frame = LabelFrame(self.wind, text = "New product registration", labelanchor = "n")
        frame.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

        Label(frame, text = "Name: ").grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)
        self.name.focus()

        Label(frame, text = "Price: ").grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        ttk.Button(frame, text = "Save product").grid(row = 3, columnspan = 2, sticky = "we")

        frame2 = Frame(self.wind)
        frame2.grid(row = 4, columnspan = 2)

        self.tree = ttk.Treeview(frame2, height = 10)
        self.tree.pack()
        self.tree["columns"] = ("one","two")
        self.tree.column("#0")
        self.tree.heading("#0", text = "ID")
        self.tree.column("one")
        self.tree.heading("one", text = "Name")
        self.tree.column("two")
        self.tree.heading("two", text = "Price")

    def run_query(self, query, parameter = ()):
        with sqlite3.connect(self.)
if __name__ == "__main__":
    window = Tk()
    application = Product(window)

        
    window.mainloop()