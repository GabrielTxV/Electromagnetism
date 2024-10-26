import numpy as np
from scipy.integrate import dblquad
# PROGRAMA PARA CALCULAR A CARGA TOTAL EM UMA PLACA
# Função que define a densidade superficial de carga σ(x, y) em µC/m²
def densidade_superficial(x, y):
    return 4 * (y**2)  # Densidade superficial dada no problema (4 * y^2 µC/m²)

# Função para calcular a carga total em uma placa
def calcular_carga_total(x_min, x_max, y_min, y_max):
    # Integral dupla para calcular a carga total
    carga_total, erro = dblquad(densidade_superficial, x_min, x_max, lambda x: y_min, lambda x: y_max)
    return carga_total

# Definir os limites de x e y
x_min = -3  # Limite inferior para x
x_max = 3   # Limite superior para x
y_min = -3  # Limite inferior para y
y_max = 3   # Limite superior para y

# Calcular a carga total em µC (pois a densidade está em µC/m²)
carga_total = calcular_carga_total(x_min, x_max, y_min, y_max)
carga_total_mC = carga_total * 1e-3  # Converter de µC para mC
print(f"A carga total na placa é: {carga_total_mC:.6f} mC")
