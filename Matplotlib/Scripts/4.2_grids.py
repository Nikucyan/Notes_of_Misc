import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# # Method 1
# ##########
# plt.figure()
# # plot 1
# ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 1) # 3 row 3 col.
# ax1.plot([1,2], [1,2])
# # ax1.set_xlabel = plt.xlabel; ax1.set_title = plt.title; ...
# ax1.set_title('title 1')
# # plot 2
# ax2 = plt.subplot2grid((3,3), (1,0), colspan = 2) 
# ax2.plot([1,2], [1,2])
# # plot 3
# ax3 = plt.subplot2grid((3,3), (1,2), rowspan = 2) 
# ax4 = plt.subplot2grid((3,3), (2,0))
# ax5 = plt.subplot2grid((3,3), (2,1))
 

# # Method 2
# ##########
# plt.figure()
# gs = gridspec.GridSpec(3,3) # 3x3 grid
# ax1 = plt.subplot(gs[0, :]) # 0th row and occupies all columns
# ax2 = plt.subplot(gs[1, :2])    # 1st row and take place of first 2 col.
# ax3 = plt.subplot(gs[1:, 2])    
# ax4 = plt.subplot(gs[-1, 0])    # last row and 1st col.
# ax5 = plt.subplot(gs[-1, -2])   # last row and last second column

 
# Method 3
##########
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharey=True, sharex=True)    # 2x2; share x and y axis
ax11.scatter([1,2], [2,1])  # scatter plot


plt.tight_layout()
plt.show()