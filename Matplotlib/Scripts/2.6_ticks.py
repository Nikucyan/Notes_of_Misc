import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 150)
y1 = 0.5 * x + 0.1
#y2 = x ** 2	

plt.figure()	# when making multiple figures, use this command before very `plt.plot()`
	# (if not spec., number will show in order)
plt.plot(x, y1, linewidth=10, zorder=1)  # plot the first figure

plt.xlim((-0.5, 0.5))
new_ticks = np.linspace(-1, 1, 9)
#print(new_ticks)
plt.xticks(new_ticks)

#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')	# top and right frames disappear
ax.xaxis.set_ticks_position('bottom')	# set bottom frame as x-axis
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data', 0))	# set x-axis at y = -1
ax.spines['left'].set_position(('data', 0))	# if x and y axes are all set to 0, so that get original pt

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))	# alpha can also be used in plot (70% transparency)

plt.show() 
