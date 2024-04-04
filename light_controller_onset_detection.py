import librosa
import librosa.display
import matplotlib.pyplot as plt

# Cargar una muestra de audio incorporada (ejemplo: Drum loop)
y, sr = librosa.load('tu_cancion.mp3')

# Calcular la envolvente de fuerza de inicio
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Encontrar eventos de inicio
onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

# Imprimir el vector de tiempos donde se inicia un nuevo evento
print("Tiempo de inicio de eventos:", librosa.times_like(onset_env)[onsets])

# Graficar la envolvente de fuerza de inicio y los eventos de inicio detectados
plt.figure(figsize=(10, 4))
plt.plot(librosa.times_like(onset_env), onset_env, label='Onset Strength')
plt.vlines(librosa.times_like(onset_env)[onsets], 0, onset_env.max(), color='r', alpha=0.9, label='Detected Onsets')
plt.legend()
plt.title('Onset Detection')
plt.tight_layout()
plt.show()
