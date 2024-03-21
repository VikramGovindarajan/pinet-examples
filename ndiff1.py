import sys
import numpy as np
import scipy
import scipy.linalg
import matplotlib.pyplot as plt

D = 1E2
h = 2.5E-2
Ea = 1E2
nuEf = 2E2

n = 3
A = np.zeros((n,n))
F = np.zeros((n,n))
b = np.zeros(n)
phi = np.zeros(n)
X = np.zeros(n)

lambd = 1

A[0,0] = 4*D+Ea*h**2
A[0,1] = -D
A[0,2] = -D
A[1,0] = -2*D
A[1,1] = 6*D+Ea*h**2
A[2,0] = -2*D
A[2,2] = 2*D+Ea*h**2
F[0,0] = nuEf
F[1,1] = nuEf
F[2,2] = nuEf

phi[0] = 1
phi[1] = 1
phi[2] = 1
X[0] = 1
X[1] = 1
X[2] = 1


for i in range(100):
    S = np.dot(F,phi)
    b = S/lambd
    
    phi1 = scipy.linalg.solve(A,b)
    lambd1 = lambd*np.inner(phi1,X)/np.inner(phi,X)

    e1 = abs(np.linalg.norm(phi1)-np.linalg.norm(phi))
    e2 = abs(lambd1-lambd)
    print (i,e1,e2)
    if(e1<1.E-7 and e2<1.E-5):
        break

    phi = phi1
    lambd = lambd1

else:
    sys.exit("outer iterations not converged. stopping")

print(phi)
print(lambd)

phi2d = np.zeros((2,2))
phi2d[0,0] = phi[0]
phi2d[0,1] = phi[1]
phi2d[1,0] = phi[2]
phi2d[1,1] = phi[0]


from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

x = np.linspace(0,5,3)
y = np.linspace(0,5,3)
x, y = np.meshgrid(x, y)

z = phi2d

levels = MaxNLocator(nbins=10).tick_values(z.min(), z.max())

cmap = plt.colormaps['coolwarm']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, ax = plt.subplots()

im = ax.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax)
ax.set_title('flux distribution')

plt.show()
