# Jona163
# Autor: Jonathan Hernández
# Fecha: 25 octubre de 2024 
# Proyecto: VSArtifcial
# GitHub: https://github.com/Jona163

# Importamos las librerías necesarias
import pyqrcode
import png
from pyqrcode import QRCode

# Generamos los códigos QR de identificación
inicio_id = 1234  # ID inicial
fin_id = 1239     # ID final

# Iteramos para crear y guardar los códigos QR
for con in range(inicio_id, fin_id + 1):
    # Creamos el identificador con prefijo '65'
    id_qr = f'65{con}'
    
    # Generamos el QR con el identificador
    qr = pyqrcode.create(id_qr, error='L')
    
    # Guardamos el archivo PNG con el nombre correspondiente
    qr.png(f'A{id_qr}.png', scale=6)

print("Códigos QR generados y guardados correctamente.")
