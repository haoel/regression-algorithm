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


