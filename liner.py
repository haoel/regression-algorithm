import pdb
import matplotlib
matplotlib.use('Agg')

from numpy import arange,array,ones,asarray
from pylab import plot,show,savefig
from scipy import stats

#pdb.set_trace()

#xi = arange(0,9)
#A = array([ xi, ones(9)])
# linearly generated sequence
#y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
#print (xi, A, y)

from readjson import read_json
cpu, cpu_time, mem, mem_time, load, load_time = read_json("host1.json")

xi = asarray(cpu_time)
y = cpu
#A = array([x, ones(len(x)) ])



slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)

print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err

line = slope*xi+intercept

#print (len(xi), len(y), len(line))
import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(22.5,4.5)


plot(xi,line,'r-',xi,y,'o')

savefig("liner")



