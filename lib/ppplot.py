import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import probplot

#dist is test distribution, currently normal and lognormal
#x is an array of sequences (pandas series, etc) to test
#titles are the corresponding array of titles

def ppplot(dist, a, titles):

#the two array must be of equal length
    try:
        len(a)==len(titles)

    except ValueError:
        print('ValueError:  Arrays must be of equal length.')

    try:
        dist == 'norm'

    except ValueError:
        print('ValueError: dist (distribution must be, norm (normal) or lognorm (lognormal).')

    try:
        dist == 'lognorm'

    except ValueError:
        print('ValueError: dist (distribution must be, norm (normal) or lognorm (lognormal).')
    ppp_data = []
    y_hat_i = []
    s_y = []
#interate through the array of data       
    for i, element in enumerate(a):

#ppp_data is an array of arrays, three levels. Level 1; ppp_data[i][][] is each index in the enumeration
#Level 2 is the theorectical quantile and ordered data (ppp_data[i][0][]) or the slope, and intercept, and r_sq (ppp_data[i][1][])
#Level 3 is the either theorectical quantiles or ordered data (ppp_data[i][0][0 or 1]) or the slope, or intercept or r_sq (ppp_data[i][1][0 or 1 or 2])
        ppp_data.append(probplot(a[i], sparams=(1), dist=dist, fit=True, plot=None, rvalue=True))
           
#Second calculate residuals
        slope = ppp_data[i][1][0]
        intercept = ppp_data[i][1][1]
        x = ppp_data[i][0][0]
        y = ppp_data[i][0][1]
        y_hat_i.append(slope * x + intercept) #The fitted line
       
        l = pd.DataFrame(y_hat_i)  #Lines as data frames for charting

#Third calculate 95% prediction interval
        s_y.append(np.sqrt(np.sum((y - y_hat_i[i])**2) / (len(y) - 2))) #Std. dev. of y

        t_df = t.isf(0.025, len(x) - 2, loc = 0, scale = 1) #t-crit. from SciPy Stats

        y_pred_i_upper.append(y_hat_i[i] + (t_df * s_y[i] * np.sqrt(1 + (1 / len(x)) + (x - x.mean())**2 / ((len(x) - 1) * x.var()))))
    
        y_pred_i_lower.append(y_hat_i[i] - (t_df * s_y[i] * np.sqrt(1 + (1 / len(x)) + (x - x.mean())**2 / ((len(x) - 1) * x.var()))))
        
#Last plot charts
        plt.figure(figsize=(15,15))
        plt.suptitle('Probability Plots', fontsize=20)

        plt.subplot(len(a)//2, 2, i+1)
        plt.scatter(x[i], y[i], 'bo')
        plt.plt(l[i], 'r-')
        plt.fill_between(x[i], upi[i], lpi[i], alpha = 0.25, color = '#99caff')
        plt.plot([],[], 'r-', label = 'Fit')
        plt.plot([],[], 'bo', label = 'Data')
        plt.plot([],[], ' ', label = 'R-Sq: ' + r_sq.astype(str))
        plt.ylabel('Ordered responses')
        plt.xlabel('Theoretical quantiles ')
        plt.title(title[i])
        plt.legend(loc = 2)
        plt.grid()
        
    plt.show()
