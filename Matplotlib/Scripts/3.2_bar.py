import matplotlib.pyplot as plt
import numpy as np

n = 12  # 12 bars (actually 12 up and 12 down for demo)
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)    # Generate values from 0.5-1 for every n (12)
Y2 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor = '#9999ff', edgecolor = 'white')
plt.bar(X, -Y2, facecolor = '#ff9999', edgecolor = 'white')

# Add texts
for x, y in zip(X, Y1): # zip for looping x->X, y->Y1 dividedly in every step
    plt.text(x, y+0.05, '%.2f' % y, ha = 'center', va = 'bottom') 
    ## %.2f means 2 significant digits; ha = horizontal alignment

for x, y in zip(X, Y2): 
    plt.text(x, -y-0.05, '- %.2f' % y, ha = 'center', va = 'top')

plt.xlim = ((-0.5,n))
plt.ylim = ((-1.25,1.25))
plt.xticks(())	# hide all ticks
plt.yticks(())

plt.show()