import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.square(x) + np.square(y)  # Функция среднеквадратичного отклонения

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='cool')
ax1.set_title('График MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, np.log(z + 1), cmap='cool')
ax2.set_title('График MSE в логарифмической шкале для z')

plt.show()
