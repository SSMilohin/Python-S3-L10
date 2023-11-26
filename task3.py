import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Функция для получения координат точек фигуры Лисажу
def lissajous_curve(a, b, delta, t):
    x = np.sin(a*t + delta)
    y = np.sin(b*t)
    return x, y


fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)


# Функция инициализации анимации
def init():
    line.set_data([], [])
    return line,


# Функция обновления кадра анимации
def update(frame):
    a = 3
    b = 2
    delta = 0
    t = np.linspace(0, 2*np.pi, 100)
    x, y = lissajous_curve(a, b, delta, frame*t)
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), init_func=init, blit=True)

plt.show()
