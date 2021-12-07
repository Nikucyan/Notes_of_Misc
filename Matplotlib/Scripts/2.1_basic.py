import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50) # Generate 50 points from -1 to 1
# y = 2 * x + 1
y = x ** 2	# Try another function

plt.plot(x, y)  # plot
plt.show()  # show figure
