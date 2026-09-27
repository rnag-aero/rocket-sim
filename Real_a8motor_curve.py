# This is a8 motor data gotten of thrustcurve.org for improvements
# More specifically, this takes the data and plots it, there is a file saved as a8.eng which the data comes from
import numpy as np
import matplotlib.pyplot as plt
import matplotlib; print(matplotlib.get_backend())
data = np.loadtxt('a8.eng', skiprows=9)
real_times = data[:, 0]
real_thrusts = data[:, 1]
plt.plot(real_times, real_thrusts)
plt.show()
