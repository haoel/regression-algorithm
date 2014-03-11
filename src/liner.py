#import pdb

from numpy import arange,array,ones,asarray,vstack,linalg
from scipy import stats

def liner_regress(x, y, type=1):
    if (type==1) : 
        A = vstack([x, ones(len(x))]).T
        slope, intercept = linalg.lstsq(A, y)[0]
    else:
        slope, intercept, r, p, std_err = stats.linregress(x,y)
        #print 'r value', r_value
        #print  'p_value', p_value
        #print 'standard deviation', std_err

    print 'y = '+str(slope)+' * x + '+str(intercept)
   
    liney = slope*x + intercept
    return liney, slope, intercept 


def _chunks(lst, size):
    for i in xrange(0, len(lst), size):
        yield lst[i:i+size]

def _liner_regression(x, y, chunks_size, reduce_fn):
    ys = [reduce_fn(yy) for yy in _chunks(y, chunks_size)]
    xs = [max(xx) for xx in _chunks(x, chunks_size)]
    liney, slope, intercept = liner_regression(xs, ys)
    liney = slope*x + intercept
    return liney, slope, intercept

def liner_regression_max(x,y, chunks_size):
    return _liner_regression(x, y, chunks_size, max)

def liner_regression_min(x,y, chunks_size):
    return _liner_regression(x, y, chunks_size, min)
