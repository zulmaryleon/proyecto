import os
import sys

def salir(dashboard):
    dashboard.destroy()
    
    # Reiniciar la aplicación
    python_executable = sys.executable
    os.execl(python_executable, python_executable, *sys.argv)