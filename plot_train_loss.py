import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np 

def search(lines):
	x = []
	for i in range(len(lines)):
		if lines[i].find('Epoch') != -1:
			if lines[i].find('Loss') != -1:
				loss = lines[i].split('Loss ')[1].split(' (')[0]
				loss = float(loss)
				x.append(loss)
	return x


file1 = open('./results/Experiment #8.txt', 'r')
file2 = open('./results/Experiment #9.txt', 'r')
line1 = file1.readlines()
line2 = file2.readlines()
file1.close()
file2.close()

loss1 = search(line1)
loss2 = search(line2)

x = np.arange(0, 1000, 1)

# the main figure
fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, loss1[0:1000], label="embed_lr=1", color="red", linewidth=2)
ax1.plot(x, loss2[0:1000], label="embed_lr=0.1", color="blue", linewidth=2)
ax1.set_xlabel('iteration', fontsize=14)
ax1.set_ylabel('training loss', fontsize=14)
ax1.set_title('title')
ax1.grid(True)
ax1.legend()


# the subfigure 
left, bottom, width, height = 0.6, 0.4, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, loss1[0:1000], label="embed_lr=1", color="red", linewidth=2)
ax2.plot(x, loss2[0:1000], label="embed_lr=0.1", color="blue", linewidth=2)
ax2.axis([800, 900, 0.05, 0.5])
ax2.grid(True)

# plot the box of selective data
tx0 = 800
tx1 = 900
ty0 = 0.05
ty1 = 0.5
sx = [tx0, tx1, tx1, tx0, tx0]
sy = [ty0, ty0, ty1, ty1, ty0]
ax1.plot(sx, sy, color='purple')

# plot patch lines to connect two figures
xy = (799, 0.5)  # coordinates in the main figure
xy2 = (800, 0.05) # coordinates in the subfigure
con1 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data', axesA=ax1, axesB=ax2)
ax1.add_artist(con1)

xy = (899, 0.5)
xy2 = (899, 0.05)
con2 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data', axesA=ax1, axesB=ax2)
ax1.add_artist(con2)

plt.savefig('./losses.jpg', dpi=256)
plt.show()




