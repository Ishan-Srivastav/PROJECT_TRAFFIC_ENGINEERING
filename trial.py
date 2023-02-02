import numpy as np
from numpy.random import random as rnd
import matplotlib.pyplot as plt
from matplotlib import animation

roadlength = 50
numcars = 10
numframes = 1000  #Time
v_max = 5
p = 0.5

positions = np.zeros(numcars)
velocities = np.zeros(numcars)
theta = np.zeros(numcars)
color = np.linspace(0,numcars-1,numcars)

#Initiate r so roadlength = circumference of one lap
r = roadlength/(2*np.pi)

#Initiate positions so the cars are spread out over the road
for i in range(1,numcars):
    positions[i] = positions[i-1] + (roadlength/numcars)

#Create figure        
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.axis('off')

plot1 = ax.scatter(theta, [r]*numcars, c=color)
plot2 = ax.scatter(theta, [r+1]*numcars, c=color)

ax.set_ylim(0,r+2)

#Update positions, animate function runs framenr times
def animate(framenr):
    positions_tmp = np.array(positions, copy=True)

    #Update position and velocity for each car
    for i in range(numcars):

        #Increase velocity if below max
        if velocities[i] < v_max:
                velocities[i] += 1
        #Decrease velocity if car in front is close
        d = positions_tmp[(i+1)%numcars] - positions_tmp[i]
        if d <= 0:
            d += roadlength
        if velocities[i] >= d:
            velocities[i] = d-1
        #Decrease velocity randomly
        if velocities[i] > 0:
            if rnd() < p:
                velocities[i] -= 1

        positions[i] = positions_tmp[i] + velocities[i]
        theta[i] = positions[i]*2*np.pi/roadlength

    plot1.set_offsets(np.c_[theta, [r]*numcars])
    plot2.set_offsets(np.c_[theta, [r+1]*numcars])

    return [plot1, plot2]

# Call the animator, blit=True means only re-draw parts that have changed
anim = animation.FuncAnimation(fig, animate, frames=numframes, interval=100, blit=True, repeat=True)
plt.show()
