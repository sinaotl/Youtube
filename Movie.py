import numpy as np
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line, data2, line2):
    line.set_data(data[...,:num])
    line2.set_data(data2[...,:num])
    time_text.set_text("Points: %.0f" % int(num) )
    return line, line2

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=-1)

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
data = np.array([x,y])

x2 = np.linspace(0,2*np.pi,100)
y2 = np.cos(x)
data2 = np.array([x2,y2])

#################################################################################################################################
fig = plt.figure()
ax = fig.add_subplot(111)
l, = ax.plot([], [], 'r-', label="Sin")
ax2 = ax.twinx()
k = ax2.plot([], [], 'b-', label="Cos")[0]

ax.legend([l,k], [l.get_label(), k.get_label()], loc=0)

ax.set_xlabel("X")
# ax.set_ylabel("Sin")
ax.set_ylim(-1.5,1.5)
ax.set_xlim(0, 7)
# ax2.set_ylabel("Cos")
ax2.set_ylim(-1.5,1.5)
ax2.set_xlim(0, 7)
plt.title('Sin and Cos in play')
time_text = ax.text(0.1, 0.95,"", transform=ax.transAxes, fontsize=15, color='green')
# time_text = ax.text(0.1, 0.95,"", transform=ax.transAxes, fontsize=15, style='italic', bbox={'facecolor':'red', 'alpha':0.5, 'pad':5})
#################################################################################################################################
line_ani = animation.FuncAnimation(fig, update_line, frames=100, fargs=(data, l, data2, k))
line_ani.save('lines.mp4', writer=writer)
