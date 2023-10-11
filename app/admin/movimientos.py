from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select m.id_movimientos, m.descripcion_movimiento, m.total, u.usuario from movimientos m INNER JOIN usuario u ON m.id_usuario = u.id_usuario")

    resultado= cursor.fetchall()
    for id_movimientos, descripcion_movimiento, usuario, total  in resultado:
        #insercion de datos
        tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, usuario, total))