import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#miCursor.execute('''
#    create table PRODUCTOS (               # creación de tabla 
#    CODIGO_ARTICULO varchar(4) PRIMARY KEY,
#    NOMBRE_ARTICULO varchar(50),
#    PRECIO float,
#    SECCION varchar(20))
#''')
#
#productos = [
#    ("AR01", "Pelota", 20, "Juguetería"),
#    ("AR02", "Pantalón", 15, "Confección"),
#    ("AR03", "Destornillador", 25, "Ferretería"),
#    ("AR04", "Jarrón", 45, "Cerámica")
#]
#miCursor.executemany("insert into PRODUCTOS values (?,?,?,?)", productos)

miCursor.execute("insert into PRODUCTOS values ('AR05', 'Tren',15,'Juguetería')")

miConexion.commit() # cada modificación require una confirmación

miConexion.close()