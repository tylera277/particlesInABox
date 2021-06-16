import numpy as np
import matplotlib.pyplot as plt

def RMS(vel):

    ave = np.mean(vel)
    vel_squared = vel **2

    return ave

def histMaker(n_particles, vel):

    n_bins = 30
    fig,axs = plt.subplots()
    axs.hist(np.sqrt(vel[:,0]**2+vel[:,1]), bins=n_bins)
    plt.scatter(1,1)
    plt.show()