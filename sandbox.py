import matplotlib.pyplot as plt
x = [1.0, 0.1, 0.01, 0.001]
E = [157.1, 17.7, 0.88, 0.079]

plt.plot(x, E, marker = 'o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Delta time in seconds")
plt.ylabel('Euler method to Rk45 error in percent')
plt.savefig('error_vs_dt.png')
plt.show()