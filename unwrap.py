import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,np.pi,0.1)
y=4.2*np.pi*np.sin(x)
for i in range(len(x)):
    if y[i]<=np.pi:
        y[i]=y[i]
    elif y[i]<=3*np.pi:
        y[i]=y[i]-2*np.pi
    else:
        y[i]=y[i]-4*np.pi

plt.plot(x,y)
plt.figure("2")
plt.plot(x,np.unwrap(2*y)/2)
plt.show()