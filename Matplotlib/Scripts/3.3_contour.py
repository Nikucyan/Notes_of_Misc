import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    # define the height function
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256 # (res.)
x = np.linspace(-3, 3, n)   # from -3 to 3 with 256 pt.s
y = np.linspace(-3, 3, n)   # x-y is a square
X, Y = np.meshgrid(x, y)    # Create mesh (binding with x and y)

# Fill: Use plt.contourf to filling contours
# X, Y and value for (X, Y) point (Use cmap which is hot color)
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot) # The def. f(x,y) with meshed X and Y

# LINES: Use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors = 'black', linewidth = 0.3)

# LABELS
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()

