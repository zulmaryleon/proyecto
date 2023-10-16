from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    #cursor.execute("select m.id_movimientos, m.descripcion_movimiento, m.total, u.usuario from movimientos m INNER JOIN usuario u ON m.id_usuario = u.id_usuario")
    cursor.execute("SELECT m.id_movimientos, p.descripcion_producto, m.total, u.usuario FROM movimientos m INNER JOIN usuario u ON m.id_usuario = u.id_usuario INNER JOIN productos p ON m.descripcion_movimiento = p.id_producto")

    resultado= cursor.fetchall()
    for id_movimientos, descripcion_movimiento, total, usuario in resultado:
        total = str(total) + "$"
        #inserción de datos
        tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, total, usuario))
