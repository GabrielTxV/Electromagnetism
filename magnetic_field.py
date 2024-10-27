import numpy as np
import matplotlib.pyplot as plt

# Constantes
mu_0 = 4 * np.pi * 1e-7  # Permeabilidade magnética do vácuo
I = 100.0  # Corrente em amperes

# Posição do fio
x_fio = 0
y_fio = 0

# Define uma grade de pontos no espaço centrada no fio
x = np.linspace(x_fio - 1, x_fio + 1, 20)  # 20 pontos ao redor do fio
y = np.linspace(y_fio - 1, y_fio + 1, 20)  # 20 pontos ao redor do fio
X, Y = np.meshgrid(x, y)  # Grade 2D

# Calcula o campo magnético em cada ponto da grade
def campo_magnetico(x, y, I, mu_0, x_fio, y_fio):
    r = np.sqrt((x - x_fio)**2 + (y - y_fio)**2)  # Distância do ponto ao fio
    B_magnitude = mu_0 * I / (2 * np.pi * r)  # Magnitude do campo B
    Bx = -B_magnitude * ((y - y_fio) / r)  # Componente x do campo B
    By = B_magnitude * ((x - x_fio) / r)   # Componente y do campo B
    return Bx, By

# Calcula os componentes Bx e By em toda a grade
Bx, By = campo_magnetico(X, Y, I, mu_0, x_fio, y_fio)

# Visualiza as linhas de campo
plt.figure(figsize=(8, 8))
plt.streamplot(X, Y, Bx, By, color=np.hypot(Bx, By), cmap='viridis', linewidth=1)
plt.plot(x_fio, y_fio, 'ro', label="Fio com corrente I")  # Localização do fio

# Posição do ponto ao fio
x_ponto = 0.5
y_ponto = 0
plt.plot(x_ponto, y_ponto, 'bo', label="Ponto")  # Localização do ponto

plt.xlabel("x (metros)")
plt.ylabel("y (metros)")
plt.title("Linhas de Campo Magnético ao Redor de um Fio com Corrente")
plt.colorbar(label="Intensidade do Campo Magnético (T)")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()