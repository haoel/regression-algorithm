#coding=utf-8 
import numpy as np

def holt_winters_second_order_ewma( x, span=10, beta=1.0/8.0 ):
    n = len(x)
    alpha = 2.0 / ( 1 + span )
    s = np.zeros(( n, ))
    b = np.zeros(( n, ))
    s[0] = x[0]
    for i in xrange( 1, n ):
        s[i] = alpha * x[i] + ( 1 - alpha )*( s[i-1] + b[i-1] )
        b[i] = beta * ( s[i] - s[i-1] ) + ( 1 - beta ) * b[i-1]
    return s

# exponentially-weighted moving average with windows
def ewma_with_window(x, alpha=7.0/8.0, window=30):
    n = len(x)
    y = np.zeros((n,))
    y[0] = x[0]
    if window<=0 :
        for i in xrange(1,n):
            y[i] = alpha * y[i-1] + (1 - alpha) * x[i]
        return y

    for i in xrange(1, n):
        if i<window :
            #pdb.set_trace()
            y[i] = alpha * y[i-1] + (1 - alpha) * x[i]
        else:
            tmp = y[i - window]
            for j in xrange(i - window + 1, i):
                tmp = alpha * tmp + (1-alpha) * x[j]
            y[i] = tmp
    return y