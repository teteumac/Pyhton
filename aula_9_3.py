import math

x=[]
y=[]
t=[]

t1=0.1
i=0

while (t1<5):
    x.append(math.sin(math.cos(math.sqrt(9.80665)*t1)))
    y.append(-1*math.cos(math.cos(math.sqrt(9.80665)*t1)))
    t.append(t1)
    t1+=0.1
    
print('  x     y    z  ')

for n in range(len(t)):
       print("%.2f" % x[n], "%.2f" % y[n], "%.2f" % t[n] )
       
import matplotlib.pyplot as plot_TversusY
import matplotlib.pyplot as plot_TversusX
import matplotlib.pyplot as plot_XversusY

plot_TversusY.plot(t,y)
plot_TversusY.xlabel('t')
plot_TversusY.ylabel('y')
plot_TversusY.show()


plot_TversusX.plot(t,x)
plot_TversusX.xlabel('t')
plot_TversusX.ylabel('x')
plot_TversusX.show()


plot_XversusY.plot(x,y)
plot_XversusY.xlabel('x')
plot_XversusY.ylabel('y')
plot_XversusY.show()


plot_TversusY.plot(t,y)
plot_TversusY.xlabel('t')
plot_TversusY.ylabel('y')
plot_TversusX.plot(t,x)
plot_TversusX.xlabel('t')
plot_TversusX.ylabel('x , y')

