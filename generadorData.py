import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import random
import os
from datosUsuario1 import Persona
import logic

def generar_datos():
    try:
        # Validar entradas
        if not entry_natural.get().isdigit() or not entry_juridico.get().isdigit() or \
           not entry_min_vehiculos.get().isdigit() or not entry_max_personas.get().isdigit():
             messagebox.showerror("Error de Entrada", "Por favor, ingresa solo números enteros válidos en todos los campos.")
             return

        cantidad_natural = int(entry_natural.get())
        cantidad_juridico = int(entry_juridico.get())
        cantidad_minima_vehiculos = int(entry_min_vehiculos.get())
        cantidad_maxima_vehiculos = int(entry_max_personas.get())

        if cantidad_minima_vehiculos > cantidad_maxima_vehiculos:
             messagebox.showerror("Error de Lógica", "La cantidad mínima de vehículos no puede ser mayor que la máxima.")
             return
        
        # Feedback visual de carga (cambiar cursor)
        root.config(cursor="wait")
        root.update()

        # Generamos los datos usando la lógica compartida
        datos = logic.generar_registros(cantidad_natural, cantidad_juridico, cantidad_minima_vehiculos, cantidad_maxima_vehiculos)
            
        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos)

        # Rutas de salida
        excel_file = "datos.xlsx"
        csv_file = "datos.csv"

        # Guardar en Excel
        df.to_excel(excel_file, index=False)
        
        # Guardar en CSV (separado por comas, utf-8 para caracteres especiales)
        df.to_csv(csv_file, index=False, encoding='utf-8-sig', sep=',')
        
        # Restaurar cursor
        root.config(cursor="")

        # Mensaje de éxito con detalles
        mensaje = (
            f"¡Proceso Completado Exitosamente!\n\n"
            f"Se han generado {len(datos)} registros de {cantidad_natural + cantidad_juridico} personas.\n"
            f"- Naturales: {cantidad_natural}\n"
            f"- Jurídicas: {cantidad_juridico}\n"
            f"Archivos creados:\n"
            f"- {os.path.abspath(excel_file)}\n"
            f"- {os.path.abspath(csv_file)}"
        )
        messagebox.showinfo("Generación Exitosa", mensaje)

    except Exception as e:
        root.config(cursor="")
        messagebox.showerror("Error Inesperado", f"Ocurrió un error durante la generación:\n{str(e)}")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Datos Vía Rápida")
root.geometry("450x330")
root.resizable(False, False)

# Estilo
style = ttk.Style()
style.theme_use('clam') # Un tema un poco más limpio que el default

# Frame principal con padding
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
lbl_titulo = ttk.Label(main_frame, text="Configuración de Generación", font=('Helvetica', 12, 'bold'))
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Crear y posicionar widgets con grid
# Fila 1: Cantidad de Personas Naturales
lbl_natural = ttk.Label(main_frame, text="Cantidad de Personas Naturales:")
lbl_natural.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_natural = ttk.Entry(main_frame, width=15)
entry_natural.grid(row=1, column=1, padx=5, pady=5)
entry_natural.insert(0, "5") # Valor por defecto

# Fila 2: Cantidad de Personas Jurídicas
lbl_juridico = ttk.Label(main_frame, text="Cantidad de Personas Jurídicas:")
lbl_juridico.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_juridico = ttk.Entry(main_frame, width=15)
entry_juridico.grid(row=2, column=1, padx=5, pady=5)
entry_juridico.insert(0, "5") # Valor por defecto

# Fila 3: Mínimo de Vehículos
lbl_min_veh = ttk.Label(main_frame, text="Mínimo de Vehículos por Usuario:")
lbl_min_veh.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_min_vehiculos = ttk.Entry(main_frame, width=15)
entry_min_vehiculos.grid(row=3, column=1, padx=5, pady=5)
entry_min_vehiculos.insert(0, "1") # Valor por defecto

# Fila 4: Máximo de Vehículos
lbl_max_veh = ttk.Label(main_frame, text="Máximo de Vehículos por Usuario:")
lbl_max_veh.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
entry_max_personas = ttk.Entry(main_frame, width=15)
entry_max_personas.grid(row=4, column=1, padx=5, pady=5)
entry_max_personas.insert(0, "3") # Valor por defecto

# Fila 5: Botón de Acción
btn_generar = ttk.Button(main_frame, text="Generar Datos (Excel y CSV)", command=generar_datos)
btn_generar.grid(row=5, column=0, columnspan=2, pady=(20, 0), ipady=5, sticky=tk.EW)

# Pie de página (créditos o versión)
lbl_footer = ttk.Label(main_frame, text="v1.1 - Generador Vía Rápida", font=('Helvetica', 8), foreground="gray")
lbl_footer.grid(row=6, column=0, columnspan=2, pady=(20, 0))

# Centrar la ventana en la pantalla (opcional, cálculo simple)
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Iniciar bucle de eventos
root.mainloop()
