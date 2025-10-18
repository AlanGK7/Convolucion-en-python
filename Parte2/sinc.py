import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

t_start = -5        # tiempo inicial
t_end = 5           # tiempo final 
num_points = 1000   # número de puntos de muestreo

t = np.linspace(t_start, t_end, num_points)

sinc = np.sinc(t)

plt.figure(figsize=(10, 4))
plt.plot(t, sinc)

plt.title("Señal $\\text{sinc}(t)$")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-0.3, 1.2) 
plt.grid(True)
plt.tight_layout()
plt.show()

