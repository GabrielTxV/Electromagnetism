import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Constantes
g = 9.81  # Gravidade
mass = 0.1  # Massa do supercondutor em kg
k = 1e-5  # Constante de proporcionalidade para a força magnética

# Função para calcular a força de repulsão magnética
def magnetic_repulsion(z):
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

# Configuração da figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parâmetros da animação
time = np.linspace(0, 10, 500)  # Tempo de simulação
z = equilibrium_z + 0.01 * np.sin(2 * np.pi * time)  # Movimento oscilatório em torno do ponto de equilíbrio
x = 0.1 * np.sin(2 * np.pi * time / 5)  # Movimento de deslizamento no eixo x
y = 0.1 * np.cos(2 * np.pi * time / 5)  # Movimento de deslizamento no eixo y

# Função de atualização da animação
def update(num, x, y, z, line):
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    return line,

# Criação da linha 3D
line, = ax.plot(x, y, z, label='Movimento do Supercondutor')

# Configuração dos eixos
ax.set_xlim(-0.2, 0.2)
ax.set_ylim(-0.2, 0.2)
ax.set_zlim(0, 0.1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Simulação 3D do Movimento do Supercondutor')
ax.legend()

# Criação da animação
ani = FuncAnimation(fig, update, frames=len(time), fargs=(x, y, z, line), interval=20, blit=False)

plt.show()