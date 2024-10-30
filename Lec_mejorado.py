# Jona163
# Autor: Jonathan Hernández
# Fecha: 25 octubre de 2024 
# Proyecto: VSArtifcial
# GitHub: https://github.com/Jona163

# Importamos librerías necesarias
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Configuramos la videocaptura
cap = cv2.VideoCapture(0)

# Iniciamos el bucle principal
while True:
    # Leemos el frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar la imagen")
        break
