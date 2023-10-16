from tkinter import messagebox
from app.database import get_database_connection
import datetime, time

def datos_tabla_inventario(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select i.id_producto, i.descripcion_producto, i.cantidad_total, i.fecha_vencimiento, p.nombre, i.costo_mayor, i.precio_unitario  from productos i INNER JOIN proveedor p ON i.id_proveedor = p.id_proveedor")
    resultado= cursor.fetchall()
    for id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario in resultado:
        precio_unitario_con_signo = str(precio_unitario) + "$"
        costo_mayor = str(costo_mayor) + "$"

        #insercion de datos
        tabla.insert("", "end", values=(id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario_con_signo)) 

         # Asignar etiquetas (tags) según las reglas definidas
        if cantidad_total < 1:  # Si hay menos de 1 productos, etiquetar como "rojo"
            tabla.item(tabla.get_children()[-1], tags=("rojo",))
        elif cantidad_total >= 1 and cantidad_total <= 10:  # Por ejemplo, si quedan 10 o menos productos, etiquetar como "amarillo"
            
            tabla.item(tabla.get_children()[-1], tags=("amarillo",))
        else:   # Si quedan entre 6 y 10 productos, etiquetar como "verde"
            tabla.item(tabla.get_children()[-1], tags=("verde",))
# Función para consultar un usuario en MySQL
conexion = get_database_connection()
def confirmar(id_producto, tabla_producto, ventana, ventana_confirmacion, cantidad):
	global conexion  # Indicar que estás utilizando la variable global

	cantidad_val = cantidad.get()
	fecha_actual = datetime.date.today()
	print(f"Venta: {id_producto}")
	
	try:
		if not conexion.is_connected():
			conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

		# Abrir cursor
		cursor = conexion.cursor()
		consulta = "UPDATE productos SET cantidad_total = cantidad_total - %s WHERE id_producto = %s"
		cursor.execute(consulta, (cantidad_val, id_producto))

		# Consulta para registrar el movimiento
		consulta_insert = "INSERT INTO movimientos (descripcion_movimiento, id_status_movimientos, total, id_usuario, fecha_registro) VALUES (%s, %s, %s, %s, %s)"
		cursor.execute(consulta_insert, (id_producto, '2', cantidad_val, '13', fecha_actual))

		conexion.commit()

		# Actualizar tabla
		datos_tabla_inventario(tabla_producto)

		cursor.close()
		ventana.destroy()
		ventana_confirmacion.destroy()
		messagebox.showinfo("Producto vendido", 'Se ha vendido el producto')

	except Exception as e:
		conexion.rollback()
		messagebox.showerror("Error", f"No se ha podido vender el producto: {str(e)}")

def calcular(precio, cantidad):
	cantidad_val = float(cantidad.get())
	precio_val = float(precio.get())
	calculo = cantidad_val * precio_val
	return calculo

def cancelar(ventana):
	messagebox.showinfo("Información", "Operación de venta cancelada.")
	ventana.destroy()