import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 150)
y1 = 2 * x + 1
y2 = x ** 2	

plt.figure()	# when making multiple figures, use this command before very `plt.plot()`
	# (if not spec., number will show in order)
# plt.plot(x, y1)  # plot the first figure

plt.xlim((-1,2))
plt.xlabel('X Test')
plt.ylabel('$f(x)$')
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8, -1, 1.22, 3],
          [r'$really\ bad$', '$bad$', r'normal', 'good', 'very good'])

l1, = plt.plot(x, y2, label = 'up')	
l2, = plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')   
plt.legend(handles=[l1, l2,], labels=['aaa', 'bbb'], loc='best')	

plt.show() 
