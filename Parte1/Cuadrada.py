import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt


fs = 10000  # frecuencia de muestreo
T_total = 1 # 1 segundo de duración
t = np.arange(0, T_total, 1/fs) # vector de tiempo
frecuencia = 5  # frecuencia de la señal en Hz

onda_cuadrada = signal.square(2 * np.pi * frecuencia * t)


# grafico
plt.figure(figsize=(10, 4)) # tamaño de la figura
plt.plot(t, onda_cuadrada)
plt.title(f"Señal Cuadrada Periódica ({frecuencia} Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-1.5, 1.5)

plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()