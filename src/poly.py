from numpy import *
from numpy.random import normal

def poly_regression(x, y, d ):
    m = polyfit(x,y,d)
    return  poly1d(m)(x),  poly1d(m)

