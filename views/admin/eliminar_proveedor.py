import tkinter as tk
from app.admin.proveedor import confirmar_eliminar, cancelar_eliminar, consultar_proveedor
def eliminar_proveedor(id_proveedor, tabla_proveedor):
    # Aquí debes implementar la lógica para eliminar el usuario con el ID proporcionado.
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar proveedor con ID: {id_proveedor}")

    datos = consultar_proveedor(id_proveedor)
    
    nombre_proveedor = datos.get("nombre", "")

    # Crear una ventana Tkinter para la confirmación
    ventana_confirmacion = tk.Tk()
    ventana_confirmacion.title("Confirmación")

    # Etiqueta de confirmación
    etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar el proveedor '{nombre_proveedor}' (ID: {id_proveedor})?")
    etiqueta_confirmacion.pack()

    # Botones de confirmar y cancelar
    boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=lambda:confirmar_eliminar(id_proveedor, ventana_confirmacion, tabla_proveedor, nombre_proveedor))
    boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar_eliminar(ventana_confirmacion))

    boton_confirmar.pack()
    boton_cancelar.pack()

    ventana_confirmacion.mainloop()