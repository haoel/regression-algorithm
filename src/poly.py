from numpy import *
from numpy.random import normal

def poly_regression(x, y, d, module=False):
    m = polyfit(x,y,d)
    if module :
        return poly1d(m)    
    else:
        return poly1d(m)(x) 

