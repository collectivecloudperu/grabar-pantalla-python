import cv2
import numpy as np
import pyautogui
import keyboard

tamanio_pantalla = pyautogui.size()
fps = 30
cv = cv2.VideoWriter_fourcc(*"XVID")
salida = "video.mp4"
video = cv2.VideoWriter(salida, cv, fps, (tamanio_pantalla.width, tamanio_pantalla.height))

print("Grabando... Presiona 'q' para detener la grabación.")

while True:
    tamanio = pyautogui.screenshot()
    frame = np.array(tamanio)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    video.write(frame)

    if keyboard.is_pressed('q'):
        print("GRabación detenida.")
        break

video.release()
print(f"Video grabado como:{salida}")