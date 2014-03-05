import pdb

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(22.5,4.5)

import pylab as pl


def testLowess(x, y):

    from cylowess import fast_lowess

    smoothy = []
    f = []
    base = 0.005
    y = np.asarray(y)
    #delta = (x.max() - x.min()) * 0.001
    delta = 0 
    for i in range(8):
        base = base + i*0.015
        f.append(base)
        smoothy.append( fast_lowess( x,y, frac=base, iter=1, delta=delta) )
 
    fig = plt.gcf()

    pl.clf()
    pl.plot(x, y, label='Raw Data')
    for i in range(len(smoothy)):
        pl.plot(x, smoothy[i], label='Smooth('+str(f[i])+')')
    pl.legend()
    pl.savefig('./imgs/lowess')
    print "Successfully created picture file lowess.png"




if __name__ == '__main__':
    #pdb.set_trace()
    import numpy as np
    from readjson import read_json
    cpu, cpu_time, mem, mem_time, load, load_time = read_json("./host2.json")


    #x = np.asarray(cpu_time)
    y=[]
    for i in xrange(10):
        y = y+cpu
    x = np.arange(0.0, len(y))

    print "----------------- LOWESS ---------------------"
    testLowess(x, y)
    
