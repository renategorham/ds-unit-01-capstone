import numpy as np
from numpy import zeros
from numpy import sum
from numpy import log
from scipy.stats import distributions



def bartlett(*args):    
    k = len(args)
    if k < 2:
        raise ValueError("Must enter at least two input sample vectors.")
    Ni = zeros(k)
    ssq = zeros(k,'d')
    for j in range(k):
        Ni[j] = len(args[j])
        ssq[j] = np.var(args[j], ddof=1)
    Ntot = sum(Ni,axis=0)
    spsq = sum((Ni-1)*ssq,axis=0)/(1.0*(Ntot-k))
    numer = (Ntot*1.0-k)*log(spsq) - sum((Ni-1.0)*log(ssq),axis=0)
    denom = 1.0 + (1.0/(3*(k-1)))*((sum(1.0/(Ni-1.0),axis=0))-1.0/(Ntot-k))
    T = numer / denom
    pval = distributions.chi2.sf(T,k-1)  # 1 - cdf
    return T, pval
