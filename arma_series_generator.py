from numpy import append,array
from numpy.random import normal

sigma = 1
n = 100

def arma_generator(sigma,n,burnin=10):
	#l = max(len(phi),len(theta))
	w = normal(0,sigma,n+burnin)
	return w

print arma_generator(sigma,n)







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
