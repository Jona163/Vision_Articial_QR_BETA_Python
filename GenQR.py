# Jona163
# Autor: Jonathan Hernández
# Fecha: 25 octubre de 2024 
# Proyecto: VSArtifcial
# GitHub: https://github.com/Jona163

# Importamos las librerias
import pyqrcode
import png
from pyqrcode import QRCode

# CODIGOS QR ID
# Variables
con = 1234

# Generamos los QR
while con <= 1239:

    #id = str('j') +  str(con)
    roster = con
    id = '65' + str(con)
    # Creamos los QR
    qr = pyqrcode.create(65 and id, error= 'L')
    # Guardamos
    qr.png('A' + str(roster) + '.png', scale = 6)
    # Aumentamos con
    con = con + 1
