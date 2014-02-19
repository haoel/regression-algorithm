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
 
if __name__ == '__main__':
    #pdb.set_trace() 
    import json
    with open("host2.json") as json_data:
        d = json.load(json_data)
        json_data.close()
    
    #result = d['resultData']["t172021094005.cm3"]["0xilovexxx"] 
    result = d['resultData']["t172021095009.cm3"]["0xilovexxx"] 
    cpu = sorted(result["cpu"].items())
    mem = sorted(result["mem"].items())
    load = sorted(result["load5"].items())
    
    from datetime import datetime
    import time
    cpu_list = [] 
    time_list = [] 
    for item in load:
        t = time.mktime(datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S").timetuple())
        time_list.append( t )
        cpu_list.append(float(item[1]))

    x = time_list
    for i in range(len(x)):
        x[i] = x[i]

    x = np.asarray(x)
    y = cpu_list
    n = len(y)    

 
    #f = 0.25
    smoothy = []
    f = 0.005
    for i in range(8):
        f = f + i*0.015
        smoothy.append( lowess(x, y, f=f, iter=1) )


    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
    fig = plt.gcf()
    fig.set_size_inches(22.5,4.5)

    import pylab as pl
    pl.clf()
    pl.plot(x, y, label='Raw Data')
    for i in range(len(smoothy)):
        pl.plot(x, smoothy[i], label='Smoothing '+str(i))
    pl.legend()
    #pl.show()
    pl.savefig('myfig')

