import librosa
import matplotlib.pyplot as plt
import soundfile as sf

# Cargar un archivo de audio (ejemplo: Piano)
y, sr = librosa.load('c4.mp3')

# Realizar separación de fuente armónica-percursiva
harmonic, percussive = librosa.effects.hpss(y)

# Visualizar el componente armónico
plt.figure(figsize=(10, 4))
plt.plot(harmonic)
plt.title('Componente Armónico')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.tight_layout()
plt.show()

# Visualizar el componente percusivo
plt.figure(figsize=(10, 4))
plt.plot(percussive)
plt.title('Componente Percusivo')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.tight_layout()
plt.show()

# Guardar la parte armónica en un archivo de audio .mp3
sf.write('armónico.mp3', harmonic, sr, format='mp3')

# Guardar la parte percusiva en un archivo de audio .mp3
sf.write('percusivo.mp3', percussive, sr, format='mp3')