import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
k = 1e-5  # Constante de força para repulsão magnética
mass = 0.01  # Massa do ímã em kg
g = 9.81  # Gravidade 

# Função para calcular a força de repulsão magnética
def magnetic_repulsion(z):
    # Força magnética inversamente proporcional ao quadrado da distância
    return k / (z**2 + 1e-9)  # 1e-9 para evitar divisão por zero

# Função para calcular a força gravitacional
def gravitational_force():
    return mass * g

# Pontos no eixo z (altura do ímã)
z_points = np.linspace(0.01, 0.1, 100)

# Calcula a força magnética em cada ponto
F_magnetic = magnetic_repulsion(z_points)
F_gravity = gravitational_force()

# Encontra o ponto de equilíbrio onde F_magnetic = F_gravity
equilibrium_index = np.argmin(np.abs(F_magnetic - F_gravity))
equilibrium_z = z_points[equilibrium_index]

# Visualização das forças
plt.figure(figsize=(10, 6))
plt.plot(z_points, F_magnetic, label="Força Magnética de Repulsão (N)", color="blue")
plt.axhline(y=F_gravity, color="red", linestyle="--", label="Força Gravitacional (N)")
plt.axvline(x=equilibrium_z, color="green", linestyle="--", label=f"Altura de Equilíbrio ≈ {equilibrium_z:.2f} m")

plt.xlabel("Distância do Supercondutor (m)")
plt.ylabel("Força (N)")
plt.title("Simulação de Levitação Magnética com Supercondutores")
plt.legend()
plt.grid(True)
plt.show()
