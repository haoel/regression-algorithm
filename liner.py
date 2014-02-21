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


if __name__ == '__main__':

    from readjson import read_json
    cpu, cpu_time, mem, mem_time, load, load_time = read_json("host2.json")
    
    x = asarray(cpu_time)
    y = cpu
    
    # --------------------------------------------------
    line1, _, _ =  liner_regress(x, y, type=1)
    # --------------------------------------------------
    line2, _, _ = liner_regress(x, y, type=0) 
    # --------------------------------------------------
    
    import matplotlib
    matplotlib.use('Agg')
    from pylab import plot,show,savefig
    import matplotlib.pyplot as plt
    fig = plt.gcf()
    fig.set_size_inches(22.5,4.5)
    
    plot(x,line1,'r-',x, line2, 'g-', x,y,'b-')
    
    savefig("liner")
    print "Successfully created picture file liner.png"



