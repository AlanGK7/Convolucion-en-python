import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

t_start = -1        # tiempo inicial 
t_end = 1           # tiempo final 
num_points = 200000

t = np.linspace(t_start, t_end, num_points)


ancho_pulso = 0.0001  # hacer el ancho del pulso lo más pequeño posible

altura_pulso = 1 / ancho_pulso # por propiedad del delta de Dirac

ventana = np.where(
    np.logical_and(t >= -ancho_pulso/2, t <= ancho_pulso/2), 
    altura_pulso, 
    0.0
) 

impulso_continuo_aprox = ventana

plt.figure(figsize=(10, 4))
plt.plot(t, impulso_continuo_aprox) 

plt.title(f"Aproximación Continua de $\\delta(t)$ (Ancho {ancho_pulso}s)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(0, altura_pulso * 1.1) 
plt.grid(True)
plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()

