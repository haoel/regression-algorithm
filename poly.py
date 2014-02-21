from numpy import *
from numpy.random import normal

def poly_regression(x, y, d, module=False):
    m = polyfit(x,y,d)
    if module :
        return poly1d(m)    
    else:
        return poly1d(m)(x) 

if __name__ == '__main__':

    from readjson import read_json
    cpu, cpu_time, mem, mem_time, load, load_time = read_json("host2.json")
    
    x = asarray(cpu_time)
    y = cpu
    n = len(y)
    
    d = 4 
    print  poly_regression(x, y, d, True)
    polyline = poly_regression(x, y, d)
    
    import matplotlib
    matplotlib.use('Agg')
    from pylab import *
    import matplotlib.pyplot as plt
    fig = plt.gcf()
    fig.set_size_inches(22.5,4.5)
    
    plot(x, y,    label="raw data")
    plot(x, polyline, label="polyfit")
    
    legend()
    
    savefig("poly")
    print "Successfully created picture file poly.png"
