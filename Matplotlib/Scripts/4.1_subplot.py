import matplotlib.pyplot as plt

plt.figure()

#plt.subplot(2, 2, 1)    # 2 rows, 2 col. This is the 1st plot
plt.subplot(2, 1, 1)    # 2nd method 
plt.plot([0,1], [0,1])

#plt.subplot(2, 2, 2)    # 2 rows, 2 col. This is the 2nd plot
plt.subplot(2, 3, 4)    # 2nd row, but with 3 columns (actually at 4th position)
plt.plot([0,1], [0,2])

#plt.subplot(2, 2, 3)    # 2 rows, 2 col. This is the 3rd plot
plt.subplot(2, 3, 5) 
plt.plot([2,1], [0,0.5])    # (2,0) - (1,0.05)

#plt.subplot(224)    # 2 rows, 2 col. This is the 4th plot
plt.subplot(2, 3, 6) 
plt.plot([0,1], [0,4])

plt.show()