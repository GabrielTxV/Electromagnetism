import numpy as np
from scipy.integrate import quad
# PROGRAMA PARA CALCULAR A CARGA TOTAL EM UM OBJETO COM FORMA DE CONCHA
# Constante da densidade volumétrica de carga (em C/m³)
const_densidade_volumetrica = 3e-4  # 3 * 10^-4 C/m³

# Função que define a densidade volumétrica multiplicada por 4πR²
def densidade_volumetrica(R):
    return const_densidade_volumetrica * R * 4 * np.pi * (R**2)
 
# Função para calcular a carga total
def calcular_carga_total(R_min, R_max):
    carga_total, erro = quad(densidade_volumetrica, R_min, R_max)
    return carga_total

# Definir os limites de R (em metros)
R_min = 0.02  # 2 cm convertidos para metros
R_max = 0.03  # 3 cm convertidos para metros

# Calcular a carga total
carga_total = calcular_carga_total(R_min, R_max)
carga_total_nC = carga_total * 1e9  # Converter de C para nC (nanoCoulombs)

print(f"A carga total na concha é: {carga_total_nC:.3f} nC")
