import tkinter as tk
from app.comprar import confirmar, cancelar, calcular
def hacer_compra(id_producto, precio,cantidad, proveedores_editar, ventana, tabla_producto, username):
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar usuario con ID: {id_producto}")
    global conexion #definimos la variable conexion como global

    total = calcular(cantidad, precio)

    ventana_confirmacion = tk.Tk()
    ventana_confirmacion.title("Confirmación")
 
    # Etiqueta de confirmación
    etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"Total a pagar '{total}'$")
    etiqueta_confirmacion.pack()

    # Botones de confirmar y cancelar
    boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=lambda:confirmar(id_producto, tabla_producto, ventana, ventana_confirmacion, cantidad, username))
    boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar(ventana_confirmacion))

    boton_confirmar.pack()
    boton_cancelar.pack()

    ventana_confirmacion.mainloop()