import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ESSE PROGRAMA CRIA UM GIF PARA MOSTRAR A TRAJETORIA DA PARTICULA

# Parâmetros da partícula e do campo magnético
q = 1.0     # Carga da partícula (unidades arbitrárias)
m = 0.1     # Massa da partícula (unidades arbitrárias)
v0 = np.array([1.0, 0.0, 0.0])  # Velocidade inicial (m/s)
B = np.array([0.0, 0.0, 1.0])   # Campo magnético uniforme (unidades arbitrárias)
dt = 0.05   # Passo de tempo em segundos
num_steps = 200  # Número de passos de tempo

# Função para calcular a força de Lorentz
def lorentz_force(q, v, B):
    return q * np.cross(v, B)

# Inicialização das listas para armazenar a posição
positions = []

# Condições iniciais
r = np.array([0.0, 0.0, 0.0])  # Posição inicial
v = v0

# Loop de integração usando o método de Euler
for step in range(num_steps):
    F = lorentz_force(q, v, B)  # Aplicando a força de Lorentz desde o início
    a = F / m
    v = v + a * dt
    r = r + v * dt
    positions.append(r.copy())

# Converter lista para array para facilitar a plotagem
positions = np.array(positions)

# Configuração para a animação
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trajetória da Partícula sob a Força de Lorentz')

# Inicialização da linha para a animação
line, = ax.plot([], [], [], lw=2, color='blue')

# Função de inicialização da animação
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Função de atualização da animação
def update(frame):
    line.set_data(positions[:frame, 0], positions[:frame, 1])
    line.set_3d_properties(positions[:frame, 2])
    return line,

# Criar animação e salvar como GIF
ani = FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True)
ani.save("trajetoria_forca_lorentz.gif", writer=PillowWriter(fps=20))
plt.show()
