import pandas as pd
import os
import logic

def test_csv_generation():
    print("Iniciando prueba de generación con lógica compartida...")
    
    cantidad_usuarios = 5
    cantidad_minima_vehiculos = 1
    cantidad_maxima_vehiculos = 2
    
    # Generamos los datos usando el módulo logic
    try:
        datos = logic.generar_registros(cantidad_usuarios, cantidad_minima_vehiculos, cantidad_maxima_vehiculos)
        print(f"Se generaron {len(datos)} registros.")
    except Exception as e:
        print(f"Error en logic.generar_registros: {e}")
        return

    # Crear un DataFrame con los datos
    df = pd.DataFrame(datos)
    
    csv_file = "test_datos.csv"
    
    # Intentar guardar en CSV
    try:
        df.to_csv(csv_file, index=False, encoding='utf-8-sig', sep=',')
        print(f"Archivo {csv_file} generado correctamente.")
    except Exception as e:
        print(f"Error al generar CSV: {e}")
        return

    # Verificar que el archivo existe y es legible
    if os.path.exists(csv_file):
        try:
            df_read = pd.read_csv(csv_file)
            print("Archivo CSV leído correctamente.")
            print(f"Columnas encontradas: {list(df_read.columns)}")
            
            expected_columns = ["Nombre / Razón Social", "Representante Legal", "Apellidos", "Documento", "DV", "Tipo Documento", 
                                "Responsabilidad Fiscal", "Dirección", "País", "Departamento", "Municipio", "Email", 
                                "Teléfono", "Teléfono Emergencia", "Placa Vehículo", "Categoría Vehículo"]
            
            if all(col in df_read.columns for col in expected_columns):
                print("Todas las columnas esperadas están presentes.")
            else:
                print("Faltan algunas columnas esperadas.")
                
            print(f"Total filas generadas: {len(df_read)}")
            print("TEST PASSED")
        except Exception as e:
            print(f"Error leyendo el CSV generado: {e}")
    else:
        print("El archivo CSV no se encontró.")

    # Limpieza
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print("Archivo de prueba eliminado.")

if __name__ == "__main__":
    test_csv_generation()
