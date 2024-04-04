import librosa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import pygame
import threading
import time
from itertools import cycle

sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

# Función para alternar el color de la ventana entre blanco y negro
def alternar_color(ventana, intervalo):
    colores = ["black", "white"]  # Lista de colores alternativos
    indice_color = 0  # Índice del color actual en la lista
    while pygame.mixer.music.get_busy():
        color_actual = colores[indice_color]
        ventana.configure(bg=color_actual)
        indice_color = (indice_color + 1) % len(colores)  # Cambiar al siguiente color en la lista
        time.sleep(intervalo)  # Esperar el intervalo calculado

# Función para calcular el tempo de la canción con librosa
def obtener_tempo(cancion):
    # Cargar la canción
    y, sr = librosa.load(cancion)
    
    # Calcular el tempo de la canción dinámicamente
    tempo_dynamic = librosa.feature.tempo(y=y, sr=sr, aggregate=None, std_bpm=4)
    
    # Calcular el tempo promedio
    tempo = np.mean(tempo_dynamic)
    
    return tempo

# Función principal
def main():
    #########################################################
    pygame.init()
    pygame.mixer.init()

    # Ruta de la canción
    cancion = "tu_cancion.mp3"  # Reemplaza "tu_cancion.mp3" con la ruta de tu canción

    # Cargar y reproducir la canción
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

    # Calcular el intervalo de encendido de la ventana basado en el tempo de la canción
    # Utilizamos un tempo dinámico para adaptarnos a posibles cambios en el tempo de la canción
    while pygame.mixer.music.get_busy():
        tempo = obtener_tempo(cancion)
        intervalo = 60 / tempo

        # Crear una ventana emergente
        ventana_popup = tk.Tk()
        ventana_popup.geometry("200x200")
        ventana_popup.title("Ventana Emergente")

        # Crear un hilo para controlar el parpadeo de la ventana emergente
        t = threading.Thread(target=alternar_color, args=(ventana_popup, intervalo))
        t.start()

        ventana_popup.mainloop()

if __name__ == "__main__":
    main()
