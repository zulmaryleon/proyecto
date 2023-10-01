import tkinter as tk
from app.admin.inventario import confirmar_eliminar, cancelar_eliminar, consultar_producto

def eliminar_producto(id_producto, tabla):
    # Aquí debes implementar la lógica para eliminar el usuario con el ID proporcionado.
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar producto con ID: {id_producto}")

    datos = consultar_producto(id_producto)
    
    descripcion_producto = datos.get("descripcion_producto", "")

    # Crear una ventana Tkinter para la confirmación
    ventana_confirmacion = tk.Tk()
    ventana_confirmacion.title("Confirmación")

    # Etiqueta de confirmación
    etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar el proveedor '{descripcion_producto}' (ID: {id_producto})?")
    etiqueta_confirmacion.pack()

    # Botones de confirmar y cancelar
    boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=lambda:confirmar_eliminar(id_producto, ventana_confirmacion, tabla, descripcion_producto))
    boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar_eliminar(ventana_confirmacion))

    boton_confirmar.pack()
    boton_cancelar.pack()

    ventana_confirmacion.mainloop()