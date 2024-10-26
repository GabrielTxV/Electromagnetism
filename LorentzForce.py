import numpy as np
import matplotlib.pyplot as plt
# PROGRAMA PARA PLOTAR A FORÇA DE LORENTZ EM UMA PARTÍCULA CARREGADA
# Entrada dos valores
q = 1.5e10                      #float(input("Insira a carga da partícula em Coulombs (C): "))
v = 1e3                      #float(input("Insira a velocidade da partícula em metros por segundo (m/s): "))
B = 5                      #float(input("Insira o campo magnético em Teslas (T): "))
theta_min = 0             #float(input("Insira o ângulo mínimo em graus: "))
theta_max = 360             #float(input("Insira o ângulo máximo em graus: "))

# Ângulos entre a velocidade e o campo magnético
theta_degrees = np.linspace(theta_min, theta_max, 100)
theta_radians = np.radians(theta_degrees)

# Cálculo da magnitude da força de Lorentz
F = np.abs(q) * v * B * np.sin(theta_radians)

# Plot do gráfico
plt.figure(figsize=(10, 6))
plt.plot(theta_degrees, F, label='F = |q| * v * B * sin(θ)', color='blue')
plt.xlabel('Ângulo θ (graus)')
plt.ylabel('Força de Lorentz (N)')
plt.title('Magnitude da Força de Lorentz em função do Ângulo entre v e B')
plt.legend()
plt.grid(True)
plt.show()
