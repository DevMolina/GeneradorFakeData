from flask import Flask, render_template, request, send_file
import pandas as pd
import io
import zipfile
import logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        cantidad = int(request.form['cantidad'])
        min_veh = int(request.form['min_veh'])
        max_veh = int(request.form['max_veh'])
        
        # Validaciones básicas
        if min_veh > max_veh:
            return "Error: El mínimo de vehículos no puede ser mayor que el máximo.", 400

        # Generar datos usando la lógica compartida
        datos = logic.generar_registros(cantidad, min_veh, max_veh)
        df = pd.DataFrame(datos)

        # Crear archivos en memoria
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)

        csv_buffer = io.BytesIO()
        df.to_csv(csv_buffer, index=False, encoding='utf-8-sig') # Separador por defecto es coma
        csv_buffer.seek(0)

        # Crear ZIP en memoria
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr('datos.xlsx', excel_buffer.getvalue())
            zip_file.writestr('datos.csv', csv_buffer.getvalue())
        
        zip_buffer.seek(0)

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='datos_generados.zip'
        )

    except Exception as e:
        return f"Error al generar datos: {str(e)}", 500

if __name__ == '__main__':
    # Ejecutar en modo debug para desarrollo
    app.run(debug=True, port=5000)
