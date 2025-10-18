import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

t_start = 0     # tiempo inicial 
t_end = 1       # tiempo final
num_points = 1000 # número de puntos de muestreo

t = np.linspace(t_start, t_end, num_points, endpoint=False)

frecuencia = 5  

onda_diente_sierra = signal.sawtooth(2 * np.pi * frecuencia * t, width=1.0)

# --- 3. GRÁFICO ---
plt.figure(figsize=(10, 4))
plt.plot(t, onda_diente_sierra)

plt.title(f"Señal Diente de Sierra Periódica ({frecuencia} Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-1.5, 1.5) # Para mantener uniformidad visual
plt.grid(True)
plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()
