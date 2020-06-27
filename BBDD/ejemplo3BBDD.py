import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#miCursor.execute('''
#    create table PRODUCTOS (
#    ID INTEGER PRIMARY KEY autoincrement,
#    NOMBRE_ARTICULO varchar(50) UNIQUE,
#    PRECIO float,
#    SECCION varchar(20))
#''')
#
#productos = [
#    ("Pelota", 20, "Juguetería"),
#    ("Pantalón", 15, "Confección"),
#    ("Destornillador", 25, "Ferretería"),
#    ("Jarrón", 45, "Cerámica")
#]
#miCursor.executemany("insert into PRODUCTOS values (Null,?,?,?)", productos)

miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Pantalones'")

miConexion.commit() # cada modificación require una confirmación

miConexion.close()