import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collisions import wall_collisions, inter_collisions
from gravitySimulation import getAcc, gravSimulator
from histPlotter import histMaker

n_particles = 5000

#vel = np.random.uniform (-0.5, 0.5, (n_particles, 2))
#pos = np.random.randn(n_particles,2)
pos = np.random.uniform(-5, 5, (n_particles, 2))
vel = np.random.uniform(0, 1, (n_particles, 2))

mass = np.ones((n_particles,1))

fig, ax = plt.subplots()
sc = ax.scatter(pos[:,0], pos[:,1],s=0.1)
#plt.xlim(-2, 3)
#plt.ylim(-2, 3)
X, Y = 0, 1
acc = getAcc(pos, mass, 1, 0.01)


def animate(i):
    dt = 0.1
    global pos

    pos += vel * dt

    # functions which handle collisions between walls and particles
    wall_collisions(pos, vel, -5, 5, 5, -5)
    inter_collisions(pos, vel, radius=0.025, softening=0.001)

    # models gravity between particles
    #pos = gravSimulator(pos, vel, mass)


    sc.set_offsets(np.c_[pos[:,0],pos[:,1]])

ani = matplotlib.animation.FuncAnimation(fig, animate, interval =10)
plt.show()

histMaker(n_particles, vel)

if __name__=="__main__":
    pass
