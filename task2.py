from sympy import *
from sympy import diff , symbols
import math
import numpy as np
from sympy.solvers import solve, nsolve
from sympy import exp
from scipy.optimize import fsolve
from scipy.integrate import odeint
import matplotlib.pyplot as plt
I=1.0
U0=8
n0=0.7
#47.246
w=47.246/1000*2*pi;
def f(y,t):
    U,n=y;
    if t<60:
        u = -0.25;
    else:
        u =0;
    return([I+u-2.3*(1/(1+ exp(-(U+33.8)/5.2)))**3*((1/(1+exp(-(U+35)/5)))+(1/(1+exp((U+60.5)/9.9)))-n)*(U-52)-2.4*(n)**4*(0.73290+(0.96408-0.7329)/(1+exp((U+33.87968)/10.24986)))*(U+84)-0.03*(U+63),((1/(1+exp(-(U+35)/5))-n)*6.4730)/(68/(exp((U+25)/-15)+exp((U+30)/20)))])
t = np.linspace(0,100,200)
sol = odeint(f, [U0,n0],t)
plt.plot(sol[:, 0], sol[:, 1],'b')
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.grid()
plt.show()
