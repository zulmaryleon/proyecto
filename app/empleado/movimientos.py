from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla, id_user):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("SELECT id_movimientos, descripcion_movimiento, id_status_movimientos, total, fecha_registro FROM movimientos WHERE id_usuario = %s", (id_user,))
    resultados = cursor.fetchall()  # Obtenemos todas las filas de resultados

    for id_movimientos, descripcion_movimiento, id_status_movimientos, total, fecha_registro  in resultados:
        #insercion de datos
        tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, id_status_movimientos,total))
    
    cursor.close()  # Cierra el cursor cuando hayas terminado