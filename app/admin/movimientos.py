from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

def datos_tabla_movimientos(tabla):
    try:
        # Eliminamos todos los elementos antes de actualizar
        tabla.delete(*tabla.get_children())

        cursor = conexion.cursor()
        cursor.execute("SELECT m.id_movimientos, p.descripcion_producto, m.total, u.usuario, s.descripcion_status FROM movimientos m INNER JOIN usuario u ON m.id_usuario = u.id_usuario INNER JOIN productos p ON m.descripcion_movimiento = p.id_producto INNER JOIN status_movimientos s ON m.id_status_movimientos = s.id_status_movimientos ORDER BY m.id_movimientos DESC")

        resultado = cursor.fetchall()
        for id_movimientos, descripcion_movimiento, total, usuario, status in resultado:
            total = str(total) + "$"
            # Inserción de datos
            tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, total, usuario, status))

    except Exception as e:
        print("Error en la consulta SQL:", e)

def actualizar(tabla):
    datos_tabla_movimientos(tabla) 