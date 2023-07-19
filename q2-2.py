import numpy as np
from scipy import integrate
from scipy.special import erf
import math
import matplotlib.pyplot as plt

def f(t):
  return np.e ** (-t ** 2)

# 作成した誤差関数
result_1 = integrate.quad(f, 0, 1)[0] * (2 / np.sqrt(np.pi))

# scipyの誤差関数
result_2 = erf(1)

print(result_1)
print(result_2)


def func(x,t):
    cs = 1
    c0 = 0
    d = 1
    c = cs - (cs-c0)* math.erf(x/(2*math.sqrt(d*t)))
    return c


print(func(2,1))

h = 0.001
xrange = np.arange(0, 10, h)

xrange_list = []
t1_list = []
t4_list = []
t16_list = []

t_range = [1,4,16]


for x in xrange:
    xrange_list.append(x)
    t1_list.append(func(x,1))
    t4_list.append(func(x,4))
    t16_list.append(func(x,16))

###plot###
plt.figure(figsize=(16,9))
plt.plot(xrange_list,t1_list, marker="", color = "red", linestyle = "-", label="c_t=1")
plt.plot(xrange_list,t4_list, marker="", color = "blue", linestyle = "--", label="c_t=4")
plt.plot(xrange_list,t16_list, marker="", color = "orange", linestyle = "--", label="c_t=16")

plt.xlabel('x',fontsize=15)
plt.ylabel('content',fontsize=15)
plt.xlabel('distance',fontsize=15)
plt.xticks([0,2,4,6,8,10])
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.tick_params(labelsize = 15)
plt.legend()
plt.savefig("result_q2-2.png", format="png")
plt.show()


