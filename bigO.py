"""
create a plot with algorithmic complexity (time and/or space)
"""

import numpy as np
import matplotlib.pyplot as plt 
import math
import scipy.special

# set up runtime comparison
n = np.linspace(1,12)   # return evenly spaced numbers over a specified interval
labels = ['Constant', 'Log', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential', 'Factorial'] #
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n, scipy.special.factorial(n)] #

# plot setup
fig = plt.figure(figsize=(12,10))
plt.ylim(0, 60)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])


plt.legend(loc=0)
plt.ylabel('Relative runtime')
plt.xlabel('n')
plt.show()

fig.savefig('big_o_comparison_close.png', dpi=100)