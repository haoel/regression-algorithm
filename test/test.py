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

    
