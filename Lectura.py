# Jona163
# Autor: Jonathan Hernández
# Fecha: 25 octubre de 2024 
# Proyecto: VSArtifcial
# GitHub: https://github.com/Jona163

# Importamos librerias para lecturas
import cv2
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

# Creamos la videocaptura
cap = cv2.VideoCapture(0)

# Empezamos
while True:
    # Leemos los frames
    ret, frame = cap.read()
