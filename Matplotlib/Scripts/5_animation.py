import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))   # x, y=sin(x)

def anime(i):
    line.set_ydata(np.sin(x+i/10)) # update y data in the function (x no change)
    return line,    # the first of the list (line,)

def init():
    line.set_ydata(np.sin(x))   # set init. value
    return line,


ani = animation.FuncAnimation(fig = fig, func = anime, frames = 100, init_func = init, interval = 20, blit=False)

plt.show()