import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 150)
y1 = 2 * x + 1
#y2 = x ** 2	

plt.figure()	# when making multiple figures, use this command before very `plt.plot()`
	# (if not spec., number will show in order)
plt.plot(x, y1)  # plot the first figure

plt.xlim((-1,2))
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
#plt.yticks([-2,-1.8, -1, 1.22, 3],
#         [r'$really\ bad$', '$bad$', r'normal', 'good', 'very good'])

#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')	# top and right frames disappear
ax.xaxis.set_ticks_position('bottom')	# set bottom frame as x-axis
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data', 0))	# set x-axis at y = -1
ax.spines['left'].set_position(('data', 0))	# if x and y axes are all set to 0, so that get original pt

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5) # actual plotted points: (x0, y0) & (x0, 0), k-- for dashed black line

plt.annotate(r'$2x+1=%s$' % y0, xy = (x0, y0), xycoords = 'data', xytext=(+30, -30), textcoords = 'offset points',
    fontsize = 16, arrowprops = dict(arrowstyle='->', connectionstyle = 'arc3, rad=.2'))

plt.text(-1, 3, r'Test math env. $\mu\ \rho_i$', fontdict={'size': 16, 'color': 'r'})

plt.show() 
