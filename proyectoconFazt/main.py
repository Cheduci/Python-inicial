from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

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

        ttk.Button(frame, text = "Save product", command = self.add_product).grid(row = 3, columnspan = 2, sticky = "we")

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

        self.get_products()
        
        Button(self.wind, text = "Edit", command = self.edit_product).grid(row = 5, column = 0, sticky = "we")
        Button(self.wind, text = "Delete", command = self.delete_product).grid(row = 5, column = 1, sticky = "we")

    def run_query(self, query, parameter = ()):
        with sqlite3.connect(self.db_name) as conn:
            micursor = conn.cursor()
            miresultado = micursor.execute(query, parameter)
            conn.commit()
        return miresultado

    def get_products(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        query = "select * from DATOSPRODUCTOS order by ID desc"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("",0, text = row[0], values = (row[1], row[2]))

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            try:
                query = "create table DATOSPRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL)"
                self.run_query(query)
                messagebox.showinfo("BBDD", "Tabla creada exitósamente")
            except:
                query = "insert into DATOSPRODUCTOS values (Null,?,?)"
                parameters = (self.name.get(), self.price.get())
                self.run_query(query, parameters)
                messagebox.showinfo("BBDD","Se registró {} correctamente a ${}".format(self.name.get(), self.price.get()))
                self.name.delete(0, END)
                self.price.delete(0, END)
        else:
            messagebox.showwarning("Cuidado","Debe ingresar datos")
        self.get_products()

    def delete_product(self):
        try:
            idsel = self.tree.item(self.tree.selection())["text"]
            query = "delete from DATOSPRODUCTOS where ID=?"
            self.run_query(query, (idsel,))
            messagebox.showinfo("BBDD","Se eliminó {} correctamente".format(self.tree.item(self.tree.selection())["values"][0]))
            self.get_products()
        except:
            messagebox.showwarning("Cuidado","Debe seleccionar un elemento de la tabla")
        
    def edit_product(self):
        try:
            idsel = self.tree.item(self.tree.selection())["text"] 
            name = self.tree.item(self.tree.selection())["values"][0]
            old_price = self.tree.item(self.tree.selection())["values"][1]
            self.update_wind = Toplevel()
            self.update_wind.title("Update")

            Label(self.update_wind, text = "Old name: ").grid(row = 0, column = 0)
            Entry(self.update_wind, textvariable = StringVar(self.update_wind, value = name), state = "readonly").grid(row = 0, column = 1)
            Label(self.update_wind, text = "Old price: ").grid(row = 1, column = 0)
            Entry(self.update_wind, textvariable = StringVar(self.update_wind, value = old_price), state = "readonly").grid(row = 1, column = 1)

            nombrenuevo = StringVar()
            precionuevo = StringVar()
            Label(self.update_wind, text = "New name: ").grid(row = 0, column = 2)
            Entry(self.update_wind, textvariable = nombrenuevo).grid(row = 0, column = 3)
            Label(self.update_wind, text = "New price: ").grid(row = 1, column = 2)
            Entry(self.update_wind, textvariable = precionuevo).grid(row = 1, column = 3)

            def update_records():
                if len(nombrenuevo.get()) != 0 and len(precionuevo.get()) != 0:
                    query = "update DATOSPRODUCTOS set NOMBRE=?, PRECIO=? where ID=?"
                    parameters = (nombrenuevo.get(), precionuevo.get(), self.tree.item(self.tree.selection())["text"])
                    self.run_query(query,parameters)
                    self.update_wind.destroy()
                    messagebox.showinfo("BBDD", "Se actualizó {} correctamente".format(nombrenuevo.get()))
                else:
                    messagebox.showwarning("Cuidado", "Debe ingresar datos")

            Button(self.update_wind, text = "Update", font = ("Cambria",15), bg = "green", fg = "white", command = update_records).grid(row = 2, columnspan = 4, sticky = "we")

        except:
            messagebox.showwarning("Cuidado","Debe seleccionar un elemento de la tabla")


if __name__ == "__main__":
    window = Tk()
    application = Product(window)

        
    window.mainloop()