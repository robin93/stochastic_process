from numpy import append,array
from numpy.random import normal
import matplotlib.pyplot as plt

sigma = 2
n = 100
phi = [0.8]
theta = [-0.8]
burnin = 500

def arma_generator(sigma,n,burnin=10):
	l = max(len(phi),len(theta))
	w = normal(0,sigma,n+burnin)
	ARMA = array([])
	s = 0.0
	for i in range(n+burnin):
		if (i<1):
			ARMA = append(ARMA,w[i])
		else:
			s = 0.0
			for j in range(len(phi)):
				s = s + phi[j]*ARMA[i-j-1]
			for j in range(len(theta)):
				s = s + theta[j]*w[i-j-1]
			ARMA = append(ARMA,s+w[i])
	return ARMA[burnin:] 

x = arma_generator(sigma,n)

print x

plt.plot(x,'r')
plt.plot(x,'or')
plt.show()





"""
Random generation of Gaussian ARMA(p,q) time series.

INPUTS

phi:      An array of length p with the AR coefficients (the AR part of 
          the ARMA model).

theta:    An array of length q with the MA coefficients (the MA part of 
          the ARMA model).

sigma:    Standard deviaton of the Gaussian noise.

n:        Length of the returned time-series.

burnin:   Number of datapoints that are going to be discarded (the higher 
          the better) to avoid dependence of the ARMA time-series on the 
          initial values.
""" 
