import pdb

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(220.5,4.5)

import pylab as pl



def lowessProcess(x, y):

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
    return f, smoothy
     

def savefile(x,y, smoothy, f):
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
    for i in xrange(30):
        y = y+cpu
    x = np.arange(0.0, len(y))

    print "----------------- LOWESS ---------------------"

    def chunks(l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i+n]

    chunk_size = 1000
    x_chunks = list(chunks(x,chunk_size))
    y_chunks = list(chunks(y,chunk_size))
    
    lowessy=None
    f =[]
    for i in xrange(len(x_chunks)):
        f, smoothy =  lowessProcess(x_chunks[i], y_chunks[i])
        if (lowessy == None):
            lowessy = smoothy
        else:
            #pdb.set_trace()
            for i in range(len(smoothy)):
                lowessy[i]=np.concatenate([lowessy[i],smoothy[i]])

    savefile(x, y, lowessy, f)
        
    
