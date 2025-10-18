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

# Demostración del escalado (Homogeneidad)
a = 5  # constante de escalado
x_nueva = a * x_senoidal
y_nueva = np.convolve(x_nueva, h_sinc, mode='full')
y_esperada = a * y_salida
son_iguales = np.allclose(y_nueva, y_esperada) 
print(f"¿Se cumple la propiedad de Homogeneidad (a * x --> a * y)? {son_iguales}")

# Gráfico de Homogeneidad
plt.figure(figsize=(10, 4))
plt.plot(t_salida, y_nueva[:len(t_salida)], label='Salida Nueva (Entrada escalada * h)')
plt.plot(t_salida, y_esperada[:len(t_salida)], '--r', label='Salida Esperada (5 * Salida Original)', alpha=0.7)
plt.title(f"Verificación de Linealidad (Homogeneidad, a={a})")
plt.legend()
plt.grid(True)
plt.show()

# demostración de la invarianza temporal (Corrimiento)
tau_muestras = 500  # correr la señal 500 muestras hacia la derecha (retraso)
h_retrasada_larga = np.pad(h_sinc, (tau_muestras, 0), 'constant', constant_values=(0, 0)) # h(t - tau)
y_convolucion_retrasada = np.convolve(x_senoidal, h_retrasada_larga, mode='full') # y[n] con h retrasada

# creamos la salida esperada retrasada y la ajustamos a la longitud de la nueva convolución (CORRECCIÓN)
y_esperada_retrasada = np.pad(y_salida, (tau_muestras, 0), 'constant', constant_values=(0, 0))
y_esperada_retrasada = y_esperada_retrasada[:len(y_convolucion_retrasada)]

# Comparación de arrays completos (CORRECCIÓN)
son_iguales_invariancia = np.allclose(y_convolucion_retrasada, y_esperada_retrasada)

print(f"--- PRUEBA DE INVARIANCIA TEMPORAL (Corrimiento $\\tau={tau_muestras}$ muestras) ---")
print(f"¿Se cumple la propiedad de Invariancia Temporal? {son_iguales_invariancia}")

t_salida_retrasada = np.linspace(t_salida[0] - (tau_muestras / num_points), 
                               t_salida[-1] + (tau_muestras / num_points), 
                               len(y_convolucion_retrasada))
                               
plt.figure(figsize=(10, 4))
plt.plot(t_salida, y_salida, label='y[n] Original', alpha=0.7)
plt.plot(t_salida_retrasada, y_convolucion_retrasada, 'g', label=f'y[n] con h Retrasada $\\tau$')
plt.title(f'Verificación de Invariancia Temporal')
plt.legend()
plt.grid(True)
plt.show()

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