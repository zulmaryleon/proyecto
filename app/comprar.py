from tkinter import messagebox
from app.database import get_database_connection
from app.admin.inventario import datos_tabla_inventario
import datetime, time

# Función para consultar un usuario en MySQL
conexion = get_database_connection()
def confirmar(id_producto, tabla_producto, ventana, ventana_confirmacion, cantidad, username):
	global conexion  # Indicar que estás utilizando la variable global

	cantidad_val = cantidad.get()
	fecha_actual = datetime.date.today()
	print(f"Compra: {id_producto}")

	try:
		if not conexion.is_connected():
			conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
		
		# Abrir cursor
		cursor = conexion.cursor()
		consulta = "UPDATE productos SET cantidad_total = cantidad_total + %s WHERE id_producto = %s"
		cursor.execute(consulta, (cantidad_val, id_producto))

		conexion.commit()
		
		# Actualizar tabla
		datos_tabla_inventario(tabla_producto)

		cursor.close()
		ventana.destroy()
		ventana_confirmacion.destroy()
		messagebox.showinfo("Producto comprado", 'Se ha comprado el producto')
	
	except Exception as e:
		conexion.rollback()
		messagebox.showerror("Error", f"No se ha podido hacer inventario: {str(e)}")

def calcular(precio, cantidad):
	cantidad_val = float(cantidad.get())
	precio_val = float(precio.get())
	calculo = cantidad_val * precio_val
	return calculo

def cancelar(ventana):
	messagebox.showinfo("Información", "Operación de compra cancelada.")
	ventana.destroy()