from matplotlib.pyplot import *
from numpy import *


def f(x, m, s):
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

m = 0;  s_start = 2;  s_stop = 0.2
s_values = linspace(s_start, s_stop, 30)

x = linspace(m -3*s_start, m + 3*s_start, 1000)
# f is max for x=m (smaller s gives larger max value)
max_f = f(m, m, s_stop)

ion()
y = f(x,m,s_stop)
lines = plot(x,y)
axis([x[0], x[-1], -0.1, max_f])
xlabel('x')
ylabel('f')

frame_counter = 0

for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    legend(['s=%4.2f' %s])
    draw()
    savefig('tmp_%04d.png' % frame_counter)
    frame_counter += 1
