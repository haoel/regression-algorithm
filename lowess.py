#coding=utf-8 
#import pdb

"""
This module implements the Lowess function for nonparametric regression.
 
Functions:
lowess        Fit a smooth nonparametric regression curve to a scatterplot.
 
For more information, see
 
William S. Cleveland: "Robust locally weighted regression and smoothing
scatterplots", Journal of the American Statistical Association, December 1979,
volume 74, number 368, pp. 829-836.
 
William S. Cleveland and Susan J. Devlin: "Locally weighted regression: An
approach to regression analysis by local fitting", Journal of the American
Statistical Association, September 1988, volume 83, number 403, pp. 596-610.

Reference
—————————
http://en.wikipedia.org/wiki/Local_regression
https://gist.github.com/agramfort/850437
"""
 
from math import ceil
import numpy as np
from scipy import linalg
 
 
def lowess(x, y, f=2./3., iter=3):
    n = len(x)
    r = int(ceil(f*n))
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = np.clip(np.abs((x[:,None] - x[None,:]) / h), 0.0, 1.0)
    w = (1 - w**3)**3
    smoothy = np.zeros(n)
    delta = np.ones(n)
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:,i]
            b = np.array([np.sum(weights*y), np.sum(weights*y*x)])
            A = np.array([[np.sum(weights), np.sum(weights*x)],
                   [np.sum(weights*x), np.sum(weights*x*x)]])
            beta = linalg.solve(A, b)
            smoothy[i] = beta[0] + beta[1]*x[i]
 
        residuals = y - smoothy
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta**2)**2
 
    return smoothy

def savePng(x, raw_y, smooth_ys, smooth_factor, file):
    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
    fig = plt.gcf()
    fig.set_size_inches(22.5,4.5)

    import pylab as pl
    pl.clf()
    pl.plot(x, raw_y, label='Raw Data')
    for i in range(len(smooth_ys)):
        pl.plot(x, smooth_ys[i], label='Smooth('+str(smooth_factor[i])+')')
    pl.legend()
    pl.savefig(file)



if __name__ == '__main__':
    #pdb.set_trace() 
    from readjson import read_json
    cpu, cpu_time, mem, mem_time, load, load_time = read_json("host1.json")
    

    x = np.asarray(cpu_time)
    y = cpu
    n = len(y)    

 
    #f = 0.25
    smoothy = []
    f = []
    base = 0.005
    for i in range(8):
        base = base + i*0.015
        f.append(base)
        smoothy.append( lowess(x, y, f=base, iter=1) )


    savePng(x, y, smoothy, f, "lowess")

