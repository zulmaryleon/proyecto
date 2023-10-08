import tkinter as tk
from app.venta import confirmar, cancelar, calcular
def hacer_venta(id_producto, ventana, cantidad, precio, tabla_producto, cantidad_actual, username):
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar usuario con ID: {id_producto}")
    global conexion #definimos la variable conexion como global
    if int(cantidad.get()) > cantidad_actual:
        ventana_confirmacion = tk.Toplevel()

        ventana_confirmacion.title("Ops.. No hay suficiente cantidad.")

        # Etiqueta de confirmación
        etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"La cantidad '{int(cantidad.get())}' supera a '{cantidad_actual}' no hay suficiente en el inventario, por favor intente de nuevo con una cantidad existente")
        etiqueta_confirmacion.pack()

        boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar(ventana_confirmacion))
        boton_cancelar.pack()

    else:
        total = calcular(cantidad, precio)
        print(f"cantidad actual: {cantidad_actual}")

        ventana_confirmacion = tk.Tk()
        ventana_confirmacion.title("Confirmación")
    
        # Etiqueta de confirmación
        etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"Total a pagar '{total}'$")
        etiqueta_confirmacion.pack()

        # Botones de confirmar y cancelar
        boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=lambda:confirmar(id_producto, tabla_producto, ventana, ventana_confirmacion, cantidad))
        boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=lambda:cancelar(ventana_confirmacion))

        boton_confirmar.pack()
        boton_cancelar.pack()

    ventana_confirmacion.mainloop()