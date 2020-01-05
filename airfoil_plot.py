import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0, 2*np.pi, 100)
B = 2.2
E = 0.6
P = 2.050
T = 0.1
C = 0.02
R = 0.005


def xtheta(theta):
    return 0.5 + 0.5*(abs(np.cos(theta))**B/np.cos(theta))


def ytheta(theta):
    return (T/2)*(abs(np.sin(theta))**B/np.sin(theta))*(1-xtheta(theta)**P)+C*np.sin(
        np.pi*xtheta(theta)**E) + R*np.sin(xtheta(theta)*2*np.pi)


x = xtheta(theta)
y = ytheta(theta)


plt.plot(x,y)
plt.ylim(bottom=-1.00)
plt.ylim(top=1.0)
plt.show()
