from numpy import *
from numpy.random import normal

def poly_regression(x, y, d ):
    m = polyfit(x,y,d)
    return  poly1d(m)(x),  poly1d(m)

def _chunks(lst, size):
    for i in xrange(0, len(lst), size):
        yield lst[i:i+size]

def _poly_regression(x, y, d, chunks_size, reduce_fn):
    ys = [reduce_fn(yy) for yy in _chunks(y, chunks_size)]
    xs = [max(xx) for xx in _chunks(x, chunks_size)]
    poly_y, poly_fn = poly_regression(xs, ys, d)
    poly_y = poly_fn(x)
    return poly_y, poly_fn

def poly_regression_max(x, y, d, chunks_size):
    return _poly_regression(x, y, d, chunks_size, max)

def poly_regression_min(x, y, d, chunks_size):
    return _poly_regression(x, y, d, chunks_size, min)
