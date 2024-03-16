import sys
import numpy as np
import scipy

D = 1E2
h = 2.5E-2
Ea = 1E2
nuEf = 2E2

n = 3
A = np.zeros((n,n))
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

phi[0] = 1
phi[1] = 1
phi[2] = 1
X[0] = 1
X[1] = 1
X[2] = 1


for i in range(20):

    b[0] = nuEf*phi[0]/lambd
    b[1] = nuEf*phi[1]/lambd
    b[2] = nuEf*phi[2]/lambd

    phi1 = scipy.linalg.solve(A,b)
    lambd1 = lambd*np.inner(phi1,X)/np.inner(phi,X)

    e = abs(np.linalg.norm(phi1)-np.linalg.norm(phi))
    print (i,e)
    if(e<1.E-5):
        break

    phi = phi1
    lambd = lambd1

else:
    sys.exit("outer iterations not converged. stopping")

print(phi)
print(lambd)