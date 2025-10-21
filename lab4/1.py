import numpy as np, matplotlib.pyplot as plt

def z1(a, fi=8e30):
    return (np.pow(np.sin(3*a),-2)+np.cos(7*a)-np.sin(6*a))/(np.tan(a)+fi-2*a)


def z2(a):
   return (13*np.pow(np.tan(a),2)-54*np.tan(a)+98)

xn = 0.1
xk = np.pi * 2
nn = 200
X = np.linspace(xn, xk, nn)

Y = z1(X)
Z = z2(X)
plt.figure(figsize=(10, 6))
plt.plot(X, Y, 'r-', linewidth=2)
plt.title('z2')
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(X, Z, 'r-', linewidth=2)
plt.title('z2')
plt.grid(True, alpha=0.3)
plt.show()
