import pdb

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(22.5,4.5)

import pylab as pl


def testLowess(x, y):

    from lowess import lowess

    smoothy = []
    f = []
    base = 0.005
    for i in range(8):
        base = base + i*0.015
        f.append(base)
        smoothy.append( lowess(x, y, f=base, iter=1) ) 
 
    fig = plt.gcf()

    pl.clf()
    pl.plot(x, y, label='Raw Data')
    for i in range(len(smoothy)):
        pl.plot(x, smoothy[i], label='Smooth('+str(f[i])+')')
    pl.legend()
    pl.savefig('./imgs/lowess')
    print "Successfully created picture file lowess.png"


def testLinerRegression(x,y):

    from liner import liner_regress

    line1, _, _ = liner_regress(x, y, type=1)

    line2, _, _ = liner_regress(x, y, type=0)

    pl.clf()

    pl.plot(x,line1,'r-',x, line2, 'g-', x,y,'b-')

    pl.savefig("./imgs/liner")
    print "Successfully created picture file liner.png"



def testPolyRegression(x, y):

    from poly import poly_regression

    d = 4
    print  poly_regression(x, y, d, True)
    polyline = poly_regression(x, y, d)


    pl.clf()

    pl.plot(x, y,    label="raw data")
    pl.plot(x, polyline, label="polyfit")

    pl.legend()

    pl.savefig("./imgs/poly")
    print "Successfully created picture file poly.png"

def testHoltWintersEWMAverage(x, y):

    from ewma import holt_winters_second_order_ewma

    beta = 1.0/8.0;
    span = 10.0
    n = len(y)
    ave_y = holt_winters_second_order_ewma(y, span, beta)
    
    pl.clf()
    pl.plot(x, y, label="raw data")
    pl.plot(x, ave_y, label="HoltWintersEMWA")
    pl.legend()
    pl.savefig("./imgs/holt_winters_average")
    print "Successfully created picture file holt_winters_average.png"

def testEWMAverage(x, y):

    from ewma import ewma_with_window

    ave_y =  ewma_with_window(y, 0.8, 50 )
    pl.clf()
    pl.plot(x, y, label="raw data")
    pl.plot(x, ave_y, label="EWMAverage")
    pl.legend()
    pl.savefig("./imgs/emwa_window")
    print "Successfully created picture file emwa_window.png" 

if __name__ == '__main__':
    #pdb.set_trace()
    import numpy as np
    from readjson import read_json
    cpu, cpu_time, mem, mem_time, load, load_time = read_json("./host2.json")


    x = np.asarray(cpu_time)
    y = cpu

    print "----------------- LOWESS ---------------------"
    testLowess(x, y)

    print "------------ Liner Regression ----------------"
    testLinerRegression(x, y)

    print "------------- Poly Regression ----------------"
    testPolyRegression(x, y)

    print "---- Exponential Weighted Moving Average -----"
    testEWMAverage(x, y)   
    testHoltWintersEWMAverage(x, y)
