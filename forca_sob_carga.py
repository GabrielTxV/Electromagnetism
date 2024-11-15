import numpy as np

# Constante eletrostática (N * m² / C²)
k = 8.99e9

# Definição das cargas em Coulombs
q1 = 10e-6  # carga das cargas fixas
q2 = 20e-6  # carga no ponto (0, 0, 4)

# Posições das cargas fixas em metros
positions = [
    np.array([-3, 0, 0]),
    np.array([3, 0, 0]),
    np.array([0, -3, 0]),
    np.array([0, 3, 0])
]

# Posição da carga q2 em metros
position_q2 = np.array([0, 0, 4])

# Calculando a força total sobre a carga q2
total_force = np.array([0.0, 0.0, 0.0])

for pos in positions:
    # Vetor de posição da carga em relação à carga q2
    r_vector = position_q2 - pos
    # Distância entre as cargas
    r_magnitude = np.linalg.norm(r_vector)
    # Cálculo da força de Coulomb (vetorial)
    force_magnitude = k * q1 * q2 / r_magnitude**2
    force_vector = force_magnitude * (r_vector / r_magnitude)
    # Soma vetorial das forças
    total_force += force_vector

# Exibindo o resultado
print("Força total sobre a carga de 20 µC:", total_force, "N")
print("Magnitude da força total:", np.linalg.norm(total_force), "N")
