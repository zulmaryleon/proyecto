# Importa las funciones para obtener ventas y compras
import tkinter as tk
from tkinter import messagebox, ttk
from app.admin.usuarios import consultar_usuario, datos_tabla_usuarios, crear_usuario
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

def usuarios(contenedor_derecho):
	# Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Usuarios", fg=c_blanco, bg=c_verde, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Crear un Frame principal para contener todo
    frame_principal = tk.Frame(contenedor_derecho, bg="white")
    frame_principal.pack(fill="both", expand=True)

    # Crear un Frame para contener el buscador
    frame_buscador = tk.Frame(frame_principal, bg="white")
    frame_buscador.pack(side="top", fill="x")

    # Crear la entrada de búsqueda
    entrada_busqueda = tk.Entry(frame_buscador)
    entrada_busqueda.pack(side="left")

    # Crear el botón de búsqueda
    boton_buscar = tk.Button(frame_buscador, text="Buscar", command=lambda: buscar(tabla_usuarios, entrada_busqueda))
    boton_buscar.pack(side="left")

    # Crear la tabla de usuario en el Frame principal
    tabla_usuarios = ttk.Treeview(frame_principal, columns=("id", "Usuario", "Rol", "Registrado"), show="headings", style="Custom.Treeview")

    tabla_usuarios.heading("id", text="#")
    tabla_usuarios.heading("Usuario", text="Usuario")
    tabla_usuarios.heading("Rol", text="Rol del Usuario")
    tabla_usuarios.heading("Registrado", text="Fecha de registro")

    # Ajustar tamaño de columnas
    tabla_usuarios.column("id", width=50)
    tabla_usuarios.column("Usuario", width=200)
    tabla_usuarios.column("Rol", width=200)
    tabla_usuarios.column("Registrado", width=200)

    # contenido de la tabla
    datos_tabla_usuarios(tabla_usuarios)

    # Mostrar la tabla en el Frame principal
    tabla_usuarios.pack(fill="both", expand=True)

    # Botón de crear usuario
    boton_guardar_usuario = tk.Button(frame_principal, text="Crear Usuario", command=crear_usuario)
    boton_guardar_usuario.pack(side="left", padx=10, pady=5)

    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(frame_principal, text="Editar", command=lambda: editar_usuario(id_usuario))
    eliminar_button = tk.Button(frame_principal, text="Eliminar", command=lambda: eliminar_usuario(id_usuario))

    # Configurar la acción de selección de usuario
    def seleccionar_usuario(event):
        item_seleccionado = tabla_usuarios.selection()
        if item_seleccionado:
            id_usuario = tabla_usuarios.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_usuario(id_usuario))
            eliminar_button.configure(command=lambda: eliminar_usuario(id_usuario))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()

    tabla_usuarios.bind("<<TreeviewSelect>>", seleccionar_usuario)
