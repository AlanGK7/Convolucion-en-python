import numpy as np

def  EnergiaPotencia(senal):

    # largo de la señal
    N = len(senal)
    
    # energía total (E = sum(|x[n]|^2))
    E = np.sum(senal**2)
    
    # potencia media (P = E / N)
    if N > 0:
        P = E / N
    else:
        P = 0.0 # sirve para no dividir por cero
        
    resultados = {
        "energia": E,
        "potencia_media": P
    }
    
    return resultados
