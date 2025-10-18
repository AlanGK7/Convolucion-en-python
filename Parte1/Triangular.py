import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt


t_start = 0 # tiempo inicial
t_end = 1  # tiempo final
num_points = 1000 # número de puntos de muestreo

t = np.linspace(t_start, t_end, num_points) # vector de tiempo
frecuencia = 5

onda_triangular = signal.sawtooth(2 * np.pi * frecuencia * t, width=0.5) # witdh obtine una onda triangular simetrica

plt.figure(figsize=(10, 4))
plt.plot(t, onda_triangular)
plt.title(f"Señal Triangular Periódica ({frecuencia} Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()