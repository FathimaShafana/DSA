import numpy as np
x = np.logspace(0,15,100,dtype=np.float128)

y_1 = np.ones(100)
y_n = x
y_square = x*x
y_squareroot = np.sqrt(x)
y_nlogn = x*np.log(x)
y_cube = x**3
y_2n = 2**x

import matplotlib.pyplot as plt
fig = plt.figure()
p = fig.add_subplot(1,1,1)
p.set_yscale('log')
p.set_xscale('log')
p.set_xlim(1,10**15)
p.set_ylim(1,10**19)

plt.xlabel('X')
plt.title('Functions')

p.plot(x,y_1,label='1')
p.plot(x,y_n,label='n')
p.plot(x,y_square,label='n^2')
p.plot(x,y_squareroot,label='sqrt(n)')
p.plot(x,y_nlogn,label='nlogn')
p.plot(x,y_cube,label='n^3')
p.plot(x,y_2n,label='2^n')
plt.legend()
plt.show()
