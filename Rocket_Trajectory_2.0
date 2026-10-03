import matplotlib.pyplot as plt
import math as math
import numpy as np

# Vertical rocket motion information
bt = float(input('Burn time of motor in seconds'))
mass = float(input('Mass of rocket in grams'))
mass = mass / 1000
ttl_implse = float(input('Total impulse of motor in N/s'))

#Thrust Curve data
data = np.loadtxt('a8.eng', skiprows=9)
real_times = data[:, 0]
real_thrusts = data[:, 1]

# Horizontal rocket motion information
# windspeed = float(input('Wind speed at time of flight in miles per hour'))

# Creating vertical movement graph
plt.title("Rocket Vertical Movement")
plt.xlabel("Time in Seconds")
plt.ylabel("Distance travelled in Meters")

# Finding maximum altitude
grav = 9.81
avr_thrust = 0
avr_thrust = ttl_implse / bt
weight = mass * grav
F_net = avr_thrust - weight
accel = F_net / mass
vbrnout = accel * bt
btcalc = bt ** 2
vtheight1 = 0.5 * accel * btcalc
vbrnoutcalc = vbrnout ** 2
vbrnoutcalc2 = 2 * grav
vtheight2 = vbrnoutcalc / vbrnoutcalc2
mx_alt = vtheight1 + vtheight2
coasttime = vbrnout / grav

#Fall time calculations
falltmcalc1 = 2 * mx_alt
falltmcalc2 = falltmcalc1 / grav
falltm = math.sqrt(falltmcalc2)
ttlflight = falltm + bt + coasttime
totalupflghttm = bt + coasttime
plt.text(totalupflghttm, mx_alt, "Apogee of trajectory vertically")
plt.scatter(totalupflghttm, mx_alt)
xcalc = 0
#Assigning values to axis
x = []
y = []
velocity = 0
altitude = 0
dt = 0.001
while xcalc < ttlflight:
    xcalc = xcalc + dt
    x.append(xcalc)
    if xcalc <= bt:
        thrust = np.interp(xcalc, real_times, real_thrusts)
        F_netcalc = thrust - weight
        accel = F_netcalc / mass
        velocity = velocity + accel * dt
        altitude = altitude + velocity * dt
        y.append(altitude)

    else:
        velocity = velocity + -grav * dt
        altitude = altitude + velocity * dt
        y.append(altitude)


   



plt.plot(x, y)
print("Old constant-thrust prediction:", mx_alt)
print("New real-curve prediction:", max(y))
plt.show
