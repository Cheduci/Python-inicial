import sqlite3

miConexion = sqlite3.connect("PrimeraBase") # nombre de archivo

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO FLOAT, SECCION VARCHAR(20))") # solo se ejecuta la primera vez
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#variosProductos = [
#    ("Camiseta",10,"Deportes"),
#    ("Jarrón", 90, "Cerámica"),
#    ("Camión", 20, "Juguetería")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("Select * from productos")
variosProductos = miCursor.fetchall()
for i in variosProductos:
    print(i)

miConexion.commit() # cada modificación require una confirmación

miConexion.close()