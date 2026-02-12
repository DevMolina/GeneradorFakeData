import unittest
from web_app import app
import io
import zipfile

class WebAppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generador de Datos', response.data)

    def test_generate(self):
        data = {
            'cantidad': '5',
            'min_veh': '1',
            'max_veh': '2'
        }
        response = self.client.post('/generate', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/zip')
        
        # Verificar contenido del zip
        zip_buffer = io.BytesIO(response.data)
        with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
            self.assertIn('datos.xlsx', zip_file.namelist())
            self.assertIn('datos.csv', zip_file.namelist())

if __name__ == '__main__':
    unittest.main()
