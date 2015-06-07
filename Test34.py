import numpy as np
from scipy.integrate import odeint

# solve the system dw/dt = f(w, t)
def func(f, t):
        X = f[0]
        Y = f[1]
        Z = f[2]
        return [10*(Y-X), X*(28-Z)-Y, X*Y-(8/3)*Z]

# initial conditions
f = [-1, 1, 0]       # initial condition vector
t  = np.arange(0,50.01,0.01)   # time grid
# solve the DEs
soln = odeint(func, f, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]

#print(S)
#print(Z)
#print(R)

print(soln)