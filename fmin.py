import matplotlib
matplotlib.use('Agg')

from pylab import *
from numpy import *
from numpy.random import normal
from scipy.optimize import fmin

from readjson import read_json
cpu, cpu_time, mem, mem_time, load, load_time = read_json("host1.json")

# parametric function, x is the independent variable
# and c are the parameters.
# it's a polynomial of degree 2
fp = lambda c, x: c[0]+c[1]*x+c[2]*x*x
real_p = rand(3)

# error function to minimize
e = lambda p, x, y: (abs((fp(p,x)-y))).sum()

# generating data with noise
n = 30
x = linspace(0,1,n)
y = fp(real_p,x) + normal(0,0.05,n)

# fitting the data with fmin
p0 = rand(3) # initial parameter value

x = asarray(cpu_time)
y = cpu
p = fmin(e, p0, args=(x,y))

print 'estimater parameters: ', p
print 'real parameters: ', real_p

xx = linspace(0,1,n*3)
plot(x,y,'bo', xx,fp(real_p,xx),'g', xx, fp(p,xx),'r')

savefig("fmin")
