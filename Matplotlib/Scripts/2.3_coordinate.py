import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 150)
y1 = 2 * x + 1
y2 = x ** 2	

plt.figure()	# when making multiple figures, use this command before very `plt.plot()`
	# (if not spec., number will show in order)
# plt.plot(x, y1)  # plot the first figure

plt.figure(num = 3, figsize = (8, 5))	# specifiy as 'figure 3' and a figure size 8x5
plt.plot(x, y2)	# plot the second figure
plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')   # plot another line with specific color, line width and dashed style in 'Figure 3'
# plot another line with specific color, line width and dashed style in 'Figure 3'

plt.xlim((-1,2))
plt.xlabel('X Test')
plt.ylabel('$f(x)$')
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8, -1, 1.22, 3],
          [r'$really\ bad$', '$bad$', r'normal', 'good', 'very good'])

#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')	# top and right frames disappear
ax.xaxis.set_ticks_position('bottom')	# set bottom frame as x-axis
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data', -1))	# set x-axis at y = -1
ax.spines['left'].set_position(('data', 0))	# if x and y axes are all set to 0, so that get original pt

plt.show() 
