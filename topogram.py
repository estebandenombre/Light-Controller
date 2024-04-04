import librosa
import librosa.display
import matplotlib.pyplot as plt

def visualizar_tempograma(cancion):
    # Cargar la canción
    y, sr = librosa.load(cancion)

    # Calcular el tempograma
    tempograma = librosa.feature.tempogram(y=y, sr=sr)

    # Visualizar el tempograma
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(tempograma, sr=sr, hop_length=512, x_axis='time', y_axis='tempo')
    plt.colorbar(label='Tempogram')
    plt.title('Tempograma de la canción')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Tempo (BPM)')
    plt.tight_layout()
    plt.show()

# Ruta de la canción
cancion = "c4.mp3"  # Reemplaza "tu_cancion.mp3" con la ruta de tu canción

# Visualizar el tempograma de la canción
visualizar_tempograma(cancion)
