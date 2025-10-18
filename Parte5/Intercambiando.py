import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt
import Energia_potencia_script

N = 1000 
t_max = 10
t = np.linspace(0, t_max, N)
t_central = np.linspace(-t_max/2, t_max/2, N)

# señal 1: Pulso Rectangular (Ancho 4)
pulso = np.where((t >= 3) & (t <= 7), 1.0, 0.0)

# señal 2: Rampa (Pendiente 0.5)
rampa = np.clip(0.5 * t, 0, 1)

# señal 3: Sinc (Aperiódica) - Ya usada previamente, centrada en 0
sinc = np.sinc(t_central * 1.5)

# señal 4: Exponencial Discreta (h[n] causal)
n_exp = np.arange(N)
exponencial = np.exp(-0.01 * n_exp)

def probar_conmutatividad(sig_A, sig_B, nombre_A, nombre_B, fig_num):
    """
    Realiza la convolución A*B y B*A y verifica si son iguales.
    """
    
    conv_AB = np.convolve(sig_A, sig_B, mode='full')
    conv_BA = np.convolve(sig_B, sig_A, mode='full')
    
    len_salida = len(conv_AB)
    t_salida = np.linspace(0, t_max * 2, len_salida) # rango de tiempo estimado para la salida
    
    son_iguales = np.allclose(conv_AB, conv_BA) # verificación numérica
    
    res_AB = Energia_potencia_script.EnergiaPotencia(conv_AB)
    res_BA = Energia_potencia_script.EnergiaPotencia(conv_BA)
    
    print(f"\n--- Combinación {fig_num}: {nombre_A} * {nombre_B} ---")
    print(f"¿Se cumple la Propiedad Conmutativa ({nombre_A}*{nombre_B} == {nombre_B}*{nombre_A})? {son_iguales}")
    print("-------------------------------------------------------------------")
    print(f"E/P de {nombre_A} * {nombre_B}: {res_AB}")
    print(f"E/P de {nombre_B} * {nombre_A}: {res_BA}")
    print("-------------------------------------------------------------------")
    # -------------------------------------------------------------------

    plt.figure(figsize=(10, 4))
    plt.plot(t_salida, conv_AB, label=f'{nombre_A} * {nombre_B}', linewidth=2, alpha=0.7)
    plt.plot(t_salida, conv_BA, '--r', label=f'{nombre_B} * {nombre_A}', alpha=0.5)
    plt.title(f'Combinación {fig_num}: Prueba de Conmutatividad ({nombre_A} y {nombre_B})')
    plt.legend()
    plt.grid(True)
    plt.show()

    return son_iguales

probar_conmutatividad(pulso, rampa, "Pulso", "Rampa", 1)
probar_conmutatividad(rampa, sinc, "Rampa", "Sinc", 2)
probar_conmutatividad(pulso, sinc, "Pulso", "Sinc", 3)
probar_conmutatividad(sinc, exponencial, "Sinc", "Exponencial", 4)
probar_conmutatividad(rampa, exponencial, "Rampa", "Exponencial", 5)



