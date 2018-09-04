import numpy as np
from numpy import zeros
from numpy import sum
from numpy import asarray
from scipy.stats import distributions


def levene(*args,**kwds):
    center = 'median'
    proportiontocut = 0.05
    for kw, value in kwds.items():
        if kw not in ['center', 'proportiontocut']:
            raise TypeError("levene() got an unexpected keyword argument '%s'" % kw)
        if kw == 'center':
            center = value
        else:
            proportiontocut = value

    k = len(args)
    if k < 2:
        raise ValueError("Must enter at least two input sample vectors.")
    Ni = zeros(k)
    Yci = zeros(k,'d')

    if not center in ['mean','median','trimmed']:
        raise ValueError("Keyword argument <center> must be 'mean', 'median'"
              + "or 'trimmed'.")

    if center == 'median':
        func = lambda x: np.median(x, axis=0)
    elif center == 'mean':
        func = lambda x: np.mean(x, axis=0)
    else:  # center == 'trimmed'
        args = tuple(stats.trimboth(np.sort(arg), proportiontocut) for arg in args)
        func = lambda x: np.mean(x, axis=0)

    for j in range(k):
        Ni[j] = len(args[j])
        Yci[j] = func(args[j])
    Ntot = sum(Ni,axis=0)

    # compute Zij's
    Zij = [None]*k
    for i in range(k):
        Zij[i] = abs(asarray(args[i])-Yci[i])
    # compute Zbari
    Zbari = zeros(k,'d')
    Zbar = 0.0
    for i in range(k):
        Zbari[i] = np.mean(Zij[i], axis=0)
        Zbar += Zbari[i]*Ni[i]
    Zbar /= Ntot

    numer = (Ntot-k)*sum(Ni*(Zbari-Zbar)**2,axis=0)

    # compute denom_variance
    dvar = 0.0
    for i in range(k):
        dvar += sum((Zij[i]-Zbari[i])**2,axis=0)

    denom = (k-1.0)*dvar

    W = numer / denom
    pval = distributions.f.sf(W,k-1,Ntot-k)  # 1 - cdf
    return W, pval
