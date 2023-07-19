import matplotlib.pyplot as plt
import numpy as np
import math

def derivative(f, x, h):
    return (f(x+h) - f(x)) / h

def func1(x):
    c0d = 1
    d = 1
    t1 = 1
    c1 = (c0d / (2 * math.sqrt(math.pi*d*t1))) * (np.exp(-(x**2)/4*d*t1))
    return c1

def func4(x):
    c0d = 1
    d = 1
    t4 = 4
    c4 = (c0d / (2 * math.sqrt((math.pi)*d*t4))) * (np.exp(-(x**2)/(4*d*t4)))
    return c4

h = 0.001
xrange = np.arange(-10, 10, h)

x_list = []
c1_list = []
c4_list = []
f1_list = []
f4_list = []
xrange_list = []

for x in xrange:
    xrange_list.append(x)
    c1_list.append(func1(x))
    c4_list.append(func4(x))
    f1 = -1*derivative(func1, x, h)
    f1_list.append(f1)
    f4 = -1*derivative(func4, x, h)
    f4_list.append(f4)


###plot###
fig = plt.figure()

ax1 = fig.add_subplot(111)
t = np.linspace(0.0,10.0,1000)
fs = 1.0
y1 = np.sin(2.0*np.pi*fs*t)
ln_c1=ax1.plot(xrange_list, c1_list,'blue',linestyle = "-",label=r'$c_t=1$')
ln_c4=ax1.plot(xrange_list, c4_list,'red',linestyle = "--",label=r'$c_t=4$')

ax2 = ax1.twinx()
y2 = 10.0*t + 5.0
ln_f1=ax2.plot(xrange_list,f1_list,'green',linestyle = "-",label=r'$f_t=1$')
ln_f4=ax2.plot(xrange_list,f4_list,'orange',linestyle = "--",label=r'$f_t=4$')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='lower right')

ax1.set_xlabel('t')
ax1.set_ylabel(r'$content$')
ax1.grid(True)
ax2.set_ylabel(r'$flux$')

plt.title('Relation between concentration c and distance x yields',fontsize=10)
plt.savefig("result_q2-1.png", format="png")
plt.show()