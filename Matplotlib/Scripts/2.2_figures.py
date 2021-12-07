import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2	

plt.figure()	# when making multiple figures, use this command before very `plt.plot()`
	# (if not spec., number will show in order)
plt.plot(x, y1)  # plot the first figure

plt.figure(num = 3, figsize = (8, 5))	# specifiy as 'figure 3' and a figure size 8x5
plt.plot(x, y2)	# plot the second figure
plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')   # plot another line with specific color, line width and dashed style in 'Figure 3'
# plot another line with specific color, line width and dashed style in 'Figure 3'

plt.show() 
