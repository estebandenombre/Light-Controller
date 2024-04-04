import librosa
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import pygame
import threading

# Función para cambiar el color de la ventana emergente según la energía
def cambiar_color(ventana, intensidad, umbral):
    if intensidad > umbral:
        ventana.config(bg='red')
    else:
        ventana.config(bg='black')

# Función para visualizar la gráfica del sonido con un umbral y marcar los instantes donde se supera el umbral
def visualizar_grafica_con_umbral(cancion, umbral):
    # Cargar la canción
    y, sr = librosa.load(cancion)

    # Calcular la energía de la señal de audio en cada instante de tiempo
    energia = librosa.feature.rms(y=y)

    # Obtener los tiempos correspondientes a cada muestra de energía
    duracion = librosa.get_duration(y=y, sr=sr)
    tiempos = np.linspace(0, duracion, num=len(energia[0]))

    # Identificar los instantes de tiempo donde se supera el umbral
    instantes_superados = tiempos[energia[0] > umbral]

    # Crear una ventana emergente
    ventana_popup = tk.Tk()
    ventana_popup.geometry("200x200")
    ventana_popup.title("Ventana Emergente")

    # Función para reproducir la canción de fondo en un hilo separado
    def reproducir_cancion():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play()

    # Iniciar la reproducción de la canción de fondo en un hilo separado
    t = threading.Thread(target=reproducir_cancion)
    t.start()

    # Bucle para cambiar el color de la ventana según la energía
    for tiempo, intensidad in zip(tiempos, energia[0]):
        # Cambiar el color de la ventana según la intensidad actual y el umbral
        cambiar_color(ventana_popup, intensidad, umbral)
        ventana_popup.update()
        # Pausa para simular el tiempo real
        ventana_popup.after(int(1000 * (tiempos[1] - tiempos[0])))  

    ventana_popup.mainloop()

# Parámetros
umbral = 0.15 # Umbral constante

# Visualizar la gráfica del sonido con el umbral especificado y los instantes superados
visualizar_grafica_con_umbral("c3º.mp3", umbral)
