import numpy as np 
import matplotlib.pyplot as plt

t_start = -1        
t_end = 2           
num_points = 1000  

t = np.linspace(t_start, t_end, num_points)

escalon_unitario = np.where(t >= 0, 1.0, 0.0)

# --- 3. GRÁFICO ---
plt.figure(figsize=(10, 4))
plt.plot(t, escalon_unitario)

plt.title("Escalón Unitario $u(t)$")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-0.2, 1.2) # ajustamos Y para ver el salto
plt.grid(True)
plt.tight_layout() # ajusta el diseño para evitar solapamientos
plt.show()
