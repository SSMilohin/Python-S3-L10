import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
fig, ax = plt.subplots(2, 2, figsize=(8, 8))

# 3:2
ax[0, 0].plot(np.sin(3*t), np.sin(2*t))
ax[0, 0].set_title('Соотношение частот 3:2')

# 3:4
ax[0, 1].plot(np.sin(3*t), np.sin(4*t))
ax[0, 1].set_title('Соотношение частот 3:4')

# 5:4
ax[1, 0].plot(np.sin(5*t), np.sin(4*t))
ax[1, 0].set_title('Соотношение частот 5:4')

# 5:6
ax[1, 1].plot(np.sin(5*t), np.sin(6*t))
ax[1, 1].set_title('Соотношение частот 5:6')

plt.show()
