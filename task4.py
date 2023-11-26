import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(3, figsize=(10, 8))

x = np.linspace(0, 2*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

line1, = ax[0].plot(x, y1, label='sin(x)')
line2, = ax[1].plot(x, y2, label='cos(x)')
line_sum, = ax[2].plot(x, y1 + y2, label='Сумма волн')

ax_freq = plt.axes((0.15, 0.02, 0.65, 0.03))
ax_amp = plt.axes((0.15, 0.06, 0.65, 0.03))

s_freq = Slider(ax_freq, 'Частота', 0.1, 10.0, valinit=1)
s_amp = Slider(ax_amp, 'Амплитуда', 0.1, 2.0, valinit=1)


def update(val):
    freq = s_freq.val
    amp = s_amp.val
    line1.set_ydata(amp * np.sin(freq * x))
    line2.set_ydata(amp * np.cos(freq * x))
    line_sum.set_ydata(line1.get_ydata() + line2.get_ydata())
    fig.canvas.draw_idle()


s_freq.on_changed(update)
s_amp.on_changed(update)

ax[0].legend()
ax[1].legend()
ax[2].set_title('Результат сложения волн')
plt.show()
