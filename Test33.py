import numpy as np
from scipy.integrate import odeint

# solve the system dw/dt = f(w, t)
def func(f, t):
        a=10
        b=28
        c=8/3
        X = f[0]
        Y = f[1]
        Z = f[2]
        return [a*(Y-X), X*(b-Z)-Y, X*Y-c*Z]

# initial conditions
f = [-1, 1, 0]       # initial condition vector
t  = np.linspace(0, 50, 5000)   # time grid

# solve the DEs
soln = odeint(func, f, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]

#print(S)
#print(Z)
#print(R)

print(soln[-1])