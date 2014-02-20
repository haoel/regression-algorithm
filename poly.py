import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import *
from numpy.random import normal
from scipy.optimize import fmin

from readjson import read_json
cpu, cpu_time, mem, mem_time, load, load_time = read_json("host2.json")

x = asarray(cpu_time)
y = cpu
n = len(y)

p = poly1d( polyfit(x,y,3) )

print p
print p(x[1])



import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(22.5,4.5)

plot(x, y,    label="raw data")
plot(x, p(x), label="polyfit")

legend()

savefig("poly")
