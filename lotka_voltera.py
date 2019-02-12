# Lotka-Volterra model (predator-prey)
#
# First order, non-linear, differential #equations used to describe the
# dynamics of biological systems in which two species interact, one a predator
# and one its prey. They were proposed independently by Alfred J. Lotka in 1925
# and Vito Volterra in 1926:
# du/dt =  a*u - b*u*v
# dv/dt = -c*v + d*b*u*v
#
# https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def dX_dt(X, t, a, b, c, d):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([ a*X[0] - b*X[0]*X[1],
                     -c*X[1] + d*b*X[0]*X[1] ])

a = 1.   # natural growth rate of rabbits, when there's no fox
b = 0.1  # natural death rate of rabbits, due to predation
c = 1.5  # natural death rate of fox, when there's no rabbit
d = 0.75 # the factor describing how many caught rabbits create a new fox
t = np.linspace(0, 15, 1000)     # time
X0 = np.array([10, 5])           # initials conditions: 10 rabbits and 5 foxes
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True, args=(a,b,c,d))

rabbits, foxes = X.T

plt.plot(t, rabbits, 'r-', label='Rabbits')
plt.plot(t, foxes  , 'b-', label='Foxes')
plt.legend(loc='best', numpoints=1)
plt.xlabel('Time')
plt.ylabel('Population')
plt.show()
