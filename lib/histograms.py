import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def histograms_6(x, label, title):
    plt.figure(figsize=(15,15))
    plt.suptitle(label + ' by Contact Mode', fontsize=20)

    for i, element in enumerate(x):
        plt.subplot(len(x)//2, 2, i+1)
        plt.hist(x[i], bins=5, density=True)
        x_axis = np.arange(x[i].mean()-3*(x[i].std()), x[i].mean()+3*(x[i].std()), 1)
        plt.plot(x_axis, norm.pdf(x_axis, x[i].mean(),x[i].std()), 'r--')
        plt.title(title[i])
        plt.xlabel(label)
        plt.ylabel('density')
        plt.grid()
        
    plt.show()

'''
    plt.subplot(322)
    plt.hist(x[1], bins=5, density=True)
    x_axis = np.arange(x[1].mean()-3*(x[1].std()), x[1].mean()+3*(x[1].std()), 1)
    plt.plot(x_axis, norm.pdf(x_axis, x[1].mean(),x[1].std()), 'r--')
    plt.title(title[1])
    plt.xlabel(label)
    plt.ylabel('density')

    plt.subplot(323)
    plt.hist(x[2], bins=5, density=True)
    x_axis = np.arange(x[2].mean()-3*(x[2].std()), x[2].mean()+3*(x[2].std()), 1)
    plt.plot(x_axis, norm.pdf(x_axis, x[2].mean(),x[2].std()), 'r--')
    plt.title(title[2])
    plt.xlabel(label)
    plt.ylabel('density')

    plt.subplot(324)
    plt.hist(x[3], bins=5, density=True)
    x_axis = np.arange(x[3].mean()-3*(x[3].std()), x[3].mean()+3*(x[3].std()), 1)
    plt.plot(x_axis, norm.pdf(x_axis, x[3].mean(),x[3].std()), 'r--')
    plt.title(title[0])
    plt.xlabel(label)
    plt.ylabel('density')

    plt.subplot(325)
    plt.hist(x[4], bins=5, density=True)
    x_axis = np.arange(x[4].mean()-3*(x[4].std()), x[4].mean()+3*(x[4].std()), 1)
    plt.plot(x_axis, norm.pdf(x_axis, x[4].mean(),x[4].std()), 'r--')
    plt.title(title[4])
    plt.xlabel(label)
    plt.ylabel('density')

    plt.subplot(326)
    plt.hist(x[5], bins=5, density=True)
    x_axis = np.arange(x[5].mean()-3*(x[5].std()), x[5].mean()+3*(x[5].std()), 1)
    plt.plot(x_axis, norm.pdf(x_axis, x[5].mean(),x[5].std()), 'r--')
    plt.title(title[5])
    plt.xlabel(label)
    plt.ylabel('density')'''

