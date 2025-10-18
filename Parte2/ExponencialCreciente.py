import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

t_start = -1        # tiempo inicial
t_end = 2           # tiempo final 
num_points = 1000   # número de puntos de muestreo

t = np.linspace(t_start, t_end, num_points)

exponencial_base = np.exp(t)
ventana_tramo = np.where(np.logical_and(t >= 0, t <= 1), 1.0, 0.0) # representa [u(t) - u(t-1)]
# en T=1 la función cambia de 1 a 0  
onda_exp_creciente = exponencial_base * ventana_tramo

plt.figure(figsize=(10, 4))
plt.plot(t, onda_exp_creciente)

plt.title("Señal Exponencial Creciente (Ventana de -1 a 2)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-0.2, 3.0) 
plt.grid(True)
plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()
