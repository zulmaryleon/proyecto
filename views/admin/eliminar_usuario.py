import tkinter as tk
from app.admin.usuarios import confirmar_eliminar, cancelar_eliminar, consultar_usuario
def eliminar_usuario(id_usuario, tabla_usuarios):
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar usuario con ID: {id_usuario}")
    global conexion #definimos la variable conexion como global

    ventana_confirmacion = tk.Tk()
    ventana_confirmacion.title("Confirmación")
    datos = consultar_usuario(id_usuario)
    
    nombre_usuario = datos.get("usuario", "")
 
    # Etiqueta de confirmación
    etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar al usuario '{nombre_usuario}' (ID: {id_usuario})?")
    etiqueta_confirmacion.pack()

    # Botones de confirmar y cancelar
    boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=lambda:confirmar_eliminar(id_usuario, tabla_usuarios, ventana_confirmacion, nombre_usuario))
    boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar_eliminar(ventana_confirmacion))

    boton_confirmar.pack()
    boton_cancelar.pack()

    ventana_confirmacion.mainloop()