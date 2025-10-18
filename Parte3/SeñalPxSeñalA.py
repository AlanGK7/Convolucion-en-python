import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt
import Energia_potencia_script 

t_start = 0     
t_end = 5       
num_points = 1000 
t = np.linspace(t_start, t_end, num_points)

# ajuste para una señal senoidal de 2 Hz
f_senoidal = 2 
x_senoidal = np.sin(2 * np.pi * f_senoidal * t) 

# Respuesta al impulso sinc(t)
t_sinc_range = np.linspace(-5, 5, 1000) 
h_sinc = np.sinc(t_sinc_range * 1) 

y_salida = np.convolve(x_senoidal, h_sinc, mode='full')

# se ajusa el tiempo de salida para la convolución
len_salida = len(x_senoidal) + len(h_sinc) - 1
t_salida = np.linspace(t_start + t_sinc_range[0], t_end + t_sinc_range[-1], len_salida)

y_salida = np.convolve(x_senoidal, h_sinc, mode='full')


fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=False, figsize=(10, 8))

ax_orig.plot(t, x_senoidal)
ax_orig.set_title('Entrada x(t)')
ax_orig.grid(True)
print(Energia_potencia_script.EnergiaPotencia(x_senoidal))
print("-----------------------------------------------")
ax_win.plot(t_sinc_range, h_sinc)
ax_win.set_title('Respuesta a Impulso h(t)')
ax_win.grid(True)
print (Energia_potencia_script.EnergiaPotencia(h_sinc))
print("-----------------------------------------------")
ax_filt.plot(t_salida, y_salida)
ax_filt.set_title('Salida y(t)')
ax_filt.set_xlabel('Tiempo (s)')
ax_filt.grid(True)
print(Energia_potencia_script.EnergiaPotencia(y_salida))
print("-----------------------------------------------")
plt.tight_layout()
plt.show()