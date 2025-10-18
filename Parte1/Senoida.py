import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt


A = 1       # amplitud
f = 2      # frecuencia en Hz
t_start = 0 # tiempo inicial
t_end = 1  # tiempo final
num_points = 1000 # número de puntos de muestreo

t = np.linspace(t_start, t_end, num_points) # vector de tiempo
onda_senoidal = A * np.sin(2 * np.pi * f * t) # señal senoidal

plt.figure(figsize=(10, 4)) 
plt.plot(t, onda_senoidal)
plt.title(f"Señal Senoidal ({f} Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()