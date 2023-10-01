from tkinter import messagebox
from app.database import get_database_connection
from views.dashboard import crear_vista_dashboard  # Importa la función para crear la vista del panel de control

# Función para manejar el evento Enter en la ventana principal
def on_enter(event, usuario_entry, password_entry, ventana):
    iniciar_sesion(usuario_entry, password_entry, ventana)


def iniciar_sesion(usuario_entry, password_entry, ventana):
    usuario = usuario_entry.get()
    contrasena = password_entry.get()

    conexion = get_database_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("select usuario, id_usuario from usuario where usuario = %s and contraseña = %s", (usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado is not None:
                username, id_usuario = resultado  # Desempaqueta los valores de la tupla
                messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
                ventana.destroy()  # Cierra la ventana de inicio de sesión actual
                
                crear_vista_dashboard(id_usuario)
  
            else:
                messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas")

        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            conexion.close()
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")

# Otras funciones relacionadas con el inicio de sesión si las tienes...
