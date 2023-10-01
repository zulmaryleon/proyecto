from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla, id_user):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_movimientos, descripcion_movimiento, id_status_movimientos,total, fecha_registro from movimientos where id_usuario = %s", (id_user))
    resultado= cursor.fetchone()
    if resultado:
        for id_movimientos, descripcion_movimiento, id_status_movimientos, total, fecha_registro  in resultado:
            #insercion de datos
            tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, id_status_movimientos,total))
        else:
            return None  # Devolver None si no se encuentra la descripción
    
   