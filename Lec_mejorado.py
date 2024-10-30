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

    # Detectamos y procesamos los códigos QR
    for qr_code in decode(frame):
        # Decodificamos la información del QR
        info = qr_code.data.decode('utf-8')
        tipo = int(info[0:2])  # Extraemos el tipo de usuario
        pts = np.array([qr_code.polygon], np.int32).reshape((-1, 1, 2))  # Coordenadas del QR
        xi, yi = qr_code.rect.left, qr_code.rect.top  # Posición de texto

        # Determinamos el tipo de usuario y configuramos el mensaje y color
        if tipo == 69:  # Usuario accionista
            color, prefix, msg = (255, 255, 0), 'E0', "El usuario es accionista de la empresa"
        elif tipo == 71:  # Usuario ejecutivo
            color, prefix, msg = (255, 0, 255), 'G0', "El usuario pertenece a la sección ejecutiva"
        elif tipo == 83:  # Usuario salud
            color, prefix, msg = (0, 255, 255), 'S0', "El usuario pertenece a la sección salud"
        elif tipo == 65:  # Usuario general
            color, prefix, msg = (0, 255, 0), 'A0', "Usuario general"
        else:
            color, prefix, msg = (0, 0, 255), 'UNK', "Tipo desconocido"

        # Dibujamos el polígono y mostramos el texto con información del usuario
        cv2.polylines(frame, [pts], True, color, 5)
        cv2.putText(frame, f'{prefix}{info[2:]}', (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        print(f"{msg} | Número de Identificación: {prefix}{info[2:]}")
    
    # Mostramos el frame en pantalla
    cv2.imshow(" LECTOR DE QR", frame)

    # Salida si se presiona 'Esc'
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberamos la captura y cerramos ventanas
cap.release()
cv2.destroyAllWindows()
