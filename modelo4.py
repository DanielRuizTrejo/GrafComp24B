import matplotlib.pyplot as plt
from random import *
from numpy import *

# Parámetros del modelo
a = 0.7
b = 0.5
c = 0.3
e = 0.5  # Aumenta la eficiencia en la conversión de presas a depredadores
dt = 0.001; max_time = 100

# Tiempo inicial y poblaciones
t = 0
x = 1.0  # Población de presas
y = 0.5  # Población de depredadores

# Listas vacías para almacenar tiempo y poblaciones
t_list = []
x_list = []
y_list = []

# Inicializar listas
t_list.append(t)
x_list.append(x)
y_list.append(y)

while t < max_time:
    # Calcular nuevos valores para t, x, y
    t = t + dt
    x = x + (a * x - b * x * y) * dt
    y = y + (-c * y + e * x * y) * dt

    # Almacenar nuevos valores en listas
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

# Graficar los resultados    
plt.plot(t_list, x_list, 'r', label="Población de presas", linewidth=2)
plt.plot(t_list, y_list, 'g', label="Población de depredadores", linewidth=2)

# Añadir etiquetas y título
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.title("Modelo Presa-Depredador")

# Añadir una leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
