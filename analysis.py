import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

import librosa
import librosa.display
import IPython.display as ipd

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
    
    # Calcular el tempo de la canción
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    return tempo

# Función principal
def main():
    #########################################################
    pygame.init()
    pygame.mixer.init()

    # Ruta de la canción
    cancion = "c3.mp3"  # Reemplaza "tu_cancion.mp3" con la ruta de tu canción

    # Cargar y reproducir la canción
    #pygame.mixer.music.load(cancion)
    #pygame.mixer.music.play()

    ######################################################

    y, sr = librosa.load(cancion)
    print(f'y: {y[:10]}')
    print(f'shape y: {y.shape}')
    print(f'sr: {sr}')
    pd.Series(y).plot(figsize=(10, 5),
                  lw=1,
                  title='Raw Audio Example',
                 color=color_pal[0])
    #plt.show()

    ################################################################
    # Trimming leading/lagging silence
    y_trimmed, _ = librosa.effects.trim(y, top_db=20)
    pd.Series(y_trimmed).plot(figsize=(10, 5),
                  lw=1,
                  title='Raw Audio Trimmed Example',
                 color=color_pal[1])
    plt.show()
    ################################################################

    # Compute local onset autocorrelation
    hop_length = 512
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=sr,
                                              hop_length=hop_length)
    # Compute the auto-correlation tempogram, unnormalized to make comparison easier
    ac_tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,
                                         hop_length=hop_length, norm=None)
   
    fig, ax = plt.subplots(nrows=3, sharex=True)
    ax[0].plot(librosa.times_like(oenv), oenv, label='Onset strength')
    ax[0].legend(frameon=True)
    ax[0].label_outer()
    librosa.display.specshow(np.abs(tempogram), sr=sr, hop_length=hop_length,
                         x_axis='time', y_axis='fourier_tempo', cmap='magma',
                         ax=ax[1])
    ax[1].set(title='Fourier tempogram')
    ax[1].label_outer()
    librosa.display.specshow(ac_tempogram, sr=sr, hop_length=hop_length,
                         x_axis='time', y_axis='tempo', cmap='magma',
                         ax=ax[2])
    ax[2].set(title='Autocorrelation tempogram')


if __name__ == "__main__":
    main()
