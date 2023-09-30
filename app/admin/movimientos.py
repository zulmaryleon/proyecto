from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_movimientos, descripcion_movimiento, id_status_movimientos,total, id_usuario, fecha_registro from movimientos")
    resultado= cursor.fetchall()
    for id_movimientos, descripcion_movimiento, id_status_movimientos, total, id_usuario, fecha_registro  in resultado:
        #insercion de datos
        tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, id_status_movimientos,total))