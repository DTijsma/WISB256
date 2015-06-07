import numpy as np
from scipy.integrate import odeint
from scipy import linalg


class Lorenz(object):
    """Lorenz Attractors"""
    
    def __init__(self,initial,a=10,b=28,c=8/3):
        self.initial=initial
        self.a=a
        self.b=b
        self.c=c
    
    # Solves ODE in [0,T] with steps dt.
    def solve(self,T,dt):
        # The ODE itself.
        def func(f, t):
            X = f[0]
            Y = f[1]
            Z = f[2]
            return [self.a*(Y-X), X*(self.b-Z)-Y, X*Y-self.c*Z]
        
        timelist=np.arange(0,T,dt)
        # ODE solver.
        soln = odeint(func,self.initial, timelist)
        return soln
    
    # Calculates Jacobian
    def df(self,u):
        return np.matrix[[-self.a,self.a,0],[self.b-u[2],-1,0],[u[1],u[0],-self.c]]
    
    # Checks if eigenvalues of Jacobian matrix are all negative.
    def isStable(self,u):
        eigenvalues=linalg.eig(self.df(u))[0]
        if eigenvalues[0]<0 and eigenvalues[1]<0 and eigenvalues[2]<0:
            return True
        else:
            return False
        
        


#sigma = 10
#rho = 28
#beta = 8/3
#L1 = Lorenz([-1,1,0],sigma,rho,beta)
#u1 = L1.solve(50,.01)
# = Lorenz([-1.001,1.001,.001],sigma,rho,beta)
#u2 = L2.solve(50,.01)
#print(u1[0,0],u2[0,0])
#print(u1[-1,0],u2[-1,0])