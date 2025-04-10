import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
from datosUsuario1 import Persona

def generar_excel():
    try:
        cantidad_usuarios = int(entry_usuarios.get())
        cantidad_minima_vehiculos = int(entry_min_vehiculos.get())
        cantidad_maxima_vehiculos = int(entry_max_personas.get())
        
        # Generamos los datos de las personas
        personas = [Persona("Natural" if random.random() < 0.5 else "Juridico", cantidad_minima_vehiculos, cantidad_maxima_vehiculos) for _ in range(cantidad_usuarios)]

        datos = []
        for persona in personas:
            for vehiculo in persona.vehiculos:
                datos.append({
                    "Razon Social": persona.razon_social,
                    "Nombre Representante": persona.nombre,
                    "Apellidos": persona.apellido,
                    "Documento": persona.documento,
                    "CódigoVerificación": persona.cod_ver,
                    "NIT": persona.nit,
                    "ResponsabilidadFiscal": persona.res_fiscal,
                    "Dirección": persona.dir,
                    "Pais": persona.pais,
                    "Departamento": persona.dep,
                    "Municipio": persona.mun,
                    "email": persona.email,
                    "Telefono": persona.cel,
                    "Telefono_Emergencia": persona.tel_eme,
                    "Placa": vehiculo.placa,
                    "Categoria": vehiculo.categoria
                })
            
        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos)

        # Guardar el DataFrame en un archivo de Excel
        df.to_excel("datos.xlsx", index=False)
                
        messagebox.showinfo("Excel Generado", "El archivo datos.xlsx ha sido generado correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de datos de usuarios Vía Rápida - Excel")

# Crear y posicionar widgets
label_usuarios = tk.Label(root, text="Cantidad de Usuarios:")
label_usuarios.grid(row=0, column=0, padx=5, pady=5)
entry_usuarios = tk.Entry(root)
entry_usuarios.grid(row=0, column=1, padx=5, pady=5)

label_min_vehiculos = tk.Label(root, text="Cantidad Mínima de Vehículos:")
label_min_vehiculos.grid(row=1, column=0, padx=5, pady=5)
entry_min_vehiculos = tk.Entry(root)
entry_min_vehiculos.grid(row=1, column=1, padx=5, pady=5)

label_max_personas = tk.Label(root, text="Cantidad Máxima de Vehículos:")
label_max_personas.grid(row=2, column=0, padx=5, pady=5)
entry_max_personas = tk.Entry(root)
entry_max_personas.grid(row=2, column=1, padx=5, pady=5)

boton_generar_excel = tk.Button(root, text="Generar Excel", command=generar_excel)
boton_generar_excel.grid(row=3, columnspan=2, padx=5, pady=5)

# Iniciar bucle de eventos
root.mainloop()
